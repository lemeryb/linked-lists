# Title: Linked Lists
# Author: Benjamin Lemery
# Date: 2/21/2020
# This program demonstrates how to create, and display linked lists.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Function that creates a new node
    def create_new_node(self, newdata):
        new_node = Node(newdata)
        # Gets the current node and points it to the next node if it exists
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    # Print the linked list

    def list_print(self):
        printval = self.head
        print("4 nodes have been created. Its values are: ")
        while printval is not None:
            print("Node data value: " + printval.data)
           # print(printval.data)
            printval = printval.next
