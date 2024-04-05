# initialize the node
class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

# class for doubly linked list
class DoublyLinkedList:
    def __init__(self):
        self.start_node = None
    
    # insert element to empty list
    def insert_to_empty_list(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("the list is not empty")
    
    # insert element at the end
    def insert_to_end(self, data):
        # check if the list is empty
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        # iterate till the next reaches None
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n
    
    # delete the elements from the start
    def delete_at_start(self):
        if self.start_node is None:
            print("the linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_node.prev = None
    
    # delete the elements from the end
    def delete_at_end(self):
        # check if the list is empty
        if self.start_node is None:
            print("the linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None
    
    # traversing and display each element of the list
    def display(self):
        if self.start_node is None:
            print("the list is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print("element is:", n.item)
                n = n.next
            print("\n")

# create a new doubly linked list
new_doubly_linked_list = DoublyLinkedList()

# insert the element to empty list
new_doubly_linked_list.insert_to_empty_list(10)

# insert the element at the end
new_doubly_linked_list.insert_to_end(20)
new_doubly_linked_list.insert_to_end(30)
new_doubly_linked_list.insert_to_end(40)
new_doubly_linked_list.insert_to_end(50)
new_doubly_linked_list.insert_to_end(60)

# display data
new_doubly_linked_list.display()

# delete elements from start
new_doubly_linked_list.delete_at_start()

# delete elements from end
new_doubly_linked_list.delete_at_end()

# display data
new_doubly_linked_list.display()
                                                        
