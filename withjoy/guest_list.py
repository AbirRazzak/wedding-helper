from pydantic import BaseModel


class WithjoyGuest(BaseModel):
    first_name: str
    last_name: str
    email: str = ''
    party: str = ''


class WithjoyGuestList(BaseModel):
    guests: list[WithjoyGuest]
