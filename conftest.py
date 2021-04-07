import json
import os

import ftputil
import pytest

from fixture.application import Application
from fixture.db import DbFixture

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target"))


@pytest.fixture
def app(request, config):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    web_config = config['webadmin']
    web_config_url = config['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, config=config)
        base_url = web_config_url['base_url']
    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return fixture


@pytest.fixture(scope="session")
def db(request, config):
    db_config = config['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'],
                          user=db_config['user'], password=db_config['password'])

    def fin():
        dbfixture.destroy()

    request.addfinalizer(fin)
    return dbfixture


def install_server_configuration(host, username, password):
    with ftputil.FTPHost(host, username, password) as remote:
        if remote.path.isfile('config_inc.php.bac'):
            remote.remove('config_inc.php.bac')
        if remote.path.isfile('config_inc.php'):
            remote.rename('config_inc.php', 'config_inc.php.bac')
        remote.upload(os.path.join(os.path.dirname(__file__), "resourses/config_inc.php"), "config_inc.php")


def restore_server_configuration(host, username, password):
    with ftputil.FTPHost(host, username, password) as remote:
        if remote.path.isfile('config_inc.php.bac'):
            if remote.path.isfile('config_inc.php'):
                remote.remove('config_inc.php')
            remote.rename('config_inc.php.bac', 'config_inc.php')


@pytest.fixture(scope="session", autouse=True)
def configure_server(request, config):
    install_server_configuration(config['ftp']['host'], config['ftp']['username'], config['ftp']['password'])

    def fin():
        restore_server_configuration(config['ftp']['host'], config['ftp']['username'], config['ftp']['password'])

    request.addfinalizer(fin)


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
