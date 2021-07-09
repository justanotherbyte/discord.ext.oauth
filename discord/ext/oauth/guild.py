from __future__ import annotations

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User

__all__: tuple = ("Guild",)


class Guild:
    def __init__(self, *, data: dict, user: User):
        self._data = data

        self._icon_hash = self._data.get("icon")
        self._icon_format = "gif" if self._icon_hash.startswith("a") else "png"

        self.user = user

        self.id: int = int(self._data.get("id"))
        self.name: str = self._data.get("name")
        self.icon_url: str = "https://cdn.discordapp.com/icons/{0.id}/{0._icon_hash}.{0._icon_format}".format(
            self
        )
        self.is_user_owner: bool = self._data.get("owner")
        self.features: List[str] = self._data.get("features")
