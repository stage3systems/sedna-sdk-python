class UsersAPI:
    def __init__(self, client):
        self.client = client

    def me(self):
        return self.client._request("GET", "/users/me")