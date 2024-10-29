#insertion after a specified key
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_after_key(head, key, data):
    new_data = Node(data)
    
    curr = head
    while curr is not None:
        if curr.data == key:
            break
        curr = curr.next

    new_data.next = curr.next
    curr.next = new_data

    return head

def Print_list(head):
    curr = head
    while curr is not None:
        print(curr.data)
        curr = curr.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(5)

key = 3
data = 4

new_linked_list = insert_after_key(head, key, data)

Print_list(new_linked_list)


