
def suit(card: str) -> str:
    """Return the second character of the card.

    Preconditions: card has two characters;
    the first is one of 'A', '2' to '9', 'T', 'J', 'Q', 'K'
    the second is one of 'C', 'D', 'H' 'S'
    """
    return card[1]

VALUES = 'A23456789TJQK'

def value(card: str) -> int:
    """Return the value of the card.

    Preconditions: as for function 'suit'
    Postconditions: the output is 1 to 13 respectively for
    'A', '2' to '9', 'T', 'J', 'Q', 'K'
    """
    for index in range(len(VALUES)):
        if VALUES[index] == card[0]:
            return index + 1        # return 1—13, not 0—12

def suit_value(card: str) -> tuple:
    """Return a tuple with the suit and value of the card.

    Preconditions: as for function 'suit'
    """
    return (suit(card), value(card))

UP_DOWN = ['AS','3H','QD','KC'] # ascending values, descending suits
SAME_VALUE = ['TD', 'TS', 'TH', 'TC']

sorting_tests = [
    # case,        unsorted,           key, sorted
    ('empty list', [],          suit_value, []),
    ('1 card',     ['AS'],      suit_value, ['AS']),
    ('same cards', ['6D','6D'], suit_value, ['6D','6D']),
    ('3 cards',    ['JC','8D','TS'], value, ['8D','TS','JC']),
    ('values up',  UP_DOWN,          value, UP_DOWN),
    ('suits down', UP_DOWN,           suit, ['KC','QD','3H','AS']),
    ('same value', SAME_VALUE,  suit_value, ['TC','TD','TH','TS']),
]

def identity(item: object) -> object:
    """Return the item, i.e. the key is the whole item."""
    return item
