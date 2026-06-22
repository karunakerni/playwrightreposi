
from playwright.sync_api import Page, expect

class Booking:

    
    def __init__(self,page):
       self.page =page
       
    def view_booking(self,page,bookingnumber):

        self.page.get_by_test_id("nav-bookings").click()
        print("Hi")
        print(bookingnumber)
        #nothing is getting catched here
       # page.wait_for_selectore("[class*='booking-ref']")
        References_booking=page.locator("[class*='booking-ref']").all_text_contents() 
        #Just to check
        print(References_booking)
        for referenc in References_booking:
            print(referenc)
            if referenc == bookingnumber:
             print("matched")
             self.page.get_by_role("button",name="View Details").click()
            else:
             self.page.get_by_role("button",name="Cancel Booking").click()

               

