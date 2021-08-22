from __future__ import annotations

from typing import List, TYPE_CHECKING

from .http import Route
from ..user import User

if TYPE_CHECKING:
    from ..guild import Guild
    from ..token import AccessTokenResponse


__all__: tuple = (
    "User",
)

class NoAsyncUser(User):
    def refresh(self) -> AccessTokenResponse:
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
        request_data = self._http.request(route, data=post_data)
        token_resp = AccessTokenResponse(data=request_data)
        self.refresh_token = token_resp.refresh_token
        self.access_token = token_resp.token
        self._acr = token_resp
        return token_resp

    def fetch_guilds(self, *, refresh: bool = True) -> List[Guild]:
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
        resp = self._http.request(route, headers=headers)
        self.guilds = []
        for array in resp:
            guild = Guild(data=array, user=self)
            self.guilds.append(guild)

        return self.guilds