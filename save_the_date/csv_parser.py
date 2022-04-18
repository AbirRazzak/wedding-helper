from __future__ import annotations

import csv
import pathlib

import environs

from save_the_date import (
    ISaveTheDateResponsesParser
)
from save_the_date.response import SaveTheDateResponse


class SaveTheDateResponsesParser(ISaveTheDateResponsesParser):
    def __init__(
        self,
        responses: list[SaveTheDateResponse]
    ):
        self.responses = responses

    def get_names_of_responders(self):
        return [response.full_name for response in self.responses]

    @staticmethod
    def new(
        env: environs.Env
    ) -> SaveTheDateResponsesParser:
        responses = SaveTheDateResponsesParser._parse_csv_file_into_responses(
            csv_file_path=env.path('SAVE_THE_DATE_PLUS_ONE_CSV_FILE_PATH')
        )
        responses.extend(
            SaveTheDateResponsesParser._parse_csv_file_into_responses(
                csv_file_path=env.path('SAVE_THE_DATE_WITHOUT_PLUS_ONE_CSV_FILE_PATH')
            )
        )

        return SaveTheDateResponsesParser(
            responses=responses
        )

    @staticmethod
    def _parse_csv_data_into_response(
        data: dict[str, str]
    ) -> SaveTheDateResponse:
        return SaveTheDateResponse(
            full_name=data['What is your full name?'],
            email_address=data['What is your email address?']
        )

    @staticmethod
    def _parse_csv_file_into_responses(
        csv_file_path: pathlib.Path
    ) -> list[SaveTheDateResponse]:
        responses = []
        with open(file=csv_file_path, encoding='utf8') as data:
            for line in csv.DictReader(data):
                response = SaveTheDateResponsesParser._parse_csv_data_into_response(data=line)
                responses.append(response)

        return responses
