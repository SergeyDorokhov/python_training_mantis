class NavigationHelper:
    def __init__(self, app, base_url):
        self.app = app
        self.base_url = base_url

    def open_auth_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("login_page.php/"):
            wd.get(self.base_url)

    def open_manage_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("manage_overview_page.php")):
            wd.find_element_by_link_text("Manage").click()

    def open_manage_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("manage_proj_page.php")):
            wd.find_element_by_link_text("Manage Projects").click()
