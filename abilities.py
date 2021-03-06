from collections import namedtuple
from struct import unpack

Ability = namedtuple('Ability', ['name', 'mystery'])

abilities = []

with open('/tmp/conquest/fsroot/data/Tokusei.dat', 'rb') as ability_data:
    for ability in range(128):
        name, mystery = unpack('15s5s', ability_data.read(20))
        name = name.decode('Shift_JIS').rstrip('\x00')
        abilities.append(Ability(name, mystery))

if __name__ == '__main__':
    from binascii import hexlify

    for n, ability in enumerate(abilities):
        print('{0:3}. {1:15} {2}'.format(n, ability.name,
          hexlify(ability.mystery).decode('ASCII')))
