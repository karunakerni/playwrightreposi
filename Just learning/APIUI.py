
import json

from playwright.sync_api import Playwright
import pytest
from pytest_playwright.pytest_playwright import page

class pagesmeth:


    def APi_login(playwright:Playwright,credentials):
       
        EMAIL=credentials["email"]
        PASSWORD=credentials["password"]
        browser=playwright.chromium.launch(headless=False)
        context=browser.new_context(base_url="https://api.eventhub.rahulshettyacademy.com")
        response=context.request.post("/api/auth/login",
                               headers={"content-type":"application/json"},
                               data = {"email": EMAIL, "password":PASSWORD })
        response_text=response.json()
        print(response_text)
        token=response_text["token"]
        print("Value of token is :+token")
                                    
    #page.get_by_role("button",name="login-btn").click()
        print(token)
        print("The titleof the page is :"+page.title())
        page.get_by_role("link", name ="/events").click()
        print("clicked")
        return token

  

                        
    
                              

    