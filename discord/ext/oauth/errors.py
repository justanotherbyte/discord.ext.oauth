from aiohttp import ClientResponse


class ExtOauthException(Exception):
    """
    The base exception the library always raises
    """


class HTTPException(ExtOauthException):
    """
    The error that is raised whenever an http error occurs
    """

    def __init__(self, resp: ClientResponse, *, json: dict = {}):
        self.resp = resp
        self.msg = json.get("error_description") or json.get("message")

    def __str__(self):
        fmt = "{0.status}: {0.reason}: {1}"
        return fmt.format(self.resp, self.msg)
