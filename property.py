from pathlib import Path

BASE = Path(__file__).resolve().parent


class Property:
    FILE = BASE / 'data' / 'properties.txt'
    BOOKING_FILE = BASE / 'data' / 'bookings.txt'
    DELIMITER = '|'

    def __init__(self, property_id, title, property_type, location, price,
                 bedrooms, agent_id, description='', status='Pending'):
        self.property_id = int(property_id)
        self.title = title
        self.property_type = property_type
        self.location = location
        self.price = float(price)
        self.bedrooms = int(bedrooms)
        self.agent_id = int(agent_id)
        self.description = description
        self.status = status

    @staticmethod
    def _clean(value):
        return str(value).replace('|', '/').replace('\n', ' ').replace('\r', ' ')

    def display(self):
        print(
            f"\nID:{self.property_id} | {self.title} | {self.property_type} | "
            f"{self.location} | ₹{self.price:,.2f} | {self.bedrooms} BHK | "
            f"Agent:{self.agent_id} | Status:{self.status}\nDescription: {self.description}"
        )

    @classmethod
    def load_properties(cls):
        properties = []
        try:
            with open(cls.FILE, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.rstrip('\n')
                    if not line:
                        continue
                    parts = line.split(cls.DELIMITER)
                    if len(parts) != 9:
                        continue
                    try:
                        properties.append({
                            'property_id': int(parts[0]), 'title': parts[1],
                            'property_type': parts[2], 'location': parts[3],
                            'price': float(parts[4]), 'bedrooms': int(parts[5]),
                            'agent_id': int(parts[6]), 'description': parts[7],
                            'status': parts[8]
                        })
                    except ValueError:
                        continue
        except FileNotFoundError:
            cls.FILE.parent.mkdir(parents=True, exist_ok=True)
            with open(cls.FILE, 'w', encoding='utf-8'):
                pass
        except OSError as error:
            print('Unable to read properties file:', error)
        return properties

    @classmethod
    def save_properties(cls, properties):
        try:
            cls.FILE.parent.mkdir(parents=True, exist_ok=True)
            with open(cls.FILE, 'w', encoding='utf-8') as file:
                for p in properties:
                    file.write(cls.DELIMITER.join([
                        str(p['property_id']), cls._clean(p['title']),
                        cls._clean(p['property_type']), cls._clean(p['location']),
                        str(p['price']), str(p['bedrooms']), str(p['agent_id']),
                        cls._clean(p.get('description', '')), cls._clean(p.get('status', 'Pending'))
                    ]) + '\n')
        except OSError as error:
            print('Unable to save properties:', error)

    @classmethod
    def add_property_interactive(cls, agent_id):
        try:
            title = input('Title: ').strip()
            typ = input('Property type (Apartment/Villa/House/Plot): ').strip().title()
            loc = input('Location: ').strip()
            price = float(input('Price: ').strip())
            bedrooms = int(input('Bedrooms: ').strip())
            desc = input('Description: ').strip()
            if not title or not typ or not loc or price < 0 or bedrooms < 0:
                print('Invalid property details.')
                return
            properties = cls.load_properties()
            property_id = max([p['property_id'] for p in properties], default=100) + 1
            properties.append({
                'property_id': property_id, 'title': title, 'property_type': typ,
                'location': loc, 'price': price, 'bedrooms': bedrooms,
                'agent_id': agent_id or 0, 'description': desc, 'status': 'Pending'
            })
            cls.save_properties(properties)
            print(f'Property added successfully. Property ID: {property_id}. Status: Pending.')
        except ValueError:
            print('Price and bedrooms must be valid numbers.')
        except Exception as error:
            print('Unable to add property:', error)

    @classmethod
    def get_property(cls, property_id):
        return next((p for p in cls.load_properties() if p['property_id'] == property_id), None)

    @classmethod
    def view_all(cls):
        properties = cls.load_properties()
        if not properties:
            print('No properties found.')
            return
        for p in properties:
            cls(**p).display()

    @classmethod
    def view_approved(cls):
        properties = [p for p in cls.load_properties() if p['status'] in ('Approved', 'Available')]
        if not properties:
            print('No approved properties available.')
            return
        for p in properties:
            cls(**p).display()

    @classmethod
    def view_details(cls, property_id):
        p = cls.get_property(property_id)
        if not p:
            print('Property not found.')
        elif p['status'] not in ('Approved', 'Available'):
            print('Property is not approved yet.')
        else:
            cls(**p).display()

    @classmethod
    def update_status(cls, property_id, status):
        properties = cls.load_properties()
        for p in properties:
            if p['property_id'] == property_id:
                p['status'] = status
                cls.save_properties(properties)
                print(f'Property {property_id} is now {status}.')
                return
        print('Property not found.')

    @classmethod
    def delete_property(cls, property_id):
        properties = cls.load_properties()
        new_properties = [p for p in properties if p['property_id'] != property_id]
        if len(new_properties) == len(properties):
            print('Property not found.')
        else:
            cls.save_properties(new_properties)
            print('Property deleted.')

    @classmethod
    def load_bookings(cls):
        bookings = []
        try:
            with open(cls.BOOKING_FILE, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(cls.DELIMITER)
                    if len(parts) != 4:
                        continue
                    try:
                        bookings.append({
                            'booking_id': int(parts[0]), 'customer_id': int(parts[1]),
                            'property_id': int(parts[2]), 'status': parts[3]
                        })
                    except ValueError:
                        continue
        except FileNotFoundError:
            cls.BOOKING_FILE.parent.mkdir(parents=True, exist_ok=True)
            with open(cls.BOOKING_FILE, 'w', encoding='utf-8'):
                pass
        except OSError as error:
            print('Unable to read bookings file:', error)
        return bookings

    @classmethod
    def save_bookings(cls, bookings):
        try:
            cls.BOOKING_FILE.parent.mkdir(parents=True, exist_ok=True)
            with open(cls.BOOKING_FILE, 'w', encoding='utf-8') as file:
                for booking in bookings:
                    file.write(cls.DELIMITER.join([
                        str(booking['booking_id']), str(booking['customer_id']),
                        str(booking['property_id']), cls._clean(booking['status'])
                    ]) + '\n')
        except OSError as error:
            print('Unable to save bookings:', error)
