from pprint import pprint

from main import setup_environment
from master_list.csv_parser import get_names_of_everyone_on_the_list
from save_the_date.csv_parser import SaveTheDateCSVParser

if __name__ == '__main__':
    env = setup_environment()
    save_the_date_parser = SaveTheDateCSVParser.new(env)
    print('The following people have responded to the save the date:')
    pprint(sorted(save_the_date_parser.get_names_of_responders()))

    everyone_on_notion = get_names_of_everyone_on_the_list(env.path('NOTION_CSV_FILE_PATH'))

    filter_set = set(save_the_date_parser.get_names_of_responders())

    people_who_have_not_responded = [x for x in everyone_on_notion if x not in filter_set]

    print('The following people have not responded to the save the date:')
    pprint(sorted(people_who_have_not_responded))
