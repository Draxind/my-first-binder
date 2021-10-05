
def head(items: list) -> object:
    """Return the first item of the list.

    Preconditions: items isn't empty
    """
    return items[0]

def tail(items: list) -> list:
    """Return the list without the first item.

    Preconditions: items isn't empty
    """
    return items[1:len(items)]

def is_empty(items: list) -> bool:
    """Return True if and only if the list is empty."""
    return items == []

def prepend(item: object, items: list) -> list:
    """Return a new list with item as head and items as tail."""
    return [item] + items
