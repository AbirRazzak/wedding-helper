from save_the_date.csv_parser import SaveTheDateResponsesParser
from save_the_date.question import SaveTheDateQuestions
from save_the_date.response import SaveTheDateResponse


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

    result = SaveTheDateResponsesParser._parse_csv_data_into_response(raw_data)

    assert result == expected_response
