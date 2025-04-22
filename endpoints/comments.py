class CommentsAPI:
    def __init__(self, client):
        self.client = client

    def list(self, message_id):
        return self.client._request("GET", f"/messages/{message_id}/comments")

    def create(self, message_id, data):
        return self.client._request("POST", f"/messages/{message_id}/comments", json=data)