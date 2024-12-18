class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_list(head):
    curr = head 
    prev = None

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def Print(head):
    curr = head
    while curr is not None:
        print(curr.data)
        curr = curr.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

reversed = reverse_list(head)
Print(reversed)

