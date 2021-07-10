import weakref

from typing import Optional, Union, List

from .http import Route, HTTPClient
from .token import AccessTokenResponse
from .user import User


__all__: tuple = (
    "OAuth2Client",
)


class OAuth2Client:
    """
    A class representing a client interacting with the discord OAuth2 API.
    """
    def __init__(
        self,
        *,
        client_id: int,
        client_secret: str,
        redirect_uri: str,
        scopes: Optional[List[str]] = None
    ):
        """A class representing a client interacting with the discord OAuth2 API.

        :param client_id: The OAuth application's client_id
        :type client_id: int
        :param client_secret: The OAuth application's client_secret
        :type client_secret: str
        :param redirect_uri: The OAuth application's redirect_uri. Must be from one of the configured uri's on the developer portal
        :type redirect_uri: str
        :param scopes: A list of OAuth2 scopes, defaults to None
        :type scopes: Optional[List[str]], optional
        """
        self._id = client_id
        self._auth = client_secret
        self._redirect = redirect_uri
        self._scopes = " ".join(scopes) if scopes is not None else None

        self.http = HTTPClient()
        self.http._state_info.update(
            {
                "client_id": self._id,
                "client_secret": self._auth,
                "redirect_uri": self._redirect,
                "scopes": self._scopes,
            }
        )

        self._user_cache = weakref.WeakValueDictionary()

    async def exchange_code(self, code: str) -> AccessTokenResponse:
        """Exchanges the code you receive from the OAuth2 redirect.

        :param code: The code you've received from the OAuth2 redirect
        :type code: str
        :return: A response class containing information about the access token
        :rtype: AccessTokenResponse
        """
        route = Route("POST", "/oauth2/token")
        post_data = {
            "client_id": self._id,
            "client_secret": self._auth,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self._redirect,
        }
        if self._scopes is not None:
            post_data["scope"] = self._scopes
        request_data = await self.http.request(route, data=post_data)
        token_resp = AccessTokenResponse(data=request_data)
        return token_resp

    async def refresh_token(self, refresh_token: Union[str, AccessTokenResponse]) -> AccessTokenResponse:
        """Refreshes an access token. Takes either a string or an AccessTokenResponse.

        :param refresh_token: The refresh token you received when exchanging a redirect code
        :type refresh_token: Union[str, AccessTokenResponse]
        :return: A new access token response containg information about the refreshed access token
        :rtype: AccessTokenResponse
        """
        refresh_token = (
            refresh_token if isinstance(refresh_token, str) else refresh_token.token
        )
        route = Route("POST", "/oauth2/token")
        post_data = {
            "client_id": self._id,
            "client_secret": self._auth,
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        }
        request_data = await self.http.request(route, data=post_data)
        token_resp = AccessTokenResponse(data=request_data)
        return token_resp

    async def fetch_user(self, access_token_response: AccessTokenResponse) -> User:
        """Makes an api call to fetch a user using their access token.

        :param access_token_response: A class holding information about an access token
        :type access_token_response: AccessTokenResponse
        :return: Returns a User object holding information about the select user
        :rtype: User
        """
        access_token = access_token_response.token
        route = Route("GET", "/users/@me")
        headers = {"Authorization": "Bearer {}".format(access_token)}
        resp = await self.http.request(route, headers=headers)
        user = User(http=self.http, data=resp, acr=access_token_response)
        self._user_cache.update({user.id: user})
        return user

    def get_user(self, id: int) -> Optional[User]:
        """Gets a user from the cache. The cache is a WeakValueDictionary, so objects may be removed without notice.

        :param id: The id of the user you want to get
        :type id: int
        :return: A possible user object. Returns None if no User is found in cache.
        :rtype: Optional[User]
        """
        user = self._user_cache.get(id)
        return user

    async def close(self):
        """Closes and performs cleanup operations on the client, such as clearing its cache.
        """
        self._user_cache.clear()
        await self.http.close()
