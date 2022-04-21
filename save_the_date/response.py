from __future__ import annotations

import pydantic


class SaveTheDatePlusOne(pydantic.BaseModel):
    full_name: str
    age: int = None


class SaveTheDateResponse(pydantic.BaseModel):
    full_name: str
    email_address: str
    plus_ones: list[SaveTheDatePlusOne] = []
    is_hotel_needed: bool
    is_vaccinated: bool
