import keyring
from getpass import getpass


def _set_password():
    pw = getpass('Password: ')

    keyring.set_password('test', 'gary', pw)
    print(keyring.get_password('test', 'hello'))


_set_password()
