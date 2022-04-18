import csv


def get_names_of_everyone_on_the_list(csv_file) -> list[str]:
    """
    Returns a list of all names on the list.
    """
    with open(csv_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        return [row[0] for row in reader]
