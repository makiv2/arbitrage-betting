import yaml

from util.path.path import get_abs_path


def get_config():
    with open(get_abs_path("config.yaml"), 'r') as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            print(e)
    return config
