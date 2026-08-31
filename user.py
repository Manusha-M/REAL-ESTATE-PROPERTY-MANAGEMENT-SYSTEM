import re
from pathlib import Path

BASE = Path(__file__).resolve().parent


class User:
    FILE = BASE / 'data' / 'users.txt'
    DELIMITER = '|'

    def __init__(self, user_id, name, email, password, role):
        self.user_id = int(user_id)
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def to_record(self):
        return self.DELIMITER.join([
            str(self.user_id), self._clean(self.name), self._clean(self.email),
            self._clean(self.password), self._clean(self.role)
        ])

    @staticmethod
    def _clean(value):
        return str(value).replace('|', '/').replace('\n', ' ').replace('\r', ' ')

    @classmethod
    def load_users(cls):
        users = []
        try:
            with open(cls.FILE, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(cls.DELIMITER)
                    if len(parts) != 5:
                        continue
                    users.append({
                        'user_id': int(parts[0]), 'name': parts[1], 'email': parts[2],
                        'password': parts[3], 'role': parts[4]
                    })
        except FileNotFoundError:
            cls.FILE.parent.mkdir(parents=True, exist_ok=True)
            with open(cls.FILE, 'w', encoding='utf-8'):
                pass
        except (ValueError, OSError) as error:
            print('Unable to read users file:', error)
        return users

    @classmethod
    def save_users(cls, users):
        try:
            cls.FILE.parent.mkdir(parents=True, exist_ok=True)
            with open(cls.FILE, 'w', encoding='utf-8') as file:
                for user in users:
                    file.write(cls.DELIMITER.join([
                        str(user['user_id']), cls._clean(user['name']),
                        cls._clean(user['email']), cls._clean(user['password']),
                        cls._clean(user['role'])
                    ]) + '\n')
        except OSError as error:
            print('Unable to save users:', error)

    @staticmethod
    def validate_email(email):
        return bool(re.match(r'^[\w.%-]+@[\w.-]+\.[A-Za-z]{2,}$', email))

    @classmethod
    def register(cls, name, email, password):
        if not name or not password or not cls.validate_email(email):
            print('Enter valid name, email and password.')
            return
        users = cls.load_users()
        if any(u['email'].lower() == email.lower() for u in users):
            print('Email already registered.')
            return
        user_id = max([u['user_id'] for u in users], default=0) + 1
        users.append({
            'user_id': user_id, 'name': name, 'email': email,
            'password': password, 'role': 'customer'
        })
        cls.save_users(users)
        print('Customer registration successful!')

    @classmethod
    def login(cls, email, password):
        for user in cls.load_users():
            if user['email'].lower() == email.lower() and user['password'] == password:
                print(f"\nWelcome, {user['name']} ({user['role'].title()})!")
                return user
        print('Invalid email or password.')
        return None
