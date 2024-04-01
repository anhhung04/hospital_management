from typing import Annotated
from fastapi import Header

TokenHeader = Annotated[str, Header(alias="Authorization")]
