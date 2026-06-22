from playwright.sync_api import Page


class UIlogin:

    EMAIL_INPUT = "you@email.com"
    PASSWORD_INPUT = "••••••"
    SIGN_IN_BUTTON = "Sign In"

    def __init__(self, page):
        self.page = page

    def url_login(self, email, password):
        self.page.goto("https://eventhub.rahulshettyacademy.com/login")
        self.page.get_by_placeholder(self.EMAIL_INPUT).fill(email)
        self.page.get_by_placeholder(self.PASSWORD_INPUT).fill(password)
        self.page.get_by_role("button", name=self.SIGN_IN_BUTTON).click()
        print(self.page.title())
