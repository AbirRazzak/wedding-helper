from save_the_date.response import SaveTheDatePlusOne
from save_the_date.response_parser import SaveTheDateResponseParser


def test_parse_full_name_response_removes_leading_and_trailing_whitespace():
    response = '   John Doe  '
    expected = 'John Doe'

    parser = SaveTheDateResponseParser()
    result = parser.parse_full_name_response(response)

    assert result == expected


def test_parse_full_name_response_removes_double_whitespaces():
    response = 'John  Doe'
    expected = 'John Doe'

    parser = SaveTheDateResponseParser()
    result = parser.parse_full_name_response(response)

    assert result == expected


def test_parse_plus_ones_answer_with_single_plus_one_and_no_age():
    answer = 'John Doe'
    expected_plus_one = SaveTheDatePlusOne(
        full_name=answer,
    )

    parser = SaveTheDateResponseParser()
    result = parser.parse_plus_ones_response(answer)

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

    parser = SaveTheDateResponseParser()
    result = parser.parse_plus_ones_response(answer)

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

    parser = SaveTheDateResponseParser()
    result = parser.parse_plus_ones_response(answer)

    assert result == expected
