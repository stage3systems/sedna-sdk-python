class JobReferencesAPI:
    def __init__(self, client):
        self.client = client

    def list(self):
        return self.client._request("GET", "/job-reference")