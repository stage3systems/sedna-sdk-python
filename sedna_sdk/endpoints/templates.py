class TemplatesAPI:
    def __init__(self, client):
        self.client = client

    def list(self):
        return self.client._request("GET", "/template")

    def get(self, template_id: str, include_doc: bool = False):
        if not include_doc:
            return self.client._request("GET", f"/template/{template_id}")
        return self.client._request("GET", f"/template/{template_id}?include=documents")

    def download(self, doc_id: str):
        response = self.client._raw_request("GET", f"/download/template/document/{doc_id}", stream=True)
        return response.content
