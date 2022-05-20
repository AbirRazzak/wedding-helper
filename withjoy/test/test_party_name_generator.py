from save_the_date import SaveTheDateResponse
from save_the_date.response import SaveTheDatePlusOne
from withjoy.party_name_generator import PartyNameGenerator


def test_generate_party_name_with_plus_ones():
    response = SaveTheDateResponse(
        full_name='Foo Bar',
        email_address='',
        plus_ones=[
            SaveTheDatePlusOne(
                full_name='Plus One'
            )
        ],
        is_vaccinated=True,
        is_hotel_needed=True
    )

    expected = 'foo-bar'

    result = PartyNameGenerator().generate_party_name(
        save_the_date_response=response
    )

    assert result == expected


def test_generate_party_name_without_plus_ones():
    response = SaveTheDateResponse(
        full_name='Foo Bar',
        email_address='',
        is_vaccinated=True,
        is_hotel_needed=True
    )

    expected = ''

    result = PartyNameGenerator().generate_party_name(
        save_the_date_response=response
    )

    assert result == expected

