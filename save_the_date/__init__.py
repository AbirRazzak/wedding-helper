from __future__ import annotations

import abc

from save_the_date.response import SaveTheDateResponse


class ISaveTheDateResponsesParser(abc.ABC):
    @abc.abstractmethod
    def parse_data_into_response(
        self,
        data: dict[str, str]
    ) -> SaveTheDateResponse:
        pass

    @abc.abstractmethod
    def get_responses(self) -> list[SaveTheDateResponse]:
        pass

    @abc.abstractmethod
    def get_names_of_responders(self) -> list[str]:
        pass
