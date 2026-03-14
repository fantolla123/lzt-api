class LolzAPIError(Exception):
    def __init__(self, status_code: int, message: str = ""):
        self.status_code = status_code
        self.message = message
        super().__init__(f"[{status_code}] {message}")


class RateLimitError(LolzAPIError):
    def __init__(self, retry_after: float | None = None):
        self.retry_after = retry_after
        super().__init__(429, f"Rate limited. Retry after: {retry_after}s")


class AuthError(LolzAPIError):
    def __init__(self, message: str = "Unauthorized"):
        super().__init__(401, message)


class NotFoundError(LolzAPIError):
    def __init__(self, message: str = "Not found"):
        super().__init__(404, message)
