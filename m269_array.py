
class StaticArray:
    """A fixed-length sequence of references in contiguous memory."""

    def __init__(self, length: int):
        """Create an array of the given length.

        Preconditions: length >= 0
        Postconditions: every item in the array is None
        """
        # assume lists are stored in arrays
        self.items = [None] * length

    def length(self) -> int:
        """Return the length of the array."""
        return len(self.items)

    def get_item(self, index: int) -> object:
        """Return the item at the given index.

        Preconditions: 0 <= index < self.length()
        """
        return self.items[index]

    def set_item(self, index: int, item: object) -> None:
        """Replace the item at the given index with the given item.

        Preconditions: 0 <= index < self.length()
        Postconditions: self.get_item(index) == item
        """
        self.items[index] = item

    def __str__(self) -> str:
        """Return a string representation of the array."""
        return str(self.items)

class DynamicArray(StaticArray):
    """An array that can grow and shrink."""

    def resize(self, length: int) -> None:
        """Shorten or extend the array to the new length.

        Preconditions: 0 <= length; length != self.length()
        Postconditions: if pre-self is a_0, a_1, ..., a_n then
        post-self is b_0, b_1, ..., b_m with
        - n == pref-self.length() - 1
        - m == length - 1
        - b_i == a_i for every i from 0 to min(n, m)
        - b_i == None for every i from min(m, n) + 1 to m
        """
        new_array = [None] * length
        for index in range(0, min(length, self.length())):
            new_array[index] = self.items[index]
        self.items = new_array
