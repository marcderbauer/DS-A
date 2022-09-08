from abc import ABC, abstractmethod

class Node:
    """
    Simple class representing a Node
    value: value of the node
    """
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return str(self.value)


class LinkedList(ABC):
    """
    Once more classes are added, this will be the parent class
    """
    def __init__(self, head) -> None:
        self.head = head

    def __repr__(self) -> str:
        string = ""
        node = self.head
        while True:
            string = string + f"{str(node.value)} "
            if node.next:
                node = node.next
            else:
                break
        return string

    @abstractmethod
    def swap_keys(self, key1, key2):
        pass

class SLL(LinkedList):
    """
    Class representing a singly linked list
    head: first element in the list
    """

    def __init__(self, head) -> None:
        #TODO: make use of inheritance
        self.head = head
        self.tail = None
    
    def traverse(self, node=None):
        """
        Traverses the SLL and prints each node's value.
        If no node is given, will start at the beginning of the list.
        Automatically sets tail if non-existent
        node:   starting-point of the traversal
        """
        if not node:
            node = self.head

        print(node.value)
        if node.next:
            self.traverse(node.next)
        else:
            self.tail = node

    def __repr__(self) -> str:
        return super().__repr__()

    def push(self, new_data):
        """
        Add a new entry at the beginning of the list
        Time Complexity:    O(1)
        Auxliary Space:     O(1)

        new_data:   value to insert
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    

    def insert_after(self, prev_node, new_data):
        """
        Inserts a new node into the list after a specified node.
        Time Complexity:    O(N) -> TODO Why? Not iterating over list
        Auxiliary Space     O(1)

        prev_node:  previous node, which to insert the new node in after
        new_data:   value of new_node
        """
        assert prev_node is not None 
        
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

        print(f"Successfully inserted new node with value {new_data} after given previous node.")


    def append(self, new_data):
        """
        Inserts a new node at the end of the list.
        Time Complexity: O(N) -> TODO Can be optimized to O(1) by adding final node pointer
        Auxiliary Space: O(1)
        
        new_data:   value to insert at end of list
        """
        new_node = Node(new_data)
        if self.tail:
            final_node = self.tail
        else:
            if not self.head:
                self.head = new_node

            final_node = self.head
            while (final_node.next):
                final_node = final_node.next

        final_node.next = new_node
        self.tail = final_node.next

        print(f"Successfully appended new node with value {new_data} to list.")


    def search(self):
        """
        TODO: Implement
        -> Might fit better under algorithms?
        """
        pass


    def search_idx(self, index):
        """
        Traverses the linkedlist and returns the value of a node at a given index.
        """
        assert index >= 0
        counter = 0
        node = self.head
        while (True):
            if index == counter:
                return node
            else:
                counter += 1
                node = node.next


    def delete_beginning(self):
        """
        Deletes the first element from the linked list
        Time Complexity: O(1)
        Auxiliary Space: O(1) TODO: correct?
        """
        temp = self.head
        self.head = self.head.next
        del temp
        print(f"Deleted head. New head has value {self.head.value}")


    def delete_end(self):
        node = self.head
        while node.next != self.tail:
            node = node.next
        self.tail = node
        del node.next
        print(f"Deleted tail. New tail has value {self.tail.value}")


    def delete_middle(self, idx):
        """
        Deletes a note at a given index.
        idx:    index of the node to be deleted
        """
        temp = self.head
        prev = self.head

        for i in range(idx):
            if i == 0 and idx == 1:
                self.head = self.head.next
                del temp
            else:
                if i == idx - 1 and temp:
                    prev.next =  temp.next
                    del temp
                else:
                    prev = temp
                    if prev == None:
                        raise IndexError("Requested index is larger then the length of the list")
                    temp = temp.next

    def swap_keys(self, key1, key2):
        node1 = None
        node2 = None
        node1_prev = None
        node2_prev = None
        node_curr = self.head
        node_prev = self.head

        if key1 == key2:
            return

        # Find the nodes
        while True:
            # Assign keys to node if found
            if node_curr.value == key1:
                node1_prev = node_prev
                node1 = node_curr
            elif node_curr.value == key2:
                node2_prev = node_prev
                node2 = node_curr

            if node1 and node2:
                    break
            elif node_curr.next == None:
                missing = "Reached end of the list. Missing the following nodes:"
                if node1 == None:
                    missing = f"{missing} node1"
                if node2 == None:
                    missing = f"{missing} node2"
                print(missing)
                return None

            node_prev = node_curr
            node_curr = node_curr.next
        
        # Swap the nodes:
        node1_prev.next = node2
        node2_prev.next = node1
        
        node_curr = node1.next # Use as placeholder
        node1.next = node2.next
        node2.next = node_curr

        print(f"Sucessfully switched nodes of {key1}, {key2}")
class DLL(LinkedList):
    def __init__(self, head) -> None:
        self.tail = None
        super().__init__(head=head)
    
    def push(self, new_data):
        """
        Creates and inserts new object at beginning of list.
        new_data:   Data to be appended to DLL
        """
        new_node = Node(new_data)
        tmp = self.head
        new_node.next = tmp
        tmp.prev = new_node
        self.head = new_node

        print(f"Pushed new node with value {new_data} to beginning of ll.")
        
    def append(self, new_data):
        """
        Creates a new node for the data and appends it to the back of the DLL.
        new_data:   Data to be appended to DLL
        """
        new_node = Node(new_data)
        if self.tail:
            node = self.tail

        else:
            node = self.head
            while node.next:
                node = node.next

        node.next = new_node
        new_node.prev = node
        self.tail = new_node

        print(f"Appended new node with value {new_data}.")
    
    def delete_beginning(self):
        """
        Deletes the beginning node of the DLL.
        """
        temp = self.head
        self.head = temp.next
        self.head.prev = None
        del temp

        print(f"Deleted node at the beginning of the DLL.")
    
    def delete_end(self):
        """
        Deletes the last node of the DLL.
        """
        if self.tail:
            node = self.tail
        else:
            node = self.head
            while node.next:
                node = node.next
        self.tail = node.prev
        self.tail.next = None
        del node
        
        print(f"Deleted node at the end of the DLL.")
    

def test_sll():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    n1.next = n2
    n2.next = n3

    sll = SLL(n1)
    sll.push(0)
    sll.traverse()

    # sll.insert_after(n2, 2.5)
    sll.append(4)
    sll.swap_keys(1, 3)
    print(sll)
    # sll.delete_middle(20)
    # sll.insert_after(None, "23")
    #sll.swap_keys("a", "b")

def test_dll():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    dll = DLL(n1)
    dll.append(n2)
    dll.append(n3)


if __name__ == "__main__":
    test_sll()
    # test_dll()