from typing import Union

from .http import HTTPClient, Route

class AccessTokenResponse:
    def __init__(self, *, data: dict):
        self._data = data
        self.token = self._data.get("access_token")
        self.token_type: str = self._data.get("token_type")
        self.expires_in = self._data.get("expires_in")
        self.refresh_token: str = self._data.get("refresh_token")
        self.scope: str = self._data.get("scope")

class User:
    def __init__(self, http: HTTPClient, *, data: dict, acr: AccessTokenResponse):
        self._data = data
        self._http = http
        self._acr: AccessTokenResponse = acr

        self._avatar_hash = self._data.get("avatar")
        self._avatar_format = "gif" if self._avatar_hash.startswith("a") else "png"

        self.id: int = int(self._data.get("id"))
        self.name: str = self._data.get("name")
        self.avatar_url: str = "https://cdn.discordapp.com/avatars/{0.id}/{0._avatar_hash}.{0._avatar_format}".format(self)
        self.discriminator: int = int(self._data.get("discriminator"))
        self.mfa_enabled: bool = self._data.get("mfa_enabled")
        self.email: str = self._data.get("email")
        self.verified: bool = self._data.get("verified")
        self.access_token: str = self._acr.token
        self.refresh_token: str = self._acr.refresh_token

    def __str__(self) -> str:
        return "{0.id}#{0.discriminator}".format(self)

    def __repr__(self) -> str:
        return "<User id={0.id} name={0.name} discriminator={0.discriminator} verified={0.verified}>".format(self)

    async def refresh(self) -> AccessTokenResponse:
        refresh_token = self.refresh_token
        route = Route("POST", "/oauth2/token")
        post_data = {
            "client_id": self._id,
            "client_secret": self._auth,
            "grant_type": "refresh_token",
            "code": refresh_token
        }
        request_data = await self._http.request(route, data=post_data)
        token_resp = AccessTokenResponse(data=request_data)
        self.refresh_token = token_resp.refresh_token
        self.access_token = token_resp.token
        self._acr = token_resp
        return token_resp

