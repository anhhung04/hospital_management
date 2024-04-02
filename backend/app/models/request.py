from typing import Annotated
from fastapi import Header

AUTH_HEADER = "Authorization"

TokenHeader = Annotated[str, Header(alias=AUTH_HEADER)]
