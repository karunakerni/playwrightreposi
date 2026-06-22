from playwright.sync_api import Page, expect

def test_user_navigating_to_url(page:Page):
    page.goto("https://the-internet.herokuapp.com/")
    expect(page).to_have_title("The Internet")
    