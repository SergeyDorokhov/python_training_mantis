from selenium import webdriver

from fixture.james import JamesHelper
from fixture.navigation import NavigationHelper
from fixture.project import ProjectHelper
from fixture.session import SessionHelp
from fixture.mail import MailHelper
from fixture.signup import SignupHelper
from fixture.soap import SoapHelper


class Application:
    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognised browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.config = config
        self.session = SessionHelp(self)
        self.navigation = NavigationHelper(self, base_url=config['web']['base_url'])
        self.project = ProjectHelper(self)
        self.james = JamesHelper(self)
        self.mail = MailHelper(self)
        self.signup = SignupHelper(self)
        self.soap = SoapHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
