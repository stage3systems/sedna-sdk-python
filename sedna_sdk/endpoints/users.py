class UsersAPI:
    def __init__(self, client):
        self.client = client

    def list(self):
        return self.client._request("GET", "/user")