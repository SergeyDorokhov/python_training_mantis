class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.app.navigation.move_to_manage_project_page()
        wd.find_element_by_css_selector("input[value = 'Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def fill_project_form(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)

    def delete(self, project):
        wd = self.app.wd
        self.app.navigation.move_to_manage_project_page()
        wd.find_element_by_link_text(f"{project.name}").click()
        wd.find_element_by_css_selector("input[value = 'Delete Project']").click()
        wd.find_element_by_css_selector("input[value = 'Delete Project']").click()
