from pprint import pprint

import environs

from master_list.csv_parser import get_names_of_everyone_on_the_list
from save_the_date.csv_parser import SaveTheDateResponsesParser


def setup_environment() -> environs.Env:
    env = environs.Env()
    env.read_env()

    return env


if __name__ == '__main__':
    env = setup_environment()
    save_the_date_parser = SaveTheDateResponsesParser.new(env)
    # pprint(sorted(save_the_date_parser.get_names_of_responders()))

    everyone_on_notion = get_names_of_everyone_on_the_list(env.path('NOTION_CSV_FILE_PATH'))

    filter_set = set(save_the_date_parser.get_names_of_responders())

    c = [x for x in everyone_on_notion if x not in filter_set]

    pprint(sorted(c))
