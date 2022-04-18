from __future__ import annotations

import abc


class ISaveTheDateResponsesParser(abc.ABC):
    def get_names_of_responders(self) -> list[str]:
        pass
