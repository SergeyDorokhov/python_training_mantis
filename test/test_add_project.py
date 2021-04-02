import pytest

from data.projects import testdata


@pytest.mark.parametrize("project", testdata, ids=(repr(x) for x in testdata))
def test_add_project(app, db, project):
    list_before = db.get_project_list()
    app.project.create(project)
    project.id = db.get_project_list()[-1].id
    list_before.append(project)
    assert list_before == db.get_project_list()
