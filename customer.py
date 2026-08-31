from user import User
from property import Property
from enquiry import Enquiry


class Customer(User):
    @classmethod
    def from_dict(cls, user):
        return cls(user['user_id'], user['name'], user['email'], user['password'], 'customer')

    @staticmethod
    def search_properties_interactive(approved_only=True):
        try:
            location = input('Location (Enter to skip): ').strip()
            property_type = input('Property type (Enter to skip): ').strip()
            max_price = input('Maximum price (Enter to skip): ').strip()
            max_price_value = float(max_price) if max_price else None
            properties = Property.load_properties()
            found = False
            for p in properties:
                if approved_only and p['status'] not in ('Approved', 'Available'):
                    continue
                if location and location.lower() not in p['location'].lower():
                    continue
                if property_type and property_type.lower() != p['property_type'].lower():
                    continue
                if max_price_value is not None and p['price'] > max_price_value:
                    continue
                Property(**p).display()
                found = True
            if not found:
                print('No matching properties found.')
        except ValueError:
            print('Maximum price must be a valid number.')
        except Exception as error:
            print('Search error:', error)

    def send_enquiry(self, property_id, message):
        property_data = Property.get_property(property_id)
        if not property_data or property_data['status'] not in ('Approved', 'Available'):
            print('Approved property not found.')
            return
        if not message:
            print('Message cannot be empty.')
            return
        Enquiry.add(self.user_id, property_id, message)
        print('Enquiry sent successfully. Agent can now see it.')

    def booking_request(self, property_id):
        property_data = Property.get_property(property_id)
        if not property_data or property_data['status'] not in ('Approved', 'Available'):
            print('Approved property not found.')
            return
        bookings = Property.load_bookings()
        if any(
            b['customer_id'] == self.user_id and
            b['property_id'] == property_id and
            b['status'] == 'Requested'
            for b in bookings
        ):
            print('Booking request already exists.')
            return
        booking_id = max([b['booking_id'] for b in bookings], default=0) + 1
        bookings.append({
            'booking_id': booking_id, 'customer_id': self.user_id,
            'property_id': property_id, 'status': 'Requested'
        })
        Property.save_bookings(bookings)
        print('Booking request sent.')

    def view_bookings(self):
        bookings = [b for b in Property.load_bookings() if b['customer_id'] == self.user_id]
        if not bookings:
            print('No bookings found.')
            return
        for booking in bookings:
            print(
                f"Booking ID: {booking['booking_id']} | Property ID: {booking['property_id']} | "
                f"Status: {booking['status']}"
            )
