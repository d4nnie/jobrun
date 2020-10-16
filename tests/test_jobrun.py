import os
import shutil
import jobrun

def test_read_yaml():
    yaml = jobrun.read_yaml('example.yml')

    assert yaml['before_script'] == ['touch file']
    assert 'script' in yaml['run.example']

def test_before_script():
    yaml = jobrun.read_yaml('example.yml')
    runner = jobrun.Runner(yaml)
    runner.before_script()

    assert os.path.exists('file')
    os.remove('file')

def test_job():
    yaml = jobrun.read_yaml('example.yml')
    runner = jobrun.Runner(yaml)
    runner.job('run.example')

    assert os.path.exists('folder')
    assert os.path.exists('folder/file_in_folder')
    shutil.rmtree('folder')
