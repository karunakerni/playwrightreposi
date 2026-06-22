


from playwright.sync_api import Playwright,expect,Page,TimeoutError


def test_basictesting(page :Page):
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_title("The Internet")
    expect(page).to_have_title("The Internet")
    page.get_by_role("link", name="Checkboxes").click()  
    page.go_back()
    print(page.url)
    page.get_by_role("link",name="A/B Testing").click()
    print("All links are working fine")
    #page.go_back()
    #Heading=page.get_by_role("heading",name="A/B Test Variation 1").text_content()
    Heading=page.locator("h3")
    expect(Heading).to_contain_text("A/B Test")
    print("Heading")
    Text=page.locator("div.example").locator("p").text_content()
    print(Text)
    page.go_back()

def test_basic_auth_window(page:Page):
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="Basic Auth").click()
    sucess_message=page.locator( "div.example").locator("p").text_content()
    print(sucess_message)
    page.go_back()
    page.get_by_role("link",name="Add/Remove Elements").click()
    #text_con=page.get_by_role("button",name="Add Element").text_content()
    expect(page.get_by_role("button",name="Add Element")).to_have_text("Add Element")
    page.get_by_role("button",name="Add Element").click()
    page.get_by_role("button",name="Delete").click()
    print("Hi , Deleted")
    try:
        page.get_by_role("button",name="Delete").click(timeout=3000)
    except  TimeoutError as e:
        print("Element not found")     
    page.go_back()
    page.get_by_role("link",name="Checkboxes").click()
    page.locator("xpath=//input[@type='checkbox'][following-sibling::text()[contains(., 'checkbox 1')]]").check()
    try:
        page.locator("xpath=//inputs[@type='checkbox'][following-sibling::text()[contains(.,'checkbox 3')]]").click(timeout=3000)
    except TimeoutError as e:
        print("notfound")  
    page.go_back()       
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("link",name='Context Menu').click()
    page.locator("#hot-spot").click(button="right")
    print("accepted")
    page.go_back()
    page.get_by_role("link",name="Dropdown").click()
    print("done")
    page.wait_for_selector("#dropdown")
    options =page.locator("#dropdown option").all_text_contents()
    print(options)
    for option in options:
        if "Option 2" in options:
            page.locator("#dropdown").select_option(label="Option 2")
            print("Selected Option 2")
            break


