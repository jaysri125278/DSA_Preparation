class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def insert_at_position(pos, data, head):
    new_node = Node(data)

    if pos == 1:
        new_node.next = head
        head = new_node
        return head
    
    curr = head
    for _ in range(1, pos-1):
        if curr is None:
            break
        curr = curr.next

    if curr is None:
        print("position is out of bounds")
        return head

    new_node.next = curr.next
    curr.next = new_node

    return head


def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data)
        curr = curr.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(4)
head.next.next.next = Node(5)

pos = 3
data = 3
new_list = insert_at_position(pos, data, head)
print_list(new_list)

