import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
         # compare the value passed into the insert function to self.value
        if value < self.value:
          # go to the left
          # if there's something there, do something
          # if there's nothing there, do something else
          # if there's nothing there
          if self.left is None:
            self.left = BinarySearchTree(value)
          # if there's something there
          else:
            # call the insert function, but on the node/value that's on the left
            self.left.insert(value)
        else:
          # go to the right
          if self.right is None:
            self.right = BinarySearchTree(value)
          else:
            self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)
        # if target < self.value or target > self.value:
        #     if target == self.left or self.right:
        #         return True
        #     else:
        #         if self.left is None and self.right is None:
        #             return False

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

     # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        # stack = Stack()

        # stack.push(node)
        # while stack.len() > 0:
          # current_node = stack.pop()
          # print(current_node)
        # if node is None:
          # return
        if node.left:
          self.left.in_order_print(node.left)
        print(node.value)
        if node.right:
          self.right.in_order_print(node.right)

        #   if stack.size == 0:
        #     return
        # return

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)

        while queue.size > 0:

          current_node = queue.dequeue()
          if current_node.left:
            queue.enqueue(current_node.left)
          if current_node.right:
            queue.enqueue(current_node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.size > 0:
          current_node = stack.pop()

        print(current_node)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
