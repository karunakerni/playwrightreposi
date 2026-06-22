import json
import page
import pytest

from pages.Browservent import Events
from pages.clearbooking import clearBookingButton
from pages.login import ApiLoginPage
from pages.login_ui import UIlogin
from pages.viewbbooking import Booking


with open("testdata/Credentials.json") as file:
    data = json.load(file)
credentials_list = data["user_credentials"]

@pytest.mark.parametrize('credentials', credentials_list)
def test_executions(context, credentials):
    

    loginaobj = ApiLoginPage(context)
    token = loginaobj.url_APi_login(credentials["email"], credentials["password"])
    assert token is not None, "Login failed — invalid credentials"
   
    
    #booking_reference = loginaobj.browse_events(context, token,credentials["name"],credentials["email"],credentials["phone"],3)
    page = context.new_page()
    loguiobj=UIlogin()
    loguiobj.url_login(page,credentials["email"],credentials["password"])


    Eventsobj=Events()
    booking_reference=Eventsobj.browse_events(context,token,credentials["email"],credentials["name"],credentials["phone"],3)

    Bookobj= Booking()
    Bookobj.view_booking(page,booking_reference)
    #expect(page).to_have_title("EventHub — Discover & Book Events")

    

    
  
