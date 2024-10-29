#insertion at front of linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertion_at_front(head, data):
    new_data = Node(data)
    new_data.next = head
    return new_data

def Print_list(head):
    curr = head
    while curr is not None:
        print(curr.data)
        curr = curr.next

head = Node(2)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(5)

new_data_to_be_added = 1
new_linked_list = insertion_at_front(head, new_data_to_be_added)

Print_list(new_linked_list)


