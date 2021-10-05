
class Tree:
    """A rooted binary tree"""
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

def is_empty(tree: Tree) -> bool:
    """Return True if and only if tree is empty."""
    return tree.root == tree.left == tree.right == None

def join(item: object, left: Tree, right: Tree) -> Tree:
    """Return a tree with the given root and subtrees."""
    tree = Tree()
    tree.root = item
    tree.left = left
    tree.right = right
    return tree

EMPTY = Tree()
THREE = join(3, EMPTY, EMPTY)
FOUR = join(4, EMPTY, EMPTY)
FIVE = join(5, EMPTY, EMPTY)
SIX = join(6, EMPTY, EMPTY)

TPM = join('*', join('+', THREE, FOUR), join('-', FIVE, SIX)) # (3+4)*(5-6)
PMT = join('+', THREE, join('-', join('*', FOUR, FIVE), SIX)) # 3+((4*5)-6)
MPT = join('-', join('+', THREE, join('*', FOUR, FIVE)), SIX) # (3+(4*5))-6

def is_leaf(tree: Tree) -> bool:
    """Return True if and only if the tree is a single leaf."""
    return not is_empty(tree) and is_empty(tree.left) and is_empty(tree.right)

def size(tree: Tree) -> int:
    """Return the number of nodes in tree."""
    if is_empty(tree):
        return 0
    else:
        return size(tree.left) + size(tree.right) + 1
