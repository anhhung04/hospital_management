from typing import Annotated
from fastapi import Header

TokenHeader = Annotated[str | None, Header("X-Token")]
