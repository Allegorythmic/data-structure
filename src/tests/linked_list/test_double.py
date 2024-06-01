from datastruct.linked_list.double import DoublyLinkedList
import io
import sys
import pytest


def test_append():
    dll = DoublyLinkedList()
    dll.append("A")
    dll.append("B")
    dll.append("C")
    assert dll.head.data == "A"
    assert dll.head.next.data == "B"
    assert dll.head.next.next.data == "C"
    assert dll.head.next.prev.data == "A"
    assert dll.head.next.next.prev.data == "B"


def test_prepend():
    dll = DoublyLinkedList()
    dll.append("A")
    dll.append("B")
    dll.prepend("C")
    assert dll.head.data == "C"
    assert dll.head.next.data == "A"
    assert dll.head.next.next.data == "B"
    assert dll.head.next.prev.data == "C"
    assert dll.head.next.next.prev.data == "A"


def test_delete_value():
    dll = DoublyLinkedList()
    dll.append("A")
    dll.append("B")
    dll.append("C")
    dll.delete_value("B")
    assert dll.head.data == "A"
    assert dll.head.next.data == "C"
    assert dll.head.next.prev.data == "A"
    dll.delete_value("A")
    assert dll.head.data == "C"
    dll.delete_value("C")
    assert dll.head is None


def test_delete_non_existent_value():
    dll = DoublyLinkedList()
    dll.append("A")
    dll.delete_value("B")
    assert dll.head.data == "A"


def test_delete_empty_list():
    dll = DoublyLinkedList()
    dll.delete_value("A")
    assert dll.head == None


def test_print_list():
    dll = DoublyLinkedList()
    dll.append("A")
    dll.append("B")
    dll.append("C")

    captured_output = io.StringIO()
    sys.stdout = captured_output
    dll.print_list()
    sys.stdout = sys.__stdout__

    assert captured_output.getvalue().strip() == "A <-> B <-> C <-> None"


def test_print_list_without_value():
    sll = DoublyLinkedList()
    sll.append(None)

    captured_output = io.StringIO()
    sys.stdout = captured_output
    sll.print_list()
    sys.stdout = sys.__stdout__

    assert captured_output.getvalue().strip() == "None"
