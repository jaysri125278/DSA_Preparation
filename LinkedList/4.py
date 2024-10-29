#Insertion at the end
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_end(head, new_data):
    if head is None:
        return new_data
    else:
        last = head
        while last.next:
            last = last.next

        last.next = new_data
    return head

def Print_list(head):
    curr = head
    while curr is not None:
        print(curr.data)
        curr = curr.next

input = "1 2 3 4"
numbers = list(map(int, input.split()))
head = None
for num in numbers:
    new_data = Node(num)
    head = insert_at_end(head, new_data)

Print_list(head)





