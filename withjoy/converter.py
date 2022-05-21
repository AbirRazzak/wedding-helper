from save_the_date import SaveTheDateResponse
from save_the_date.repo import ISaveTheDateResponseRepo
from withjoy.guest_list import (
    WithjoyGuestList,
    WithjoyGuest
)
from withjoy.party_name_generator import PartyNameGenerator


class WithjoyConverter:
    def __init__(
        self,
        party_name_generator: PartyNameGenerator = None
    ):
        if party_name_generator is None:
            party_name_generator = PartyNameGenerator()

        self.party_name_generator = party_name_generator

    def convert_save_the_date_response_full_name_to_withjoy_guest_name(
        self,
        save_the_date_response_full_name: str
    ) -> str:
        '''
        Perform transformations on the full name to make it suitable for Withjoy.
        Withjoy does not allow special characters in the guest name.
        '''
        # TODO placing this hack in for now in the meantime while fixing some responses
        return save_the_date_response_full_name.replace(' & ', ' and ').replace(' and ', ' n ')

    def convert_save_the_date_response_to_withjoy_guests(
        self,
        save_the_date_response: SaveTheDateResponse
    ) -> list[WithjoyGuest]:
        guests: list[WithjoyGuest] = []
        party = self.party_name_generator.generate_party_name(
            save_the_date_response=save_the_date_response
        )

        main_contact = WithjoyGuest(
            name=self.convert_save_the_date_response_full_name_to_withjoy_guest_name(save_the_date_response.full_name),
            email=save_the_date_response.email_address,
            party=party
        )
        guests.append(main_contact)

        for plus_one in save_the_date_response.plus_ones:
            extra_guest = WithjoyGuest(
                name=self.convert_save_the_date_response_full_name_to_withjoy_guest_name(plus_one.full_name),
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
