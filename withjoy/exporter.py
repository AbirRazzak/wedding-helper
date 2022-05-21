import csv

from withjoy.guest_list import (
    WithjoyGuestList,
    WithjoyGuest
)


class WithjoyCSVExporter:
    def export_withjoy_guest_list_to_csv_file(
        self,
        withjoy_guest_list: WithjoyGuestList,
        csv_file_path: str
    ):
        rows_to_write = self.export_withjoy_guest_list(withjoy_guest_list)
        with open(csv_file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows_to_write)

    def export_withjoy_guest_list(
        self,
        withjoy_guest_list: WithjoyGuestList
    ) -> list[list[str]]:
        header = ['first name', 'last name', 'email', 'party']
        row_list = [header]
        for withjoy_guest in withjoy_guest_list.guests:
            row_list.append(self.export_withjoy_guest(withjoy_guest))

        return row_list

    def export_withjoy_guest(
        self,
        withjoy_guest: WithjoyGuest
    ) -> list[str]:

        return [
            withjoy_guest.name,
            '',  # ignore last name for now
            withjoy_guest.email,
            withjoy_guest.party
        ]
