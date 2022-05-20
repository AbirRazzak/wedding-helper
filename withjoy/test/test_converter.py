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
    save_the_date_repo = SaveTheDateResponseRepo(
        responses=[
            SaveTheDateResponse(
                full_name='Foo Bar',
                email_address='foo@bar.com',
                is_hotel_needed=False,
                is_vaccinated=False
            )
        ]
    )

    expected = WithjoyGuestList(
        guests=[
            WithjoyGuest(
                name='Foo Bar',
                email='foo@bar.com'
            )
        ]
    )

    converter = WithjoyConverter()
    result = converter.convert_save_the_date_repo_into_withjoy_guest_list(
        save_the_date_repo=save_the_date_repo
    )

    assert result == expected


def test_convert_save_the_date_repo_with_plus_ones():
    save_the_date_repo = SaveTheDateResponseRepo(
        responses=[
            SaveTheDateResponse(
                full_name='Foo Bar',
                email_address='foo@bar.com',
                plus_ones=[
                    SaveTheDatePlusOne(
                        full_name='Foo Bar Plus One',
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
                name='Foo Bar',
                email='foo@bar.com',
                party='foo-bar'
            ),
            WithjoyGuest(
                name='Foo Bar Plus One',
                party='foo-bar'
            )
        ]
    )

    converter = WithjoyConverter()
    result = converter.convert_save_the_date_repo_into_withjoy_guest_list(
        save_the_date_repo=save_the_date_repo
    )

    assert result == expected


def test_convert_save_the_date_response():
    name = 'Foo Bar'
    email = 'foo@bar.com'

    response = SaveTheDateResponse(
        full_name=name,
        email_address=email,
        is_vaccinated=True,
        is_hotel_needed=True
    )

    expected = [
        WithjoyGuest(
            name=name,
            email=email
        )
    ]

    result = WithjoyConverter().convert_save_the_date_response_to_withjoy_guests(
        save_the_date_response=response
    )

    assert result == expected


def test_convert_save_the_date_response_with_plus_ones():
    name = 'Foo Bar'
    email = 'foo@bar.com'
    plus_one_name = 'Plus One'

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
            name=name,
            email=email,
            party=party
        ),
        WithjoyGuest(
            name=plus_one_name,
            party=party
        )
    ]

    result = WithjoyConverter().convert_save_the_date_response_to_withjoy_guests(
        save_the_date_response=response
    )

    assert result == expected
