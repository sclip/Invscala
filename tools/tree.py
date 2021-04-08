class Tree:
    def __init__(self, data, parent=None):
        self.data = data
        self.children = []
        self.parent = parent

    def add_child(self, child, parent=None):
        """
        Adds a child node to an existing node
        :param child: Can be either a Tree object or just the data required to create one
        :param parent: If left empty it will be self by default
        :return:
        """
        # We check if data or another Tree object is being passed in
        # If it's data we have to create the object ourselves
        if parent is None:
            parent = self
        if type(child) != Tree:
            parent.children.append(Tree(child, parent=parent))
        else:
            parent.children.append(child)

    def has_children(self) -> bool:
        if len(self.children) == 0:
            return False
        return True


def get_branch_items(start_node) -> list:
    """
    Get all the items in the branch above the start node, up to the root
    :param start_node: Node to start from
    :return: All the items parenting the start node
    """
    items = []

    def _get_parent_item(node):
        items.append(node.data)
        if node.parent is not None:
            _get_parent_item(node.parent)

    _get_parent_item(start_node)

    return items


def get_end_nodes(node):
    """
    Get all leaf/end nodes in a tree, or a branch of a tree
    :param node: Node to start from
    :return: End nodes in the tree
    """
    if not node.children:
        yield node

    for child in node.children:
        for end_node in get_end_nodes(child):
            yield end_node


def get_node_depth(node) -> int:
    if node.parent is None:
        return 0
    return get_node_depth(node.parent) + 1


def get_max_depth(node) -> int:
    if len(node.children) == 0:
        return 0
    return max(get_max_depth(n) for n in node.children) + 1


def get_nodes_at_depth(start_node, depth) -> list:
    """
    Get all nodes at a certain depth
    :param start_node: Node to look for children of
    :param depth: Depth to look for
    :return: All child nodes with the correct depth
    """
    if len(start_node.children) == 0:
        return []

    nodes = []

    def _append_child_nodes_at_depth(node):
        for child in node.children:
            if get_node_depth(child) == depth:
                nodes.append(child)
            _append_child_nodes_at_depth(child)

    _append_child_nodes_at_depth(start_node)

    return nodes
