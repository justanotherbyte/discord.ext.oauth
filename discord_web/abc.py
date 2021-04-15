import aiohttp
from typing import Optional, List
from discord import Permissions
from . import checks


class AccessToken:
    def __init__(self, token_response : dict):
        self._token_response = token_response

    def __str__(self):
        return self.access_token

    @property
    def access_token(self) -> str:
        return self._token_response["access_token"]

    @property
    def token_type(self) -> str:
        return self._token_response["token_type"]

    @property
    def expires_in(self) -> int:
        return self._token_response["expires_in"]

    @property
    def refresh_token(self) -> str:
        return self._token_response["refresh_token"]

    @property
    def scope(self) -> str:
        return self._token_response["scope"]
    
class Oauth2Guild:
    def __init__(self, payload_data : dict):
        self._payload = payload_data

    def __str__(self) -> str:
        return self.name

    @property
    def id(self) -> int:
        return int(self._payload["id"])

    @property
    def name(self) -> str:
        return self._payload["name"]

    @property
    def icon_url(self) -> str:
        icon_hash = self._payload["icon"]
        return "https://cdn.discordapp.com/icons/{}/{}.png".format(self.id, icon_hash)

    @property
    def is_fetched_member_owner(self) -> bool:
        return self._payload["owner"]
    
    @property
    def fetched_member_permissions(self) -> Permissions:
        return Permissions(int(self._payload["permissions"]))

    @property
    def features(self) -> bool:
        return self._payload["features"]

class Oauth2Member:
    def __init__(self, member_payload : dict, access_token : str, session : aiohttp.ClientSession = None):
        self._payload = member_payload
        self.__session__ = session or aiohttp.ClientSession(headers = {'Content-Type': 'application/x-www-form-urlencoded'})
        self.__token__ = access_token
        

    def __str__(self):
        return "{}#{}".format(self.username, self.discriminator)

    
    async def fetch_guilds(self, access_token : Optional[str] = None) -> List[Oauth2Guild]:
        access_token = access_token or self.__token__
        async with self.__session__.get("https://discord.com/api/v8/users/@me/guilds", headers = {"Authorization" : "Bearer {}".format(access_token)}) as response:
            data = await response.json()
            guilds = []
            for guild in data:
                guild_obj = Oauth2Guild(guild)
                guilds.append(guild_obj)

            return guilds



    @property
    def id(self) -> int:
        return int(self._payload["id"])

    @property
    def username(self) -> str:
        return self._payload["username"]

    @property
    def avatar_url(self) -> str:
        avatar_hash = self._payload["avatar"]
        _id = self.id
        return "https://cdn.discordapp.com/avatars/{}/{}.png".format(_id, avatar_hash)

    @property
    def discriminator(self) -> str:
        return self._payload["discriminator"]

    @property
    def public_flags(self) -> int:
        return self._payload["public_flags"]

    @property
    def flags(self) -> int:
        return self._payload["flags"]

    @property
    def locale(self) -> str:
        return self._payload["locale"]

    @property
    def mfa_enabled(self) -> bool:
        return self._payload["mfa_enabled"]

    @property
    def email(self) -> str or None:
        return self._payload["email"]

    @property
    def verified(self) -> bool:
        return self._payload["verified"]


    


    


    