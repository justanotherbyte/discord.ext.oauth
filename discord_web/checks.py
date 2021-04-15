from .errors import *

async def screen_response(response : dict):
    if response.get("error") == "invalid_client":
        raise InvalidClient("Invalid Client Credentials Passed to Oauth2 Client")
    elif response.get("error") == "invalid_request":
        error = response.get("error_description")
        raise InvalidRequest(error)
    elif response.get("message") == "401: Unauthorized":
        raise Unauthorized("Unauthorized Requests. Check your scopes on your developer portal")
