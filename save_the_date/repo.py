from __future__ import annotations

import abc
import csv
import pathlib

import environs

from save_the_date import (
    SaveTheDateResponse,
    ISaveTheDateResponsesParser
)


class ISaveTheDateResponseRepo(abc.ABC):
    @abc.abstractmethod
    def get_all_responses(
        self
    ) -> list[SaveTheDateResponse]:
        pass


class SaveTheDateResponseRepo(ISaveTheDateResponseRepo):
    def __init__(
        self,
        responses: list[SaveTheDateResponse] = None
    ):
        self._responses = responses

    def get_all_responses(
        self
    ) -> list[SaveTheDateResponse]:
        return [value for key, value in self._responses]

    def add_response(
        self,
        response: SaveTheDateResponse
    ):
        self._responses.append(response)

    @staticmethod
    def new(
        env: environs.Env,
        parser: ISaveTheDateResponsesParser
    ) -> SaveTheDateResponseRepo:
        repo = SaveTheDateResponseRepo()

        repo._parse_csv_file_into_responses(
            csv_file_path=env.path('SAVE_THE_DATE_PLUS_ONE_CSV_FILE_PATH'),
            parser=parser
        )
        repo._parse_csv_file_into_responses(
            csv_file_path=env.path('SAVE_THE_DATE_WITHOUT_PLUS_ONE_CSV_FILE_PATH'),
            parser=parser
        )

        return repo

    def _parse_csv_file_into_responses(
        self,
        csv_file_path: pathlib.Path,
        parser: ISaveTheDateResponsesParser
    ):
        with open(file=csv_file_path, encoding='utf8') as data:
            for line in csv.DictReader(data):
                response = parser.parse_data_into_response(data=line)
                self.add_response(response=response)
