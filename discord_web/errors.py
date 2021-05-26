class InvalidClient(Exception):
    pass


class InvalidRequest(Exception):
    def __init__(self, error: str):
        self.error = error

    def __str__(self) -> str:
        return self.error


class Unauthorized(Exception):
    pass
