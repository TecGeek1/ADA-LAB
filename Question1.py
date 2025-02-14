
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None 

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node 
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node   

 
    def print_forward(self, node):
        if node is None:
            return
        print(node.data, end=" ")  
        self.print_forward(node.next) 

   
    def print_reverse(self, node):
        if node is None:
            return
        self.print_reverse(node.next)  
        print(node.data, end=" ")  

if __name__ == "__main__":
    ll = LinkedList()  

    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.append(50)

   
    print("Forward Order:")
    ll.print_forward(ll.head)
    print()

  
    print("Reverse Order:")
    ll.print_reverse(ll.head)
    print()
