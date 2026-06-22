class Events:

    END_POINT = "/api/events?limit=*"
    BOOKING_END_POINT = "/api/bookings"

    def __init__(self, context):
        self.context = context

    def browse_events(self, token, email, name, phone, quantity):
        response = self.context.request.get(
            self.END_POINT,
            headers={"authorization": "Bearer " + token, "content-type": "application/json; charset=utf-8"}
        )
        data_list = response.json()['data']
        for items in data_list:
            id = items.get("id")
            if items.get("category") == "Concert":
                response_booking = self.context.request.post(
                    self.BOOKING_END_POINT,
                    headers={"Authorization": "Bearer " + token, "content-type": "application/json"},
                    data={"customerName": name, "customerEmail": email, "customerPhone": phone, "eventId": id, "quantity": quantity}
                )
                booking_reference = response_booking.json().get("bookingRef")
                return booking_reference
