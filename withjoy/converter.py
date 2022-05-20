from save_the_date.repo import ISaveTheDateResponseRepo
from withjoy.guest_list import (
    WithjoyGuestList,
    WithjoyGuest
)


class WithjoyConverter:
    def convert_save_the_dates_into_withjoy_guest_list(
        self,
        save_the_date_repo: ISaveTheDateResponseRepo
    ) -> WithjoyGuestList:
        save_the_date_responses = save_the_date_repo.get_all_responses()

        guests: list[WithjoyGuest] = []
        for resp in save_the_date_responses:
            guests.append(
                WithjoyGuest(
                    name=resp.full_name,
                    email=resp.email_address,
                    party=''
                )
            )

        return WithjoyGuestList(
            guests=guests
        )
