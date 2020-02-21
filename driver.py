from main import *

# Initiate the Linked list and set the first head value
list = LinkedList()
list.head = Node("1")

# Using the create new node functions this will create a new node and link the lists
node_2 = list.create_new_node("2")
node_3 = list.create_new_node("3")
node_4 = list.create_new_node("4")


# Print the results after creating the new nodes.
list.list_print()

