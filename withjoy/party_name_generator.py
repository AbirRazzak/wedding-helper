from save_the_date import SaveTheDateResponse


class PartyNameGenerator:
    def generate_party_name(
        self,
        save_the_date_response: SaveTheDateResponse
    ) -> str:
        if save_the_date_response.plus_ones:
            return save_the_date_response.full_name.lower().replace(' ', '-')

        return ''
