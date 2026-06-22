
class clearBookingButton:
    def __init__(self,page):
        self.page=page
        
    role_button="Clear all bookings"   

    def clear_booking(self):
        self.page.get_by_role("button",name=self.role_button).click()

