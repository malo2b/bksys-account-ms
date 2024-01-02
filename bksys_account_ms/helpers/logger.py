import logging
from typing import Any


class EndpointFilter(logging.Filter):
    def __init__(
        self,
        path: str,
        *args: Any,
        **kwargs: Any,
    ):
        """Create a new EndpointFilter.

        Args:
            path (str): The path of the endpoint to filter.

        Example:
            ``logger.addFilter(EndpointFilter("/endpoint"))``
        """
        super().__init__(*args, **kwargs)
        self._path = path

    def filter(self, record: logging.LogRecord) -> bool:
        return record.getMessage().find(self._path) == -1
