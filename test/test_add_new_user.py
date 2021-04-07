def test_add_new_user(app):
    app.wd.find_element_by_link_text("Signup for a new account").click()
