from __future__ import annotations

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User

__all__: tuple = (
    "Guild",
)


class Guild:
    """
    A class representing a PartialGuild object sent by the OAuth2 API. This is not meant to be manually created.

    Attributes
    ---------
    user: User
        The user attached to this guild
    name: str
        The name of the guild
    id: int
        The id of the guild
    icon_url: str
        The asset url for the icon of the guild
    is_user_owner: bool
        Whether or not the user attached to this guild is the owner of the guild
    features: List[str]
        A list of enabled guild features
    """
    def __init__(self, *, data: dict, user: User):
        self._data = data

        self._icon_hash = self._data.get("icon")
        if self._icon_hash is None:
            self._icon_format = None
        else:
            self._icon_format = "gif" if self._icon_hash.startswith("a") else "png"

        self.user = user

        self.id: int = int(self._data.get("id"))
        self.name: str = self._data.get("name")
        self.icon_url: str = "https://cdn.discordapp.com/icons/{0.id}/{0._icon_hash}.{0._icon_format}".format(self) if self._icon_format is not None else None
        self.is_user_owner: bool = self._data.get("owner")
        self.features: List[str] = self._data.get("features")
        self.permissions: int = int(self._data.get("permissions"))

    def add_attached_user_to_guild(
        self,
        bot_token: str,
        **kwargs
    ):
        return self.user.add_to_guild(self.id, bot_token, **kwargs)
        