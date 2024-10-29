#creation and insertion of linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def Print_list(head):
    curr = head
    while curr is not None:
        print(curr.data)
        curr = curr.next

head = Node(2)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(5)
Print_list(head)

# print(head.data) 
# print(head.next.data) 
# print(head.next.next.data) 
# print(head.next.next.next.data) 