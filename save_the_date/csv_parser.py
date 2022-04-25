from __future__ import annotations

import csv
import pathlib

import environs

from save_the_date import (
    ISaveTheDateResponsesParser
)
from save_the_date.question import SaveTheDateQuestions
from save_the_date.response import (
    SaveTheDateResponse,
    SaveTheDatePlusOne
)


class SaveTheDateResponsesParser(ISaveTheDateResponsesParser):
    def __init__(
        self,
        responses: list[SaveTheDateResponse]
    ):
        self.responses = responses

    def get_responses(self):
        return self.responses

    # TODO: I want to get rid of this method in favor of the one above.
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
    def _handle_boolean_question_answer(
        answer: str
    ) -> bool:
        return answer.upper() == 'YES'

    @staticmethod
    def _split_answer_based_off_delimiter(
        answer: str,
        delimiter: str
    ) -> list[str]:
        return [
            plus_one_name.strip()
            for plus_one_name in answer.split(delimiter)
        ]

    @staticmethod
    def _determine_delimiter_and_split(
        answer: str
    ) -> list[str]:
        if ',' in answer:
            return SaveTheDateResponsesParser._split_answer_based_off_delimiter(
                answer=answer,
                delimiter=','
            )
        elif '&' in answer:
            return SaveTheDateResponsesParser._split_answer_based_off_delimiter(
                answer=answer,
                delimiter='&'
            )
        elif 'and' in answer:
            return SaveTheDateResponsesParser._split_answer_based_off_delimiter(
                answer=answer,
                delimiter='and'
            )
        else:
            return [answer]

    @staticmethod
    def _parse_plus_ones_answer(
        answer: str
    ) -> list[SaveTheDatePlusOne]:
        if answer == '':
            return []

        plus_ones: list[SaveTheDatePlusOne] = []

        plus_ones_entries = SaveTheDateResponsesParser._determine_delimiter_and_split(answer)

        for plus_one_entry in plus_ones_entries:
            plus_ones.append(
                SaveTheDatePlusOne(
                    full_name=plus_one_entry
                    # TODO populate the age attribute if it exists
                )
            )

        return plus_ones

    @staticmethod
    def _parse_csv_data_into_response(
        data: dict[str, str]
    ) -> SaveTheDateResponse:
        return SaveTheDateResponse(
            full_name=data[SaveTheDateQuestions.full_name.value],
            email_address=data[SaveTheDateQuestions.email_address.value],
            plus_ones=SaveTheDateResponsesParser._parse_plus_ones_answer(
                # In one of the CSV files, this column does not exist. In that case, we return an empty list.
                data.get(SaveTheDateQuestions.plus_ones.value, '')
            ),
            is_hotel_needed=SaveTheDateResponsesParser._handle_boolean_question_answer(data[SaveTheDateQuestions.hotel_needed.value]),
            is_vaccinated=SaveTheDateResponsesParser._handle_boolean_question_answer(data[SaveTheDateQuestions.vaccinated.value]),
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
