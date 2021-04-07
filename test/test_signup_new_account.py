import string
import random

def random_username(prefix, maxlen):
   symbols = string.ascii_letters
   return prefix + "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))


def test_signup_new_account(app):
   username = random_username('user', 10)
   email = username + '@localhost'
   password = 'test'
   app.james.ensure_user_exist(username, password)
   app.signup.new_user(username, password, email)
   app.session.login(username, password)
   assert app.session.is_logged_in_as(username)
   app.session.logout()