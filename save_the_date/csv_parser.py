from __future__ import annotations

import csv
import pathlib

import environs

from save_the_date import (
    ISaveTheDateResponsesParser
)
from save_the_date.question import SaveTheDateQuestions
from save_the_date.response import (
    SaveTheDateResponse
)
from save_the_date.response_parser import SaveTheDateResponseParser


class SaveTheDateCSVParser(ISaveTheDateResponsesParser):
    def __init__(
        self,
        responses: list[SaveTheDateResponse],
        parser: SaveTheDateResponseParser
    ):
        self.responses = responses
        self.parser = parser

    def get_responses(
        self
    ):
        return self.responses

    # TODO: I want to get rid of this method in favor of the one above.
    def get_names_of_responders(
        self
    ):
        return [response.full_name for response in self.responses]

    @staticmethod
    def new(
        env: environs.Env
    ) -> SaveTheDateCSVParser:
        csv_parser = SaveTheDateCSVParser(
            responses=[],
            parser=SaveTheDateResponseParser()
        )

        responses = csv_parser._parse_csv_file_into_responses(
            csv_file_path=env.path('SAVE_THE_DATE_PLUS_ONE_CSV_FILE_PATH')
        )
        responses.extend(
            csv_parser._parse_csv_file_into_responses(
                csv_file_path=env.path('SAVE_THE_DATE_WITHOUT_PLUS_ONE_CSV_FILE_PATH')
            )
        )

        csv_parser.responses = responses

        return csv_parser

    def parse_data_into_response(
        self,
        data: dict[str, str]
    ) -> SaveTheDateResponse:
        return SaveTheDateResponse(
            full_name=self.parser.parse_full_name_response(data[SaveTheDateQuestions.full_name.value]),
            email_address=data[SaveTheDateQuestions.email_address.value],
            plus_ones=self.parser.parse_plus_ones_response(
                # In one of the CSV files, this column does not exist. In that case, we return an empty list.
                data.get(SaveTheDateQuestions.plus_ones.value, '')
            ),
            is_hotel_needed=self.parser.handle_boolean_question_answer(
                data[SaveTheDateQuestions.hotel_needed.value]
            ),
            is_vaccinated=self.parser.handle_boolean_question_answer(
                data[SaveTheDateQuestions.vaccinated.value]
            ),
        )

    def _parse_csv_file_into_responses(
        self,
        csv_file_path: pathlib.Path
    ) -> list[SaveTheDateResponse]:
        responses = []
        with open(file=csv_file_path, encoding='utf8') as data:
            for line in csv.DictReader(data):
                response = self.parse_data_into_response(data=line)
                responses.append(response)

        return responses
