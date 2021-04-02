from selenium import webdriver

from fixture.navigation import NavigationHelper
from fixture.project import ProjectHelper
from fixture.session import SessionHelp


class Application:
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognised browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelp(self)
        self.navigation = NavigationHelper(self, base_url)
        self.project = ProjectHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
