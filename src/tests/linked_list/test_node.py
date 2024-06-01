from datastruct.linked_list.node import Node


def test_node_initialization():
    node = Node("A")
    assert node.data == "A"
    assert node.next is None
    assert node.prev is None


def test_node_repr():
    node = Node("A")
    assert repr(node) == "Node(A)"


def test_node_next():
    node1 = Node("A")
    node2 = Node("B")
    node1.next = node2
    assert node1.next == node2
    assert node1.next.data == "B"


def test_node_prev():
    node1 = Node("A")
    node2 = Node("B")
    node2.prev = node1
    assert node2.prev == node1
    assert node2.prev.data == "A"
