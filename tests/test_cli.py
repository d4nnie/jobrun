import os
import sys
import shutil
import pytest

import jobrun

__FAILCODE = 2

def check_args(args=[]):
    sys.argv = ['jobrun'] + args
    with pytest.raises(SystemExit) as wrapped_exit:
        jobrun.main()
    return wrapped_exit.value.code

def test_no_args():
    sys.argv = ['jobrun']
    assert jobrun.main() != __FAILCODE

def test_arg_path():
    sys.argv = ['jobrun', '-p',
                'example.yml']
    assert jobrun.main() != __FAILCODE

    sys.argv = ['jobrun', '--path',
                'example.yml']
    assert jobrun.main() != __FAILCODE

def test_arg_help():
    assert check_args(['-h']) != __FAILCODE
    assert check_args(['--help']) != __FAILCODE

def test_arg_version():
    assert check_args(['-v']) != __FAILCODE
    assert check_args(['--version']) != __FAILCODE

def test_arg_before_script():
    sys.argv = ['jobrun', '-p',
                'example.yml', '-b']
    assert jobrun.main() != __FAILCODE
    assert os.path.exists('file')
    os.remove('file')

    while os.path.exists('file'):
        continue

    sys.argv = ['jobrun', '-p',
                'example.yml',
                '--before-script']
    assert jobrun.main() != __FAILCODE
    assert os.path.exists('file')
    os.remove('file')

def test_arg_job():
    sys.argv = ['jobrun', '-p',
                'example.yml', '-j',
                'run.example']
    assert jobrun.main() != __FAILCODE
    assert os.path.exists('folder')
    assert os.path.exists('folder/file_in_folder')
    shutil.rmtree('folder')

    while os.path.exists('folder'):
        continue

    sys.argv = ['jobrun', '-p',
                'example.yml', '--job',
                'run.example']
    assert jobrun.main() != __FAILCODE
    assert os.path.exists('folder')
    assert os.path.exists('folder/file_in_folder')
    shutil.rmtree('folder')

def test_corrupted_arg():
    assert check_args(['--holp']) == __FAILCODE
