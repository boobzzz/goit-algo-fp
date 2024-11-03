import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="#000000"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(9, 6))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def show_dfs(node):
    stack = [node]
    order = 0

    while stack:
        current = stack.pop()
        if current:
            hex_color = "#{:02x}{:02x}{:02x}".format(order % 256, 0, 128)
            current.color = hex_color
            order += 32
            stack.append(current.right)
            stack.append(current.left)
    draw_tree(node, 'dfs_tree')


def show_bfs(node):
    queue = [node]
    order = 0

    while queue:
        current = queue.pop(0)
        if current:
            hex_color = "#{:02x}{:02x}{:02x}".format(order % 256, 0, 128)
            current.color = hex_color
            order += 32
            queue.append(current.left)
            queue.append(current.right)
    draw_tree(node, 'bfs_tree')


root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

show_dfs(root)

root.color = "#000000"
root.left.color = "#000000"
root.left.left.color = "#000000"
root.left.right.color = "#000000"
root.right.color = "#000000"
root.right.left.color = "#000000"

show_bfs(root)
