# Response helper functions

from fastapi import Response

from ..schemas.common_schemas import CamelCaseBaseModel


class HTTPResponse(Response):
    """HTTPResponse class for returning HTTP responses with JSON content."""
    def __init__(self, status_code: int, content: CamelCaseBaseModel):
        super().__init__(content=content.to_json(), status_code=status_code, media_type="application/json")


__all__ = ["HTTPResponse"]
