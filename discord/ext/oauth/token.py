from datetime import datetime, timedelta

class AccessTokenResponse:
    def __init__(self, *, data: dict):
        """A class representing an Access Token Response sent by the OAuth2 API.

        :param data: The raw payload returned by the api
        :type data: dict
        """
        self._data = data
        self.token = self._data.get("access_token")
        self.token_type: str = self._data.get("token_type")
        self.expires_in = self._data.get("expires_in")
        self.refresh_token: str = self._data.get("refresh_token")
        self.scope: str = self._data.get("scope")
        self.expires_in: int = self._data.get("expires_in")
        self.expires_at: datetime = datetime.now() + timedelta(seconds = self.expires_in)
