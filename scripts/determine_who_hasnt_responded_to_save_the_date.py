from pprint import pprint

from main import setup_environment
from master_list.csv_parser import get_names_of_everyone_on_the_list
from save_the_date.csv_parser import SaveTheDateCSVParser

if __name__ == '__main__':
    env = setup_environment()

    save_the_date_parser = SaveTheDateCSVParser.new(env)
    save_the_date_responses = save_the_date_parser.get_responses()
    save_the_date_responders = {response.full_name for response in save_the_date_responses}
    print('The following people have responded to the save the date:')
    pprint(sorted(save_the_date_responders))

    everyone_on_notion = get_names_of_everyone_on_the_list(env.path('NOTION_CSV_FILE_PATH'))
    people_to_ignore = env.list('DECLINED_GUESTS', delimiter=', ')
    people_to_look_for = [name for name in everyone_on_notion if name not in people_to_ignore]

    people_who_have_not_responded = [x for x in people_to_look_for if x not in save_the_date_responders]
    print('The following people have not responded to the save the date:')
    pprint(sorted(people_who_have_not_responded))

    extra_people_not_on_notion = sorted([x for x in save_the_date_responders if x not in people_to_look_for])
    if extra_people_not_on_notion:
        print('The following people have responded to the save the date, but are not on the notion list:')
        pprint(extra_people_not_on_notion)
