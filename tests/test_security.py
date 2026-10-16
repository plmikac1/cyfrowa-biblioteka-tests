from tests.pages.register_page import RegisterPage

def test_xss_not_executed_on_registration(page, base_url, random_string):
    rp = RegisterPage(page, base_url)
    rp.goto()
    payload = '<script>window.xss_test = "executed";</script>'
    username = "xss_" + random_string(6)
    email = f"{username}@example.com"
    password = "XssP@ss123"
    dialog_fired = {"called": False}
    def on_dialog(dialog):
        dialog_fired["called"] = True
        dialog.dismiss()
    page.on("dialog", on_dialog)

    rp.register(payload, email, password)
    assert dialog_fired["called"] is False, "Dialog fired — possible XSS execution"
    content = page.content()
    assert payload not in content, "Raw script payload found in page content (unescaped)"

def test_sql_injection_attempt(page, base_url, random_string):
    rp = RegisterPage(page, base_url)
    rp.goto()
    payload = "' OR '1'='1"
    username = "sql_" + random_string(6)
    email = f"{username}@example.com"
    password = payload
    rp.register(username, email, password)
    assert rp.get_error_text() or rp.get_success_text()