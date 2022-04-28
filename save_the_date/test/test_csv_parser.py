from save_the_date.csv_parser import SaveTheDateCSVParser
from save_the_date.question import SaveTheDateQuestions
from save_the_date.response import (
    SaveTheDateResponse
)
from save_the_date.response_parser import SaveTheDateResponseParser


def test_parse_csv_data_into_response():
    name = 'John'
    email_address = 'abc123@gmail.com'

    raw_data = {
        SaveTheDateQuestions.full_name.value: name,
        SaveTheDateQuestions.email_address.value: email_address,
        SaveTheDateQuestions.hotel_needed.value: 'Yes',
        SaveTheDateQuestions.vaccinated.value: 'Yes'
    }

    expected_response = SaveTheDateResponse(
        full_name=name,
        email_address=email_address,
        is_hotel_needed=True,
        is_vaccinated=True
    )

    csv_parser = SaveTheDateCSVParser(responses=[], parser=SaveTheDateResponseParser())
    result = csv_parser.parse_csv_data_into_response(raw_data)

    assert result == expected_response
