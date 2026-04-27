class ContactsAPI:
    def __init__(self, client):
        self.client = client

    def list(self):
        return self.client._request("GET", "/contact")

    def get(self, contact_id):
        return self.client._request("GET", f"/contact/{contact_id}")