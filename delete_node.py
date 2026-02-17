class Node:
    def __init__(self, idx):
        self.id = idx
        self.children = []

def delete_node(delete_list):
    delete_list = set(delete_list)
    best_height = -1
    def dfs(u, d, removed):
        nonlocal best_height
        deleted = (u in delete_list)

        if not deleted:
            now_height = d - removed
            best_height = max(best_height, now_height)

        removed = removed + 1 if deleted else removed

        for c in u.children:
            dfs(c, d + 1, removed)


    dfs(self.root, 0, 0)
