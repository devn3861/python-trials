# Binary Tree
#
#                  4 
#                /   \ 
#              2      6
#             / \    / \ 
#            1   3  5   7
#  <--L R -->
#   In-order - 1, 2, 3, 4, 5, 6, 7
#   Pre-order - 4, 2, 1, 3, 6, 5, 7
#   Post-order - 1, 3, 2, 5, 7, 6, 4

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

# Recursive Function
def printTree(node):
    if not(node):
        return None
    else:
        printTree(node.left)
        print(node.value)
        printTree(node.right)

if __name__ == "__main__":
    binTree = Node(4, Node(2, Node(1, None, None), Node(3, None, None)), Node(6, Node(5, None, None), Node(7, None, None)))
    printTree(binTree)


