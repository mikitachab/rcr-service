from .rcr import get_initial_trees, build_rcr_tree, get_leaf_codes


def command_log_to_rcr_map(log: list[str]):
    initial_trees = get_initial_trees(log)
    rcr_tree = build_rcr_tree(initial_trees)
    leaf_codes = get_leaf_codes(rcr_tree)

    return {command: "".join(code) for command, code in leaf_codes}
