import environs


def setup_environment() -> environs.Env:
    _env = environs.Env()
    _env.read_env()

    return _env


if __name__ == '__main__':
    env = setup_environment()
    print('Hello World!')
