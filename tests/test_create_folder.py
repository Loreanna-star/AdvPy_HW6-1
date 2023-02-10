import requests
import configparser
import pytest
import os
from main_1 import YandexDisk

@pytest.fixture
def setup():
    conf = configparser.ConfigParser()
    ROOT_PATH = os.getcwd()
    FILE_NAME = "tokens.ini"
    DIR = "tests"
    full_path = os.path.join(ROOT_PATH, DIR, FILE_NAME)
    conf.read(full_path)
    TOKEN_YaDisk = conf["YandexDisk"]["TOKEN"]
    
    YaDiskUser = YandexDisk(TOKEN_YaDisk)
    yield YaDiskUser
    URL = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = YaDiskUser.get_headers()
    params = {
        "path": "testfolder"
        }
    requests.delete(URL, headers=headers, params=params)

def test_create_folder(setup):
    YaDiskUser = setup
    result = YaDiskUser.create_folder("testfolder")
    assert result == 201