class TemplatesAPI:
    def __init__(self, client):
        self.client = client

    def list(self):
        return self.client._request("GET", "/template")

    def get(self, template_id):
        return self.client._request("GET", f"/template/{template_id}")