class UsersAPI:
    def __init__(self, client):
        self.client = client

    def list(self, page_limit=None, page_offset=None, sso_email=None, **kwargs):
        """
        List users with optional filtering and pagination.

        Args:
            page_limit (int, optional): Number of results per page (defaults to 100)
            page_offset (int, optional): Number of results to skip (defaults to 0)
            sso_email (str, optional): Filter by SSO email address
            **kwargs: Additional filter parameters

        Returns:
            List of user dictionaries
        """
        params = {}

        # Pagination parameters
        if page_limit is not None:
            params['page[limit]'] = page_limit
        if page_offset is not None:
            params['page[offset]'] = page_offset

        # Filter parameters
        if sso_email is not None:
            params['filter[user.ssoEmail]'] = str(sso_email)

        # Handle any additional filter parameters passed via kwargs
        for key, value in kwargs.items():
            if value is not None:
                params[key] = str(value)

        return self.client._request("GET", "/user", params=params)

    def subscribe_to_job_reference(self, user_id: str, job_reference_id: str) -> dict:
        """
        Subscribe a user to a job reference.

        Args:
            user_id: The user's ID
            job_reference_id: The job reference ID

        Returns:
            Created subscription details
        """
        data = {
            "data": [
                {
                    "id": job_reference_id,
                    "type": "job-reference"
                }
            ]
        }
        endpoint = f"/user/{user_id}/relationships/job-reference"
        return self.client._request("POST", endpoint, json=data)

    def unsubscribe_from_job_reference(self, user_id: str, job_reference_id: str) -> bool:
        """
        Unsubscribe a user from a job reference.

        Args:
            user_id: The user's ID
            job_reference_id: The job reference ID

        Returns:
            True if successful
        """
        data = {
            "data": [
                {
                    "id": job_reference_id,
                    "type": "job-reference"
                }
            ]
        }
        endpoint = f"/user/{user_id}/relationships/job-reference"
        self.client._request("DELETE", endpoint, json=data)
        return True

    def list_job_reference_subscriptions(self, user_id: str) -> list:
        """
        List all job reference subscriptions for a user.

        Args:
            user_id: The user's ID

        Returns:
            List of job reference relationships
        """
        endpoint = f"/user/{user_id}/relationships/job-reference"
        return self.client._request("GET", endpoint)
