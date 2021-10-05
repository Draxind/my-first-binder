class ArrayPriorityQueue:

    """A dynamic array implementation of a fair max-priority queue.

    Items with the same priority are retrieved in FIFO order.
    """

    def __init__(self):
        """Create a new empty priority queue."""
        self.pairs = []    # in ascending order of priority

    def length(self) -> int:
        """Return the number of items in the queue."""
        return len(self.pairs)

    def find_max(self) -> object:
        """Return the oldest item with the highest priority.

        Preconditions: self.length() > 0
        """
        return self.pairs[-1][1]

    def remove_max(self) -> None:
        """Remove the oldest item with the highest priority.

        Preconditions: self.length() > 0
        """
        self.pairs.pop(-1)

    def insert(self, item: object, priority: object) -> None:
        # question
        """Add item with the given priority to the queue.

        Preconditions:
        - priority is comparable to the priorities of all existing items
        """
        index = 0
        while index < self.length() and self.pairs[index][0] < priority:
            index = index + 1
        self.pairs.insert(index, (priority, item))
