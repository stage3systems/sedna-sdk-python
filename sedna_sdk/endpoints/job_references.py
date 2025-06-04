class JobReferencesAPI:
    def __init__(self, client):
        self.client = client

    def list(self, page_limit=None, page_offset=None, foreign_key=None, type=None,
             source=None, name=None, ids=None, job_reference_ids=None,
             created_at_since=None, created_at_until=None, **kwargs):
        """
        List job references with optional filtering and pagination.

        Args:
            page_limit (int, optional): Number of results per page (defaults to 100)
            page_offset (int, optional): Number of results to skip (defaults to 0)
            foreign_key (str, optional): Filter by foreign key
            type (str, optional): Filter by type
            source (str, optional): Filter by source
            name (str, optional): Filter by name
            ids (str, optional): Filter by IDs
            job_reference_ids (str, optional): Filter by job reference IDs
            created_at_since (str, optional): Filter by creation date (since)
            created_at_until (str, optional): Filter by creation date (until)
            **kwargs: Additional filter parameters

        Returns:
            List of job reference dictionaries
        """
        params = {}

        # Pagination parameters
        if page_limit is not None:
            params['page[limit]'] = page_limit
        if page_offset is not None:
            params['page[offset]'] = page_offset

        # Filter parameters
        if foreign_key is not None:
            params['filter[foreignKey]'] = foreign_key
        if type is not None:
            params['filter[type]'] = type
        if source is not None:
            params['filter[source]'] = source
        if name is not None:
            params['filter[name]'] = name
        if ids is not None:
            params['filter[ids]'] = ids
        if job_reference_ids is not None:
            params['filter[jobReferenceIds]'] = job_reference_ids
        if created_at_since is not None:
            params['filter[createdAt][since]'] = created_at_since
        if created_at_until is not None:
            params['filter[createdAt][until]'] = created_at_until

        # Handle any additional filter parameters passed via kwargs
        for key, value in kwargs.items():
            if value is not None:
                params[key] = value

        return self.client._request("GET", "/job-reference", params=params)

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