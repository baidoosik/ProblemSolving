class Node:
    def __init__(self, val, node=None):
        self.val = val
        self.next = node


def remove_mid_node_without_access_head(node: Node):
    if node is None or node.next is None:
        raise Exception("this is not mid node")

    node.val = node.next.val
    node.next = node.next.next
