# Singly Linked List

class Node:
    def __init__(self, value, nextNode):
        self.value = value
        self.nextNode = nextNode

if __name__ == "__main__":
    myHeadNode = Node(1, None) # Node object
    nextNode = Node(2, myHeadNode)
    print(nextNode.next.value)

    ListNode = Node(1, Node(2, Node(3, None)))
    
    # 3 -> 2 -> 1 -> None

