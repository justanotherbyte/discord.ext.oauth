from __future__ import annotations

from typing import List, TYPE_CHECKING

from .http import HTTPClient, Route

if TYPE_CHECKING:
    from .guild import Guild
    from .token import AccessTokenResponse


__all__: tuple = (
    "User",
)


class User:
    """
    A class representing a user object, containing information from the OAuth2 API.

    Attributes
    ---------
    id: int
        The id of the user
    name: str
        The username of the user
    avatar_url: str
        The asset url for the user's avatar
    discriminator: str
        The user's discriminator
    mfa_enabled: bool
        Whether the user has multi-factor authentication (2fa usually) enabled on their account
    email: Optional[str]
        The user's email. Can be None if the user has no email, or you do not have the email scope selected
    verified: bool
        Whether the user has a verified account
    access_token: str
        The access token used to get this user object
    refresh_token: str
        The refresh token to refresh the access token
    """
    def __init__(self, *, http: HTTPClient, data: dict, acr: AccessTokenResponse):
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

        self.guilds: List[Guild] = []  # this is filled in when fetch_guilds is called

    def __str__(self) -> str:
        return "{0.id}#{0.discriminator}".format(self)

    def __repr__(self) -> str:
        return "<User id={0.id} name={0.name} discriminator={0.discriminator} verified={0.verified}>".format(
            self
        )

    async def refresh(self) -> AccessTokenResponse:
        """Refreshes the access token for the user and returns a fresh access token response.

        :return: A class holding information about the new access token
        :rtype: AccessTokenResponse
        """
        refresh_token = self.refresh_token
        route = Route("POST", "/oauth2/token")
        post_data = {
            "client_id": self._http._state_info["client_id"],
            "client_secret": self._http._state_info["client_secret"],
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        }
        request_data = await self._http.request(route, data=post_data)
        token_resp = AccessTokenResponse(data=request_data)
        self.refresh_token = token_resp.refresh_token
        self.access_token = token_resp.token
        self._acr = token_resp
        return token_resp

    async def fetch_guilds(self, *, refresh: bool = True) -> List[Guild]:
        """Makes an api call to fetch the guilds the user is in. Can fill a normal dictionary cache.

        :param refresh: Whether or not to refresh the guild cache attached to this user object. If false, returns the cached guilds, defaults to True
        :type refresh: bool, optional
        :return: A List of Guild objects either from cache or returned from the api call 
        :rtype: List[Guild]
        """
        if not refresh and self.guilds:
            return self.guilds

        route = Route("GET", "/users/@me/guilds")
        headers = {"Authorization": "Bearer {}".format(self.access_token)}
        resp = await self._http.request(route, headers=headers)
        self.guilds = []
        for array in resp:
            guild = Guild(data=array, user=self)
            self.guilds.append(guild)

        return self.guilds
