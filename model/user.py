from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class User:
    """
    a user
    """
    username: str
    password: str
    role: str

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value
