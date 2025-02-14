class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
def merge_sorted_lists(l1, l2):
    dummy = Node()
    current = dummy
    while l1 is not None and l2 is not None:
        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    if l1 is not None:
        current.next = l1
    elif l2 is not None:
        current.next = l2
    return dummy.next
def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")
def create_linked_list(values):
    head = None
    for value in reversed(values):                  
        new_node = Node(value)
        new_node.next = head
        head = new_node
    return head

l1 = create_linked_list([1, 3, 5, 7])
l2 = create_linked_list([2, 4, 6, 8])

print("List 1:")
print_list(l1)
print("List 2:")
print_list(l2)

merged_list = merge_sorted_lists(l1, l2)
print("Merged List:")
print_list(merged_list)
