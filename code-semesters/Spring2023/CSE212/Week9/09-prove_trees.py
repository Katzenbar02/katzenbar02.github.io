"""
CSE212 
(c) BYU-Idaho
09-Prove - Problems

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

class BST:
    """
    Implement the Binary Search Tree (BST) data structure.  The Node 
    class below is an inner class.  An inner class means that its real 
    name is related to the outer class.  To create a Node object, we will 
    need to specify BST.Node
    """

    class Node:
        """
        Each node of the BST will have data and links to the 
        left and right sub-tree. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, data):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    ###################
    # Start Problem 1 #
    ###################
    def _insert(self, data, node):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        Hint: Update the _insert function of the BST class to only allow unique values to be added to the tree (thus creating a sorted set).
        The _insert function is already written to correctly insert values into the BST.
        However, the current implementation will cause duplicate values to be added to the tree.
        """
        if data == node.data:
            return # Already in the tree, so do nothing
        
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)
    
    #################
    # End Problem 1 #
    #################

    def __contains__(self, data):
        """ 
        Checks if data is in the BST.  This function
        supports the ability to use the 'in' keyword:

        if 5 in my_bst:
            ("5 is in the bst")

        """
        return self._contains(data, self.root)  # Start at the root

    ###################
    # Start Problem 2 #
    ###################
    def _contains(self, data, node):
        """
        This funciton will search for a node that contains
        'data'.  The current sub-tree being search is 
        represented by 'node'.  This function is intended
        to be called the first time by the __contains__ function.
        Hint: Implement the _contains function in the BST class. 
        This function is called by the __contains__ function to search for a value in the BST. 
        The __contains__ function allows you to write code using the in operator like the following:	
        if 5 in my_bst:
	    print("5 is in the bst")
		If the value is found, the True should be returned; otherwise return False.
        Hint: study the _insert function. You will need to use recursion to solve this problem.
            """
        if node is None:
            return False  # Reached a leaf node without finding the value

        if data == node.data:
            return True  # Found the value in the current node

        if data < node.data:
            return self._contains(data, node.left)  # Search in the left sub-tree
        else:
            return self._contains(data, node.right)  # Search in the right sub-tree

    #################
    # End Problem 2 #
    #################

    def __iter__(self):
        """
        Perform a forward traversal (in order traversal) starting from 
	    the root of the BST.  This is called a generator function.
        This function is called when a loop	is performed:

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        """
        Does a forward traversal (in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the left
        side (thus getting the smaller numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the right side (thus getting the larger numbers last).

        The use of the 'yield' will allow this function to support loops
        like:

        for value in my_bst:
            print(value)

        The keyword 'yield' will return the value for the 'for' loop to
	    use.  When the 'for' loop wants to get the next value, the code in
	    this function will start back up where the last 'yield' returned a 
	    value.  The keyword 'yield from' is used when our generator function
        needs to call another function for which a `yield` will be called.  
        In other words, the `yield` is delegated by the generator function
        to another function.

        This function is intended to be called the first time by 
        the __iter__ function.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
    def __reversed__(self):
        """
        Perform a formward traversal (in order traversal) starting from 
        the root of the BST.  This function is called when a the 
        reversed function is called and is frequently used with a for
        loop.

        for value in reversed(my_bst):
            print(value)

        """        
        yield from self._traverse_backward(self.root)  # Start at the root

    ###################
    # Start Problem 3 #
    ###################
    def _traverse_backward(self, node):
        """
        Does a backwards traversal (reverse in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the right
        side (thus getting the larger numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the left side (thus getting the smaller numbers last).

        This function is intended to be called the first time by 
        the __reversed__ function.    
        Hint: Implement the _traverse_backward function in the BST class. 
        This function is called by the __reversed__ function to loop through the tree backwards (largest value down to the smallest value). 
        The __reversed__ function allows you to write code using the reversed function like the following:				
        for value in reversed(my_bst):
            print(value)
		Hint: study the _traverse_forward function to see how traversing forward is done using the yield keyword.    
        """    
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)

    #################
    # End Problem 3 #
    #################

    def get_height(self):
        """
        Determine the height of the BST.  Note that an empty tree
        will have a height of 0 and a tree with one item (root) will
        have a height of 1.
        
        If the tree is empty, then return 0.  Otherwise, call 
        _get_height on the root which will recursively determine the 
        height of the tree.
        """
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root

    ###################
    # Start Problem 4 #
    ###################
    def _get_height(self, node):
        """
        Determine the height of the BST.  The height of a sub-tree 
        (represented by 'node') is 1 plus the height of either the 
        left sub-tree or the right sub-tree (whichever one is bigger).

        This function intended to be called the first time by 
        get_height.
        Hint: Implement the _get_height function to get the height of the BST. 
        The height of any tree (or subtree) is defined as one plus the height of either the left subtree or the right subtree (whichever one is bigger). 
        If the BST has only the root node, then this would be 1 plus the maximum height of either subtree which would be 0. 
        Therefore, the height of a BST with only the root node is 1. 
        You will need to use recursion to solve this problem.
        """
        if node is None:
            return 0  # Reached a leaf node, height is 0

        left_height = self._get_height(node.left)  # Height of the left sub-tree
        right_height = self._get_height(node.right)  # Height of the right sub-tree

        return 1 + max(left_height, right_height)  # Height is 1 plus the maximum of left and right heights

    #################
    # End Problem 4 #
    #################


# NOTE: Functions below are not part of the BST class above. 

def create_bst_from_sorted_list(sorted_list):
    """
    Given a sorted list (sorted_list), create a balanced BST.  If 
    the values in the sorted_list were inserted in order from left
    to right into the BST, then it would resemble a linked list (unbalanced). 
    To get a balanced BST, the _insert_middle function is called to 
    find the middle item in the list to add first to the BST.  The 
    _insert_middle function takes the whole list but also takes a 
    range (first to last) to consider.  For the first call, the full 
    range of 0 to len()-1 used.
    """
    bst = BST()  # Create an empty BST to start with 
    _insert_middle(sorted_list, 0, len(sorted_list)-1, bst)
    return bst

###################
# Start Problem 5 #
###################
def _insert_middle(sorted_list, first, last, bst):
    """
    This function will attempt to insert the item in the middle
    of 'sorted_list' into the 'bst' tree.  The middle is 
    determined by using indicies represented by 'first' and 'last'.
    For example, if the function was called on:

    sorted_list = [10, 20, 30, 40, 50, 60]
    first = 0
    last = 5

    then the value 30 (index 2 which is the middle) would be added 
    to the 'bst' (the insert function above can be used to do this).   

    Subsequent recursive calls are made to insert the middle from the values 
    before 30 and the values after 30.  If done correctly, the order
    in which values are added (which results in a balanced bst) will be:

    30, 10, 20, 50, 40, 60

    This function is intended to be called the first time by 
    create_bst_from_sorted_list.

    The purpose for having the first and last parameters is so that we do 
    not need to create new sublists when we make recursive calls.  Avoid 
    using list slicing to create sublists to solve this problem.
    Hint: Implement the _insert_middle function (note this function is defined outside the BST class) 
    so that the create_bst_from_sorted_list function can successfully create a balanced BST from a sorted list of values. 
    If we looped through the list of sorted values and added them (using the insert function in the BST class) one at a time in order, 
    then the resulting BST would look like a linked list. This is not desirable because it results in O(n) instead of O(log n).
    To achieve a balanced BST, the _insert_middle function should find the middle of the list 
    (or sub-list ... notice that the function takes a first and last value to keep track of what part of the list you are working with) 
    and add it to the BST. After adding the middle value, then the middle value from the first half and the middle value from the second half should be added. 
    This process (which is recursive) will result in a balanced BST.
    The purpose for having the first and last parameters is so that we do not need to create new sublists when we make recursive calls. 
    Avoid using list slicing to create sublists to solve this problem.
    Please note we are not using balanced algorithms like AVL or red/black trees in this problem.

    """
    if first > last:
        return

    mid = (first + last) // 2  # Calculate the middle index

    bst.insert(sorted_list[mid])  # Insert the middle value into the BST

    # Recursively insert the middle values from the first and second halves
    _insert_middle(sorted_list, first, mid - 1, bst)  # First half
    _insert_middle(sorted_list, mid + 1, last, bst)  # Second half

#################
# End Problem 5 #
#################


# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 1 TESTS ===========")
tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
# After implementing 'no duplicates' rule,
# this next insert will have no effect on the tree.
tree.insert(7)  
tree.insert(4)
tree.insert(10)
tree.insert(1)
tree.insert(6)
for x in tree:
    print(x)  # 1, 3, 4, 5, 6, 7, 10

print("\n=========== PROBLEM 2 TESTS ===========")
print(3 in tree) # True
print(2 in tree) # False
print(7 in tree) # True
print(6 in tree) # True
print(9 in tree) # False

print("\n=========== PROBLEM 3 TESTS ===========")
for x in reversed(tree):
    print(x)  # 10, 7, 6, 5, 4, 3, 1

print("\n=========== PROBLEM 4 TESTS ===========")
print(tree.get_height()) # 3
tree.insert(6)
print(tree.get_height()) # 3
tree.insert(12)
print(tree.get_height()) # 4


print("\n=========== PROBLEM 5 TESTS ===========")
tree1 = create_bst_from_sorted_list([10, 20, 30, 40, 50, 60])
tree2 = create_bst_from_sorted_list([x for x in range(127)]) # 2^7 - 1 nodes
tree3 = create_bst_from_sorted_list([x for x in range(128)]) # 2^7 nodes
tree4 = create_bst_from_sorted_list([42])
tree5 = create_bst_from_sorted_list([])
print(tree1.get_height()) # 3
print(tree2.get_height()) # 7 .. any higher and its not balanced
print(tree3.get_height()) # 8 .. any higher and its not balanced
print(tree4.get_height()) # 1
print(tree5.get_height()) # 0



