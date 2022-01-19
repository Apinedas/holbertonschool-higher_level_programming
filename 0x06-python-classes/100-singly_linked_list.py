#!/usr/bin/python3
""" Node: Class for a node in a singly linked list """

class Node:
    """ Init method to instantiate """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
    
    @property
    def data(self):
        """ Data - Node's int data """
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, int) is False:
            raise TypeError("data must be an integer")
        else:
            self._data = value

    @property
    def next_node(self):
        """ Next node - Node that follows the actual node """
        return self._next_node
    
    @next_node.setter
    def next_node(self, value):
        if isinstance(value, Node) is False and value != None:
                raise TypeError("next_node must be a Node object")
        else:
            self._next_node = value
    
"""  Singly linked list class """


class SinglyLinkedList:
    """ Init instantiate method """
    def __init__(self):
        self.__head = None

    """ Str method to print """
    def __str__(self):
        datalist = []
        actual_node = self._SinglyLinkedList__head
        while actual_node:
            datalist.append(str(actual_node.data))
            actual_node = actual_node.next_node
        return '\n'.join(datalist)
    
    """ Sorted Insert - inserts a new Node into the correct sorted
    position in the list (increasing order) """
    def sorted_insert(self, value):
        actual_node = self._SinglyLinkedList__head
        if not actual_node:
            new_node = Node(value, None)
            self._SinglyLinkedList__head = new_node
        elif value < actual_node.data:
            new_node = Node(value, actual_node)
            self._SinglyLinkedList__head = new_node
        else:
            while (actual_node.next_node):
                if value < actual_node.next_node.data:
                    break
                else:
                    actual_node = actual_node.next_node
            new_node = Node(value, actual_node.next_node)
            actual_node.next_node = new_node
