from __future__ import annotations

import pydantic


class SaveTheDateResponse(pydantic.BaseModel):
    full_name: str
    email_address: str
