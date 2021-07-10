from datetime import datetime, timedelta

class AccessTokenResponse:
    """
    A class representing an Access Token Response sent by the OAuth2 API.

    Attributes
    ---------
    token: str
        The access token for the authenticated user
    token_type: str
        The type of access token
    expires_in: int
        The seconds representation for when the token will expire
    refresh_token: str
        The refresh token authenticating you to refresh this access token
    scope: str
        The scope/s this access token gives data for
    expires_at: datetime
        The datetime representation for when the token will expire
    """
    def __init__(self, *, data: dict):
        """A class representing an Access Token Response sent by the OAuth2 API.

        :param data: The raw payload returned by the api
        :type data: dict
        """
        self._data = data
        self.token = self._data.get("access_token")
        self.token_type: str = self._data.get("token_type")
        self.refresh_token: str = self._data.get("refresh_token")
        self.scope: str = self._data.get("scope")
        self.expires_in: int = self._data.get("expires_in")
        self.expires_at: datetime = datetime.now() + timedelta(seconds = self.expires_in)
