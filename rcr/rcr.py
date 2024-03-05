from collections import Counter
from rcr.node import Node, NodesHeap


def build_rcr_tree(initial_trees):
    trees = initial_trees

    while not len(trees) == 1:
        node_0 = trees.pop()
        node_1 = trees.pop()

        new_node = combine_nodes(node_0, node_1)

        trees.push(new_node)

    return trees.pop()


def get_initial_trees(log: list[str]):
    trees = [
        Node(value=command, freq=count)
        for command, count in sorted(Counter(log).items(), key=lambda x: x[1])
    ]
    return NodesHeap(trees)


def combine_nodes(node_0, node_1):
    node_0.code = "0"
    node_1.code = "1"
    return Node(
        value=node_0.value + node_1.value,
        freq=node_0.freq + node_1.freq,
        left=node_0,
        right=node_1,
    )


def get_leaf_codes(root: Node):
    if root is None:
        return []

    result = []
    dfs(root, [], result)
    return result


def dfs(node: Node, path: list, result: list):
    if node is None:
        return
    path.append(node.code or "")
    if node.is_leaf():
        result.append((node.value, path[:]))
    else:
        dfs(node.left, path, result)
        dfs(node.right, path, result)
    path.pop()
