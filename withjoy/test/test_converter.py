from save_the_date import SaveTheDateResponse
from save_the_date.repo import SaveTheDateResponseRepo
from save_the_date.response import SaveTheDatePlusOne
from withjoy.converter import WithjoyConverter
from withjoy.guest_list import (
    WithjoyGuestList,
    WithjoyGuest
)
from withjoy.party_name_generator import PartyNameGenerator


def test_convert_save_the_date_repo():
    first_name = 'Foo'
    last_name = 'Bar'
    name = f'{first_name} {last_name}'
    email = 'foo@bar.com'

    save_the_date_repo = SaveTheDateResponseRepo(
        responses=[
            SaveTheDateResponse(
                full_name=name,
                email_address=email,
                is_hotel_needed=False,
                is_vaccinated=False
            )
        ]
    )

    expected = WithjoyGuestList(
        guests=[
            WithjoyGuest(
                first_name=first_name,
                last_name=last_name,
                email=email
            )
        ]
    )

    converter = WithjoyConverter()
    result = converter.convert_save_the_date_repo_into_withjoy_guest_list(
        save_the_date_repo=save_the_date_repo
    )

    assert result == expected


def test_convert_save_the_date_repo_with_plus_ones():
    first_name = 'Foo'
    last_name = 'Bar'
    name = f'{first_name} {last_name}'
    email = 'foo@bar.com'
    plus_one_first_name = 'Foo Bar Plus'
    plus_one_last_name = 'One'
    plus_one_name = f'{plus_one_first_name} {plus_one_last_name}'
    party = 'foo-bar'

    save_the_date_repo = SaveTheDateResponseRepo(
        responses=[
            SaveTheDateResponse(
                full_name=name,
                email_address=email,
                plus_ones=[
                    SaveTheDatePlusOne(
                        full_name=plus_one_name,
                    )
                ],
                is_hotel_needed=False,
                is_vaccinated=False
            )
        ]
    )

    expected = WithjoyGuestList(
        guests=[
            WithjoyGuest(
                first_name=first_name,
                last_name=last_name,
                email=email,
                party=party
            ),
            WithjoyGuest(
                first_name=plus_one_first_name,
                last_name=plus_one_last_name,
                party=party
            )
        ]
    )

    converter = WithjoyConverter()
    result = converter.convert_save_the_date_repo_into_withjoy_guest_list(
        save_the_date_repo=save_the_date_repo
    )

    assert result == expected


def test_convert_save_the_date_response():
    first_name = 'Foo'
    last_name = 'Bar'
    name = f'{first_name} {last_name}'
    email = 'foo@bar.com'

    response = SaveTheDateResponse(
        full_name=name,
        email_address=email,
        is_vaccinated=True,
        is_hotel_needed=True
    )

    expected = [
        WithjoyGuest(
            first_name=first_name,
            last_name=last_name,
            email=email
        )
    ]

    result = WithjoyConverter().convert_save_the_date_response_to_withjoy_guests(
        save_the_date_response=response
    )

    assert result == expected


def test_convert_save_the_date_response_with_no_last_name():
    # This test case is because some placeholder values are in the Google forms that didn't include a last name
    name = 'Foo'
    email = 'foo@bar.com'

    response = SaveTheDateResponse(
        full_name=name,
        email_address=email,
        is_vaccinated=True,
        is_hotel_needed=True
    )

    expected = [
        WithjoyGuest(
            first_name=name,
            last_name='',
            email=email
        )
    ]

    result = WithjoyConverter().convert_save_the_date_response_to_withjoy_guests(
        save_the_date_response=response
    )

    assert result == expected


def test_convert_save_the_date_response_with_plus_ones():
    first_name = 'Foo'
    last_name = 'Bar'
    name = f'{first_name} {last_name}'
    email = 'foo@bar.com'
    plus_one_first_name = 'Foo'
    plus_one_last_name = 'Bar'
    plus_one_name = f'{plus_one_first_name} {plus_one_last_name}'

    party_name_gen = PartyNameGenerator()

    plus_one = SaveTheDatePlusOne(
        full_name=plus_one_name
    )
    response = SaveTheDateResponse(
        full_name=name,
        email_address=email,
        plus_ones=[plus_one],
        is_vaccinated=True,
        is_hotel_needed=True
    )

    party = party_name_gen.generate_party_name(
        save_the_date_response=response
    )

    expected = [
        WithjoyGuest(
            first_name=first_name,
            last_name=last_name,
            email=email,
            party=party
        ),
        WithjoyGuest(
            first_name=plus_one_first_name,
            last_name=plus_one_last_name,
            party=party
        )
    ]

    result = WithjoyConverter().convert_save_the_date_response_to_withjoy_guests(
        save_the_date_response=response
    )

    assert result == expected
