class AccessTokenResponse:
    def __init__(self, *, data: dict):
        self._data = data
        self.token = self._data.get("access_token")
        self.token_type: str = self._data.get("token_type")
        self.expires_in = self._data.get("expires_in")
        self.refresh_token: str = self._data.get("refresh_token")
        self.scope: str = self._data.get("scope")

class User:
    def __init__(self, *, data: dict, access_token: str):
        self._data = data

        self._avatar_hash = self._data.get("avatar")
        self._avatar_format = "gif" if self._avatar_hash.startswith("a") else "png"

        self.id: int = int(self._data.get("id"))
        self.name: str = self._data.get("name")
        self.avatar_url: str = "https://cdn.discordapp.com/avatars/{0.id}/{0._avatar_hash}.{0._avatar_format}".format(self)
        self.discriminator: int = int(self._data.get("discriminator"))
        self.mfa_enabled: bool = self._data.get("mfa_enabled")
        self.email: str = self._data.get("email")
        self.verified: bool = self._data.get("verified")
        self.access_token: str = access_token

