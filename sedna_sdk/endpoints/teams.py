class TeamsAPI:
    def __init__(self, client):
        self.client = client

    def list(self):
        return self.client._request("GET", "/team")

    def get(self, team_id):
        return self.client._request("GET", f"/team/{team_id}")