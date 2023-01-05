# Doubly Linked List

class Node:
    def __init__(self, value, nextNode, prevNode):
        self.value = value
        self.nextNode = nextNode
        self.prevNode = prevNode

if __name__ == "__main__":
    Node_1 = Node(1, None, None)
    Node_2 = Node(2, None, None)
    Node_3 = Node(3, None, None)
    Node_2.nextNode(Node_1)
    Node_3.nextNode(Node_2)
    Node_1.prevNode(Node_2)
    Node_2.prevNode(Node_3)
    Node_3.prevNode(None)
    print()

    # None <-> 3 <-> 2 <-> 1(head) <-> None
    # next --> 
    # previous <-- 

