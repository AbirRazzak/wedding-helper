from save_the_date import (
    SaveTheDateResponse,
    ISaveTheDateResponsesParser
)
from save_the_date.question import SaveTheDateQuestions
from save_the_date.response import SaveTheDatePlusOne


class SaveTheDateResponseParser(ISaveTheDateResponsesParser):

    def parse_data_into_response(
        self,
        data: dict[str, str]
    ) -> SaveTheDateResponse:
        return SaveTheDateResponse(
            full_name=self.parse_full_name_response(data[SaveTheDateQuestions.full_name.value]),
            email_address=data[SaveTheDateQuestions.email_address.value],
            plus_ones=self.parse_plus_ones_response(
                # In one of the CSV files, this column does not exist. In that case, we return an empty list.
                data.get(SaveTheDateQuestions.plus_ones.value, '')
            ),
            is_hotel_needed=self.handle_boolean_question_answer(
                data[SaveTheDateQuestions.hotel_needed.value]
            ),
            is_vaccinated=self.handle_boolean_question_answer(
                data[SaveTheDateQuestions.vaccinated.value]
            ),
        )

    def parse_full_name_response(
        self,
        response: str
    ) -> str:
        name = response.strip()
        name = name.replace('  ', ' ')
        name = name.title()
        return name

    def handle_boolean_question_answer(
        self,
        answer: str
    ) -> bool:
        return answer.upper() == 'YES'

    def parse_plus_ones_response(
        self,
        response: str
    ) -> list[SaveTheDatePlusOne]:
        if response == '':
            return []

        plus_ones: list[SaveTheDatePlusOne] = []

        plus_ones_entries = self._split_by_delimiters(response)

        for plus_one_entry in plus_ones_entries:
            # TODO - parse plus one entry to get name and age
            plus_ones.append(
                SaveTheDatePlusOne(
                    full_name=self.parse_full_name_response(plus_one_entry)
                    # TODO populate the age attribute if it exists
                )
            )

        return plus_ones

    def _split_by_delimiters(
        self,
        answer: str
    ) -> list[str]:
        delimiters = [',', '&', ' and ', '\n']
        splits: list[str] = [answer]

        for delimiter in delimiters:
            for split in list(splits):
                splits.remove(split)
                splits.extend(
                    self._split_answer_based_off_delimiter(
                        answer=split,
                        delimiter=delimiter
                    )
                )

        return splits

    def _split_answer_based_off_delimiter(
        self,
        answer: str,
        delimiter: str
    ) -> list[str]:
        return [
            plus_one_name.strip()
            for plus_one_name in answer.split(delimiter)
        ]

