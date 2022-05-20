from pydantic import BaseModel


class WithjoyGuest(BaseModel):
    name: str
    email: str
    party: str


class WithjoyGuestList(BaseModel):
    guests: list[WithjoyGuest]
