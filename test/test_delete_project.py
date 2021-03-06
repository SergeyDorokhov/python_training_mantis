import random

import pytest

from data.projects import testdata


# @pytest.mark.parametrize("project", testdata, ids=(repr(x) for x in testdata))
# def test_delete_project(app, db, project):
#     list_before = db.get_project_list()
#     if len(list_before) == 0:
#         app.project.create(project)
#         list_before = db.get_project_list()
#     project = random.choice(list_before)
#     app.project.delete(project)
#     list_before.remove(project)
#     assert list_before == db.get_project_list()


@pytest.mark.parametrize("project", testdata, ids=(repr(x) for x in testdata))
def test_delete_project_with_soap(app, db, project):
    webadmin = app.config['webadmin']
    username = webadmin['username']
    password = webadmin['password']

    list_before = app.soap.get_project_list(username, password)
    if len(list_before) == 0:
        app.project.create(project)
        list_before = db.get_project_list()
    project = random.choice(list_before)
    app.project.delete(project)
    list_before.remove(project)
    assert sorted(list_before) == sorted(app.soap.get_project_list(username, password))
