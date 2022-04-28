from pprint import pprint

import environs

from save_the_date.csv_parser import SaveTheDateCSVParser


def setup_environment() -> environs.Env:
    env = environs.Env()
    env.read_env()

    return env


if __name__ == '__main__':
    env = setup_environment()
    save_the_date_parser = SaveTheDateCSVParser.new(env)
    pprint(sorted(save_the_date_parser.get_names_of_responders()))
