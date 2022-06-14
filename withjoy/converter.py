from pydantic import BaseModel

from save_the_date import SaveTheDateResponse
from save_the_date.repo import ISaveTheDateResponseRepo
from withjoy.guest_list import (
    WithjoyGuestList,
    WithjoyGuest
)
from withjoy.party_name_generator import PartyNameGenerator


class ConvertedFullName(BaseModel):
    first_name: str
    last_name: str


class WithjoyConverter:
    def __init__(
        self,
        party_name_generator: PartyNameGenerator = None
    ):
        if party_name_generator is None:
            party_name_generator = PartyNameGenerator()

        self.party_name_generator = party_name_generator

    def convert_save_the_date_response_full_name_to_withjoy_guest_names(
        self,
        save_the_date_response_full_name: str
    ) -> ConvertedFullName:
        '''
        Perform transformations on the full name to make it suitable for Withjoy.
        Withjoy does not allow special characters in the guest name.
        '''
        # TODO placing this hack in for now in the meantime while fixing some responses
        full_name = save_the_date_response_full_name.replace(' & ', ' and ').replace(' and ', ' n ')

        first_name_and_last_name = full_name.rsplit(' ', 1)
        first_name = first_name_and_last_name[0]
        last_name = first_name_and_last_name[1] if len(first_name_and_last_name) > 1 else ''

        return ConvertedFullName(
            first_name=first_name,
            last_name=last_name
        )

    def convert_save_the_date_response_to_withjoy_guests(
        self,
        save_the_date_response: SaveTheDateResponse
    ) -> list[WithjoyGuest]:
        guests: list[WithjoyGuest] = []
        party = self.party_name_generator.generate_party_name(
            save_the_date_response=save_the_date_response
        )

        converted_name = self.convert_save_the_date_response_full_name_to_withjoy_guest_names(save_the_date_response.full_name)
        main_contact = WithjoyGuest(
            first_name=converted_name.first_name,
            last_name=converted_name.last_name,
            email=save_the_date_response.email_address,
            party=party
        )
        guests.append(main_contact)

        for plus_one in save_the_date_response.plus_ones:
            converted_name = self.convert_save_the_date_response_full_name_to_withjoy_guest_names(plus_one.full_name)
            extra_guest = WithjoyGuest(
                first_name=converted_name.first_name,
                last_name=converted_name.last_name,
                party=party
            )
            guests.append(extra_guest)

        return guests

    def convert_save_the_date_repo_into_withjoy_guest_list(
        self,
        save_the_date_repo: ISaveTheDateResponseRepo
    ) -> WithjoyGuestList:
        save_the_date_responses = save_the_date_repo.get_all_responses()

        guests: list[WithjoyGuest] = []
        for resp in save_the_date_responses:
            guests.extend(
                self.convert_save_the_date_response_to_withjoy_guests(
                    save_the_date_response=resp
                )
            )

        return WithjoyGuestList(
            guests=guests
        )
