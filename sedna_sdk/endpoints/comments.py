class CommentsAPI:
    def __init__(self, client):
        self.client = client

    def list(self):
        return self.client._request("GET", "/comment")

    def get_comments_of_message(self, message_id):
        return self.client._request("GET", f"/message/{message_id}/comment")