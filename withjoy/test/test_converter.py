from save_the_date import SaveTheDateResponse
from save_the_date.repo import SaveTheDateResponseRepo
from withjoy.converter import WithjoyConverter
from withjoy.guest_list import (
    WithjoyGuestList,
    WithjoyGuest
)


def test_convert_save_the_dates():
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
                email='foo@bar.com',
                party=''
            )
        ]
    )

    converter = WithjoyConverter()
    result = converter.convert_save_the_dates_into_withjoy_guest_list(
        save_the_date_repo=save_the_date_repo
    )

    assert result == expected
