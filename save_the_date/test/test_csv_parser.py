from save_the_date.csv_parser import SaveTheDateResponsesParser
from save_the_date.question import SaveTheDateQuestions
from save_the_date.response import (
    SaveTheDateResponse,
    SaveTheDatePlusOne
)


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


def test_parse_plus_ones_answer_with_single_plus_one_and_no_age():
    answer = 'John Doe'
    expected_plus_one = SaveTheDatePlusOne(
        full_name=answer,
    )

    result = SaveTheDateResponsesParser.parse_plus_ones_answer(answer)

    assert result == [expected_plus_one]


def test_parse_plus_one_answer_with_single_unique_delimiter():
    p1 = 'Person 1'
    p2 = 'Person 2'
    p3 = 'Person 3'

    answer = f'{p1}, {p2}, {p3}'

    expected = [
        SaveTheDatePlusOne(full_name=p1),
        SaveTheDatePlusOne(full_name=p2),
        SaveTheDatePlusOne(full_name=p3)
    ]

    result = SaveTheDateResponsesParser.parse_plus_ones_answer(answer)

    assert result == expected


def test_parse_plus_one_answer_with_multiple_unique_delimiters():
    p1 = 'Person 1'
    p2 = 'Person 2'
    p3 = 'Person 3'

    answer = f'{p1}, {p2} and {p3}'

    expected = [
        SaveTheDatePlusOne(full_name=p1),
        SaveTheDatePlusOne(full_name=p2),
        SaveTheDatePlusOne(full_name=p3)
    ]

    result = SaveTheDateResponsesParser.parse_plus_ones_answer(answer)

    assert result == expected
