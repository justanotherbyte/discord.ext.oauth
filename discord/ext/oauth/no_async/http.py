import requests

from .errors import HTTPException


__all__: tuple = (
    "Route", 
    "HTTPClient"
)


class Route:
    BASE = "https://discord.com/api/v9"

    def __init__(self, method: str, endpoint: str, **params):
        self.url = self.BASE + endpoint.format(**params)
        self.method = method


class HTTPClient:
    def __init__(self):
        self.__session = None  # filled in later
        self._state_info = {}  # client fills this

    def _create_session(self) -> requests.Session:
        self.__session = requests.Session()
        return self.__session

    def request(self, route: Route, **kwargs) -> dict:
        if self.__session is None or self.__session.closed is True:
            self._create_session()

        headers = kwargs.pop("headers", {})

        headers["Content-Type"] = "application/x-www-form-urlencoded"  # the discord OAuth2 api requires this header to be set to this
        kwargs["headers"] = headers

        resp = self.__session.request(route.method, route.url, **kwargs)
        json = resp.json()
        if 200 <= resp.status_code < 300:
            return json
        else:
            raise HTTPException(resp, json=json)

    def close(self):
        self.__session.close()
        self.__session = None
