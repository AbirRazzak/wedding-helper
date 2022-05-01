from save_the_date.response import SaveTheDatePlusOne


class SaveTheDateResponseParser:
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
                    full_name=plus_one_entry
                    # TODO populate the age attribute if it exists
                )
            )

        return plus_ones

    def _split_by_delimiters(
        self,
        answer: str
    ) -> list[str]:
        delimiters = [',', '&', 'and']
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

