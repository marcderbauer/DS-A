from abc import ABC, abstractmethod
from email import header
class Node:
    """
    Simple class representing a Node
    value: value of the node
    """
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return str(self.value)


class LinkedList(ABC):
    """
    Once more classes are added, this will be the parent class
    """
    def __init__(self) -> None:
        super.__init__()




class SLL(LinkedList):
    """
    Class representing a singly linked list
    head: first element in the list
    """

    def __init__(self, head) -> None:
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


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    n1.next = n2
    n2.next = n3

    sll = SLL(n1)
    sll.push(0)
    sll.traverse()

    sll.insert_after(n2, 2.5)
    sll.append(4)
    sll.delete_middle(20)
    # sll.insert_after(None, "23")