
class View:
    def __init__(self, page):
        self.page=page

    view_Details_button="view Details"


    def clicking_view(self,page):
        self.page.get_by_role("button",name=self.view_Details_button).click()
