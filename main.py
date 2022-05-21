import environs

from save_the_date.repo import SaveTheDateResponseRepo
from save_the_date.response_parser import SaveTheDateResponseParser
from withjoy.converter import WithjoyConverter
from withjoy.exporter import WithjoyCSVExporter


def setup_environment() -> environs.Env:
    _env = environs.Env()
    _env.read_env()

    return _env


if __name__ == '__main__':
    env = setup_environment()
    print('Hello World!')
    save_the_date_response_repo = SaveTheDateResponseRepo.new(
        env=env,
        parser=SaveTheDateResponseParser()
    )
    withjoy_guest_list = WithjoyConverter().convert_save_the_date_repo_into_withjoy_guest_list(
        save_the_date_repo=save_the_date_response_repo
    )
    print(withjoy_guest_list)
    WithjoyCSVExporter().export_withjoy_guest_list_to_csv_file(
        withjoy_guest_list=withjoy_guest_list,
        csv_file_path=env.path('WITHJOY_GUEST_LIST_CSV_FILE_PATH')
    )
