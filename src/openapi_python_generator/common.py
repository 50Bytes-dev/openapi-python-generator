from enum import Enum
from typing import Dict
from typing import Optional

from pydantic import BaseModel


class LibraryConfig(BaseModel):
    name: str
    library_name: str
    template_name: str
    include_async: bool
    include_sync: bool


class HTTPLibrary(str, Enum):
    """
    Enum for the available HTTP libraries.
    """

    httpx = "httpx"
    requests = "requests"
    aiohttp = "aiohttp"


library_config_dict: Dict[Optional[HTTPLibrary], LibraryConfig] = {
    HTTPLibrary.httpx: LibraryConfig(
        name="httpx",
        library_name="httpx",
        template_name="httpx.jinja2",
        include_async=True,
        include_sync=True,
    ),
    HTTPLibrary.requests: LibraryConfig(
        name="requests",
        library_name="requests",
        template_name="requests.jinja2",
        include_async=False,
        include_sync=True,
    ),
    HTTPLibrary.aiohttp: LibraryConfig(
        name="aiohttp",
        library_name="aiohttp",
        template_name="aiohttp.jinja2",
        include_async=True,
        include_sync=False,
    ),
}
