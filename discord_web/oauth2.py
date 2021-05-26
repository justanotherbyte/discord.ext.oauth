import aiohttp
from . import abc
from . import checks
from typing import List


# https://discord.com/api/oauth2/authorize?client_id=770301542170361896&redirect_uri=http%3A%2F%2Flocalhost%3A8000&response_type=code&scope=identify%20email


class Oauth2Client:
    def __init__(
        self, client_id: int, client_secret: str, redirect_uri: str, scopes: List[str]
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.__session__ = aiohttp.ClientSession(
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            raise_for_status=True,
        )
        self.oauth2_endpoint = "https://discord.com/api/v9/oauth2/token"
        self.base_member_endpoint = "https://discord.com/api/v9/users/@me"
        self.scopes = " ".join(scopes)

    async def exchange_code(self, authorization_code: str) -> abc.AccessToken:
        exchange_data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "authorization_code",
            "code": authorization_code,
            "redirect_uri": self.redirect_uri,
            "scope": self.scopes,
        }
        async with self.__session__.post(
            self.oauth2_endpoint, data=exchange_data
        ) as response:
            data = await response.json()
            return abc.AccessToken(data)

    async def fetch_member(self, access_token: str) -> abc.Oauth2Member:
        headers = {"Authorization": "Bearer {}".format(access_token)}
        async with self.__session__.get(
            self.base_member_endpoint, headers=headers
        ) as user_response:
            data = await user_response.json()
            return abc.Oauth2Member(data, access_token)

    async def refresh_token(self, refresh_token: str) -> abc.AccessToken:
        exchange_data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        }
        async with self.__session__.post(
            self.oauth2_endpoint, data=exchange_data
        ) as response:
            data = await response.json()
            return abc.AccessToken(data)

    async def close(self):
        return await self.__session__.close()
