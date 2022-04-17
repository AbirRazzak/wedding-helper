from __future__ import annotations

import abc

import pydantic


class ISaveTheDateResponsesParser(abc.ABC):
    def get_names_of_responders(self) -> set[str]:
        pass


class SaveTheDateResponse(pydantic.BaseModel):
    full_name: str
    email_address: str
