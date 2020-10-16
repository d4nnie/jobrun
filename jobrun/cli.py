import os
import argparse

from yaml import safe_load

import jobrun

__SUCCESSCODE = 0
__FAILCODE = 2

def __version():
    return '%(prog)s {}'.format(jobrun.__version__)

def __parse():
    parser = argparse.ArgumentParser(
        prog='jobrun',
        description='Utility for running ' \
                    'gitlab-ci jobs on local ' \
                    'machine',
        allow_abbrev=False,
        add_help=False
    )

    parser.add_argument(
        '-h', '--help',
        action='help',
        default=argparse.SUPPRESS,
        help='Show this help' \
             'message and exit'
    )
    parser.add_argument(
        '-v', '--version',
        action='version',
        version=__version(),
        help='Show version'
    )
    parser.add_argument(
        '-p', '--path',
        action='store',
        help='Put yaml file'
    )
    parser.add_argument(
        '-b', '--before-script',
        action='store_true',
        help='Run before_script'
    )
    parser.add_argument(
        '-j', '--job',
        action='store',
        help='Put ant run job'
    )

    return parser.parse_args()


def main():
    args = __parse()

    yaml = None
    if args.path is not None:
        with open(args.path) as file:
            yaml = file.read()
        yaml = safe_load(yaml)
    elif os.path.exists('.gitlab-ci.yml'):
        args.path = '.gitlab-ci.yml'
        with open(args.path) as file:
            yaml = file.read()
        yaml = safe_load(yaml)

    runner = jobrun.Runner(yaml)
    if args.before_script:
        if args.path is None:
            return __FAILCODE
        runner.before_script()
    if args.job is not None:
        if args.path is None:
            return __FAILCODE
        runner.job(args.job)

    return __SUCCESSCODE
