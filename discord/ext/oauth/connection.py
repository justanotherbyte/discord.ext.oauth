from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional

from discord.enums import Enum, try_enum

if TYPE_CHECKING:
    from discord.types.integration import BotIntegration


class VisibilityType(Enum):
    none = 0
    everyone = 1


class Connection:
    def __init__(self, data: Dict[str, Any]):
        self._data = data

        self.id: int = data["id"]
        self.name: str = data["name"]
        self.type: str = data["type"]
        self.revoked: Optional[bool] = data.get("revoked")
        self.integrations: List[BotIntegration] = data.get("integrations", [])
        self.verified: bool = data["verified"]
        self.friend_sync: bool = data["friend_sync"]
        self.show_activity: bool = data["show_activity"]
        self.visibility = try_enum(VisibilityType, data["visibility"])