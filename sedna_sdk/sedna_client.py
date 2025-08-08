import base64
import requests
from .endpoints.templates import TemplatesAPI
from .endpoints.users import UsersAPI
from .endpoints.comments import CommentsAPI
from .endpoints.job_references import JobReferencesAPI
from .endpoints.teams import TeamsAPI

class SednaAPIError(Exception):
    def __init__(self, status_code, message):
        super().__init__(f"Sedna API Error {status_code}: {message}")
        self.status_code = status_code
        self.message = message

class SednaClient:
    def __init__(self, subdomain_or_url, client_id, client_secret):
        if subdomain_or_url.startswith('http://') or subdomain_or_url.startswith('https://'):
            self.base_url = subdomain_or_url.rstrip('/')
        else:
            self.base_url = f"https://{subdomain_or_url}.sednanetwork.com/platform/2019-01-01"
        credentials = f"{client_id}:{client_secret}"
        encoded = base64.b64encode(credentials.encode()).decode()
        self.headers = {
            "Authorization": f"Basic {encoded}",
            "Content-Type": "application/json"
        }

        # Submodules
        self.teams = TeamsAPI(self)
        self.templates = TemplatesAPI(self)
        self.users = UsersAPI(self)
        self.comments = CommentsAPI(self)
        self.job_references = JobReferencesAPI(self)

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, headers=self.headers, **kwargs)
        if not response.ok:
            raise SednaAPIError(response.status_code, response.text)

        if response.content:
            return response.json()
        return None
