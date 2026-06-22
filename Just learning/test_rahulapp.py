
import page
import pytest
from playwright.sync_api import Page, Playwright,expect



def test_login_into_url(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    Page =context.new_page()
    page.goto("https://rahulshettyacademy.com")
   # page.get_by_label("Dismiss popup").is_visible()
    #print("Yes")
   # page.get_by_label("Dismiss popup svg  ")
    #print("done")
    #page.get_by_role("link",name="Practice Apps").click()   
    websites=page.locator("p-6.flex.flex-col.flex-1.gap-3.px-6.pb-6.pt-2 h3").text_content()
                              #=page.locator("//div[@class='p-6 flex flex-col flex-1 gap-3 px-6 pb-6 pt-2']").text_content()
    print(websites)

def test_login_into_vegetable(playwright:Playwright):
        browser=playwright.chromium.launch(headless=False)
        context=browser.new_context()
        page =context.new_page()
        page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")
        productsname=page.locator(".products h4").all_text_contents()
        print(productsname)
        for products in productsname:
              
              productlist=products.split("-")
              productnames=productlist[0]
              if "Raspberry" in productnames:
                page.locator(".product").filter(has_text="Raspberry").get_by_role("button", name ="ADD TO CART").click()
                print("1stAdded")
              if "Capsicum" in productnames:
                page.locator(".product").filter(has_text="Capsicum").get_by_role("button", name ="ADD TO CART").click()
                print("2nd Added")
              if"Pears" in productnames:
                page.locator(".product").filter(has_text="Pears").get_by_role("button", name ="ADD TO CART").click()
                print("3rd Added")
        page.locator(".cart-icon").click()   
        #clicking proceed to check out 
        page.get_by_role("button",name="PROCEED TO CHECKOUT").click()
        #in the cart page
        #Total items in the cart
        page.wait_for_selector("#productCartTables tbody tr")
        Totalitemsincart=page.locator("#productCartTables tbody tr").count()
        print(f"Total items in cart are:{Totalitemsincart}")

        page.wait_for_selector("#productCartTables thead tr td b")
        Columnnumber=page.locator("#productCartTables thead tr td b").count()
        print(f"Total columns are:{Columnnumber}")
        Columnsnames=page.locator("#productCartTables thead tr td b").all_text_contents()
        print(Columnsnames)
        #Udemy tutor will confirm
        page.wait_for_selector(".products .cartTable tbody tr td")
        Amounts=page.locator(".products .cartTable tbody tr .amount").all_inner_texts()
        print(Amounts)
        sum=0
        for i in Amounts:
            
            sum =int(i) + sum
        print(f"Total amount is :{sum}")



       # To find only Rasberry related DeprecationWarning
        Locate=page.locator(".products .cartTable tbody tr").filter(has_text="Raspberry - 1/4 Kg")
        
       
        page.wait_for_selector(".products .cartTable thead tr")
        print(page.locator(".products .cartTable thead tr td").all_text_contents())
        page.wait_for_selector(".products .cartTable  tbody tr td")
         
        Cartproduct=page.locator(".products .cartTable  tbody tr td  .product-name").all_text_contents()
        for product in Cartproduct:
            if "Capsicum" in product:
                expect (page.locator(".product-name").filter(has_text="Capsicum")).to_be_visible()
                Producte=page.locator(".product-name").filter(has_text="Capsicum")
                print("Capsicum is present in cart")
         
                 
                page.get_by_placeholder("Enter promo code").fill("ABC123")
                page.get_by_role("button",name="Apply").click()
                print("clicked")
                page.wait_for_selector(".promoInfo")
                print(page.locator(".promoInfo").text_content())
        page.get_by_role("button",name="Place Order").click()
        page.get_by_role("button",name="Proceed").click()
        page.locator(".wrapperTwo div select").select_option("India")
        page.locator(".chkAgree").click()
        
        with page.expect_popup() as childwindow:
            page.get_by_role("link",name="Terms & Conditions").click()
            childpage=childwindow.value
            print("Text after clicking T&Cs is :" +page.locator(".wrapperTwo").text_content())
            childpage.wait_for_selector(".wrapperTwo")
            print("Text in the child window is:"+childpage.locator(".wrapperTwo").text_content())
            childpage.close()
        page.get_by_role("button",name="Proceed").click()
        print("last text is:"+ page.locator(".wrapperTwo").text_content())


