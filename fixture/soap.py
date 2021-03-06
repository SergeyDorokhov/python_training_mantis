from suds import WebFault
from suds.client import Client

from model.project import Project


class SoapHelper:
    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.config['web']['base_url'] +'api/soap/mantisconnect.php?wsdl')
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username, password):
        client = Client(self.app.config['web']['base_url'] + 'api/soap/mantisconnect.php?wsdl')
        list_projects = []
        try:
            projects = list(client.service.mc_projects_get_user_accessible(username, password))
            for project in projects:
                list_projects.append(Project(name=project.name, id=project.id))
            return list_projects
        except WebFault:
            return None
