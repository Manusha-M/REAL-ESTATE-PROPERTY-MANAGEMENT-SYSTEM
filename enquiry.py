from pathlib import Path

BASE = Path(__file__).resolve().parent


class Enquiry:
    FILE = BASE / 'data' / 'enquiries.txt'
    DELIMITER = '|'

    @staticmethod
    def _clean(value):
        return str(value).replace('|', '/').replace('\n', ' ').replace('\r', ' ')

    @classmethod
    def load(cls):
        enquiries = []
        try:
            with open(cls.FILE, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.rstrip('\n')
                    if not line:
                        continue
                    parts = line.split(cls.DELIMITER)
                    if len(parts) != 5:
                        continue
                    try:
                        enquiries.append({
                            'enquiry_id': int(parts[0]), 'customer_id': int(parts[1]),
                            'property_id': int(parts[2]), 'message': parts[3],
                            'status': parts[4]
                        })
                    except ValueError:
                        continue
        except FileNotFoundError:
            cls.FILE.parent.mkdir(parents=True, exist_ok=True)
            with open(cls.FILE, 'w', encoding='utf-8'):
                pass
        except OSError as error:
            print('Unable to read enquiries file:', error)
        return enquiries

    @classmethod
    def save(cls, enquiries):
        try:
            cls.FILE.parent.mkdir(parents=True, exist_ok=True)
            with open(cls.FILE, 'w', encoding='utf-8') as file:
                for enquiry in enquiries:
                    file.write(cls.DELIMITER.join([
                        str(enquiry['enquiry_id']), str(enquiry['customer_id']),
                        str(enquiry['property_id']), cls._clean(enquiry['message']),
                        cls._clean(enquiry['status'])
                    ]) + '\n')
        except OSError as error:
            print('Unable to save enquiries:', error)

    @classmethod
    def add(cls, customer_id, property_id, message):
        enquiries = cls.load()
        enquiry_id = max([e['enquiry_id'] for e in enquiries], default=0) + 1
        enquiries.append({
            'enquiry_id': enquiry_id, 'customer_id': customer_id,
            'property_id': property_id, 'message': message, 'status': 'New'
        })
        cls.save(enquiries)

    @classmethod
    def view_all_detailed(cls):
        from user import User
        from property import Property
        enquiries = cls.load()
        users = {u['user_id']: u for u in User.load_users()}
        properties = {p['property_id']: p for p in Property.load_properties()}
        if not enquiries:
            print('No enquiries found.')
            return
        for e in enquiries:
            customer = users.get(e['customer_id'], {})
            prop = properties.get(e['property_id'], {})
            print(
                f"Enquiry ID:{e['enquiry_id']} | Customer:{customer.get('name', 'Unknown')} | "
                f"Email:{customer.get('email', '')} | Property:{prop.get('title', 'Unknown')} "
                f"(ID:{e['property_id']}) | Message:{e['message']} | Status:{e['status']}"
            )

    @classmethod
    def view_for_property(cls, property_id, agent_id=None):
        from property import Property
        from user import User
        prop = Property.get_property(property_id)
        if agent_id is not None and (not prop or prop['agent_id'] != agent_id):
            print('Property not found or not owned by you.')
            return
        users = {u['user_id']: u for u in User.load_users()}
        enquiries = [e for e in cls.load() if e['property_id'] == property_id]
        if not enquiries:
            print('No enquiries for this property.')
            return
        for e in enquiries:
            customer = users.get(e['customer_id'], {})
            print(
                f"Enquiry ID:{e['enquiry_id']} | Customer:{customer.get('name', 'Unknown')} | "
                f"Email:{customer.get('email', '')} | Message:{e['message']} | Status:{e['status']}"
            )

    @classmethod
    def view_for_agent(cls, agent_id):
        from property import Property
        property_ids = {p['property_id'] for p in Property.load_properties() if p['agent_id'] == agent_id}
        enquiries = [e for e in cls.load() if e['property_id'] in property_ids]
        if not enquiries:
            print('No customer enquiries for your properties.')
            return
        for e in enquiries:
            cls.view_for_property(e['property_id'], agent_id)

    @classmethod
    def view_for_customer(cls, customer_id):
        enquiries = [e for e in cls.load() if e['customer_id'] == customer_id]
        if not enquiries:
            print('No enquiries found.')
            return
        for e in enquiries:
            print(
                f"Enquiry ID:{e['enquiry_id']} | Property ID:{e['property_id']} | "
                f"Message:{e['message']} | Status:{e['status']}"
            )
