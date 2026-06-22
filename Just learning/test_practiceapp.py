
from playwright.sync_api import Page, Playwright,expect

def test_practice_page_login(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page =context.new_page()
    page.goto("https://rahulshettyacademy.com")
    page.get_by_role("link",name="Practice Apps").click()
    page.wait_for_selector(".p-6.flex.flex-col.flex-1.gap-3.pt-4.pb-5.px-5 div h3")
    appnames=page.locator(".p-6.flex.flex-col.flex-1.gap-3.pt-4.pb-5.px-5 div h3").all_text_contents()
    print(appnames)
    if "Selenium Practice - GreenKart" in appnames:
          with page.expect_popup() as childwndow:
              page.wait_for_selector("p-6.flex.flex-col.flex-1.gap-3.pt-4.pb-5.px-5  button")
              page.wait_for_selector("p-6.flex.flex-col.flex-1.gap-3.pt-4.pb-5.px-5  button").filter(has_text="Start Practicing")
              #page.get_by_role("button",name ="Start Practicing").click()
              print("clicked")
              childpage= childwndow.value
              print(childpage.Title())

    
def test_final_code():
     from playwright.sync_api import sync_playwright

def test_greenkart_popup():
    with sync_playwright() as p:
        # 1. Launch browser and open the practice page
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        page.goto("https://rahulshettyacademy.com/practice")
        
        # 2. Click on "Practice Apps" to see the cards layout
        page.get_by_role("link", name="Practice Apps").click()
        
        # 3. Find the specific card box for GreenKart and target its button
        # This isolates the card container so you don't click the wrong button
        greenkart_card = page.locator("div.card, div.p-6").filter(has_text="Selenium Practice - GreenKart")
        
        # 4. Set up the popup listener and click "Start Practicing" inside that card
        with page.expect_popup() as popup_info:
            greenkart_card.get_by_text("Start Practicing").click()
            
        # 5. Work with the newly opened GreenKart child window
        child_page = popup_info.value
        child_page.wait_for_load_state()
        
        print("Successfully opened child window:", child_page.title())
        
        # Clean up
        child_page.close()
        browser.close()


    