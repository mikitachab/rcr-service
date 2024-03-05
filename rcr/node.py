from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    value: str
    freq: int
    x: str | None = None
    code: str | None = None
    left: Optional["Node"] = None
    right: Optional["Node"] = None

    def is_leaf(self):
        return self.left is None and self.right is None

    def __hash__(self):
        return hash(self.value)

    def __lt__(self, other):
        return self.freq < other.freq


class NodesHeap:
    """
    not using built in heapq to ensure stable sorting
    """

    def __init__(self, nodes):
        self.nodes = [(node.freq, node) for node in nodes]

    def push(self, node):
        self.nodes.append((node.freq, node))
        self.nodes.sort()

    def pop(self):
        return self.nodes.pop(0)[1]

    def __len__(self):
        return len(self.nodes)

    def __repr__(self):
        return repr(self.nodes)
