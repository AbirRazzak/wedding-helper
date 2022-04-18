from save_the_date.csv_parser import SaveTheDateResponsesParser
from save_the_date.response import SaveTheDateResponse


def test_parse_csv_data_into_response():
    name = 'John'
    email_address = 'abc123@gmail.com'

    raw_data = {
        'What is your full name?': name,
        'What is your email address?': email_address
    }

    expected_response = SaveTheDateResponse(
        full_name=name,
        email_address=email_address
    )

    result = SaveTheDateResponsesParser._parse_csv_data_into_response(raw_data)

    assert result == expected_response
