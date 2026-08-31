from user import User
from property import Property


class Agent(User):
    @classmethod
    def from_dict(cls, user):
        return cls(user['user_id'], user['name'], user['email'], user['password'], 'agent')

    def add_property_interactive(self):
        Property.add_property_interactive(self.user_id)

    def view_my_properties(self):
        properties = [p for p in Property.load_properties() if p['agent_id'] == self.user_id]
        if not properties:
            print('You have no properties.')
            return
        for p in properties:
            Property(**p).display()

    def update_my_property(self, property_id):
        properties = Property.load_properties()
        for p in properties:
            if p['property_id'] == property_id and p['agent_id'] == self.user_id:
                try:
                    for key, label in [
                        ('title', 'Title'), ('location', 'Location'),
                        ('price', 'Price'), ('bedrooms', 'Bedrooms'),
                        ('description', 'Description')
                    ]:
                        value = input(f'{label} [{p[key]}]: ').strip()
                        if value:
                            if key == 'price':
                                p[key] = float(value)
                            elif key == 'bedrooms':
                                p[key] = int(value)
                            else:
                                p[key] = value
                    p['status'] = 'Pending'
                    Property.save_properties(properties)
                    print('Property updated and sent for admin approval.')
                except ValueError:
                    print('Price and bedrooms must contain valid numbers. Changes were not saved.')
                return
        print('Property not found or not owned by you.')

    def delete_my_property(self, property_id):
        properties = Property.load_properties()
        new_properties = [
            p for p in properties
            if not (p['property_id'] == property_id and p['agent_id'] == self.user_id)
        ]
        if len(new_properties) == len(properties):
            print('Property not found or not owned by you.')
        else:
            Property.save_properties(new_properties)
            print('Property deleted.')

    def update_my_property_status(self, property_id):
        properties = Property.load_properties()
        for p in properties:
            if p['property_id'] == property_id and p['agent_id'] == self.user_id:
                if p['status'] not in ('Approved', 'Available', 'Sold', 'Rented'):
                    print('Admin must approve this property first.')
                    return
                status = input('Availability (Available/Sold/Rented): ').strip().title()
                if status not in ('Available', 'Sold', 'Rented'):
                    print('Invalid status.')
                    return
                p['status'] = status
                Property.save_properties(properties)
                print('Availability updated.')
                return
        print('Property not found.')

    def view_bookings(self):
        bookings = Property.load_bookings()
        properties = {p['property_id']: p for p in Property.load_properties()}
        users = {u['user_id']: u for u in self.load_users()}
        my_property_ids = {
            p['property_id'] for p in properties.values() if p['agent_id'] == self.user_id
        }
        mine = [b for b in bookings if b['property_id'] in my_property_ids]
        if not mine:
            print('No booking requests for your properties.')
            return
        for booking in mine:
            customer = users.get(booking['customer_id'], {})
            print(
                f"Booking ID: {booking['booking_id']} | Customer: {customer.get('name', 'Unknown')} | "
                f"Email: {customer.get('email', '')} | Property ID: {booking['property_id']} | "
                f"Status: {booking['status']}"
            )
