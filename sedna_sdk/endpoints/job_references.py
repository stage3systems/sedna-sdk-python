class JobReferencesAPI:
    def __init__(self, client):
        self.client = client

    def list(self):
        """
        List all job references.

        Returns:
            List of job reference dictionaries
        """
        return self.client._request("GET", "/job-reference")

    def create(self, data):
        """
        Create a new job reference.

        Args:
            data: Dictionary containing job reference data

        Returns:
            Created job reference dictionary
        """
        return self.client._request("POST", "/job-reference", json=data)

    def get(self, job_reference_id):
        """
        Get a specific job reference by ID.

        Args:
            job_reference_id: ID of the job reference to retrieve

        Returns:
            Job reference dictionary
        """
        return self.client._request("GET", f"/job-reference/{job_reference_id}")

    def update(self, job_reference_id, data):
        """
        Update an existing job reference.

        Args:
            job_reference_id: ID of the job reference to update
            data: Dictionary containing updated job reference data

        Returns:
            Updated job reference dictionary
        """
        return self.client._request("PATCH", f"/job-reference/{job_reference_id}", json=data)

    def delete(self, job_reference_id):
        """
        Delete a job reference.

        Args:
            job_reference_id: ID of the job reference to delete

        Returns:
            Response from the API (typically empty for successful deletion)
        """
        return self.client._request("DELETE", f"/job-reference/{job_reference_id}")