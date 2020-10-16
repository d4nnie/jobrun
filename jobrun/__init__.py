import os
import yaml

from .cli import *

__version__ = '1.0'

def read_yaml(path) -> dict:
    with open(path, 'r') as file:
        content = file.read()
    return yaml.safe_load(content)

class Runner:
    def __init__(self, yaml: dict):
        self.__yaml = yaml

    def __run_script(self, script: list):
        command = ' && '.join(script)
        os.system(command)

    def before_script(self):
        before_script = self.__yaml['before_script']
        self.__run_script(before_script)

    def job(self, name: str):
        script = self.__yaml[name]['script']
        self.__run_script(script)
