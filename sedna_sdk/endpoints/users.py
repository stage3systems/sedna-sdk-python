class UsersAPI:
    def __init__(self, client):
        self.client = client

    def list(self, sso_email=None, page_limit=None, page_offset=None, **kwargs):
        """
        List users with optional filtering and pagination.

        Args:
            sso_email (str, optional): Filter by SSO email address
            page_limit (int, optional): Number of results per page
            page_offset (int, optional): Number of results to skip
            **kwargs: Additional filter parameters

        Returns:
            List of user dictionaries
        """
        params = {}

        # Pagination parameters
        if page_limit is not None:
            params['page_limit'] = page_limit
        if page_offset is not None:
            params['page_offset'] = page_offset

        # Filter parameters
        if sso_email is not None:
            params['sso_email'] = sso_email

        # Handle any additional filter parameters passed via kwargs
        for key, value in kwargs.items():
            if value is not None:
                params[key] = value

        return self.client._request("GET", "/users", params=params)
