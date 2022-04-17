from __future__ import annotations

import abc
import csv
import pathlib

import environs
import pydantic


class SaveTheDateResponse(pydantic.BaseModel):
    full_name: str
    email_address: str


class ISaveTheDateResponsesParser(abc.ABC):
    def get_names_of_responders(self) -> set[str]:
        pass


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
        csv_file_path: pathlib.Path = env.path('SAVE_THE_DATE_PLUS_ONE_CSV_FILE_PATH')
        responses = SaveTheDateResponsesParser._parse_csv_file_into_responses(
            csv_file_path
        )

        return SaveTheDateResponsesParser(
            responses=responses
        )

    @staticmethod
    def _parse_csv_file_into_responses(
        csv_file_path: pathlib.Path
    ) -> list[SaveTheDateResponse]:
        responses = []
        with open(file=csv_file_path, encoding='utf8') as data:
            for line in csv.DictReader(data):
                response = SaveTheDateResponse(
                    full_name=line['What is your full name?'],
                    email_address=line['What is your email address?']
                )
                responses.append(response)

        return responses
