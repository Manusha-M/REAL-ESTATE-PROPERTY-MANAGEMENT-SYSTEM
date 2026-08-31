from user import User
from property import Property


class Admin(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password, 'admin')

    @classmethod
    def from_dict(cls, user):
        return cls(user['user_id'], user['name'], user['email'], user['password'])

    @classmethod
    def create_default_accounts(cls):
        users = cls.load_users()
        defaults = [
            (1, 'System Admin', 'admin@gmail.com', 'admin123', 'admin'),
            (2, 'Demo Agent', 'agent@gmail.com', 'agent123', 'agent'),
            (3, 'Demo Customer', 'customer@gmail.com', 'customer123', 'customer')
        ]
        changed = False
        for user_id, name, email, password, role in defaults:
            if not any(u['email'].lower() == email.lower() for u in users):
                users.append({
                    'user_id': user_id, 'name': name, 'email': email,
                    'password': password, 'role': role
                })
                changed = True
        if changed or not cls.FILE.exists():
            cls.save_users(users)

    def add_agent(self, name, email, password):
        if not name or not password or not self.validate_email(email):
            print('Invalid agent details.')
            return
        users = self.load_users()
        if any(u['email'].lower() == email.lower() for u in users):
            print('Email already exists.')
            return
        user_id = max([u['user_id'] for u in users], default=0) + 1
        users.append({
            'user_id': user_id, 'name': name, 'email': email,
            'password': password, 'role': 'agent'
        })
        self.save_users(users)
        print('Agent added successfully.')

    def view_agents(self):
        agents = [u for u in self.load_users() if u['role'] == 'agent']
        if not agents:
            print('No agents found.')
            return
        for user in agents:
            print(f"ID:{user['user_id']} | {user['name']} | {user['email']}")

    def view_customers(self):
        customers = [u for u in self.load_users() if u['role'] == 'customer']
        if not customers:
            print('No customers found.')
            return
        for user in customers:
            print(f"ID:{user['user_id']} | {user['name']} | {user['email']}")

    def add_property_interactive(self):
        Property.add_property_interactive(None)

    def view_bookings_detailed(self):
        bookings = Property.load_bookings()
        users = {u['user_id']: u for u in self.load_users()}
        properties = {p['property_id']: p for p in Property.load_properties()}
        if not bookings:
            print('No booking requests.')
            return
        for booking in bookings:
            customer = users.get(booking['customer_id'], {})
            prop = properties.get(booking['property_id'], {})
            print(
                f"Booking ID: {booking['booking_id']} | Customer: {customer.get('name', 'Unknown')} "
                f"({customer.get('email', '')}) | Property: {prop.get('title', 'Unknown')} "
                f"[ID {booking['property_id']}] | Status: {booking['status']}"
            )

    def update_booking(self, booking_id, status):
        bookings = Property.load_bookings()
        for booking in bookings:
            if booking['booking_id'] == booking_id:
                booking['status'] = status
                Property.save_bookings(bookings)
                print(f'Booking {booking_id} changed to {status}.')
                return
        print('Booking not found.')
