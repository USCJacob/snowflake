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



from functools import lru_cache

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_deletions_height_at_most_k(root: TreeNode, k: int):
    """
    不考虑“删更深优先”的 tie-break：
    返回 (min_delete_count, deleted_set)
    """
    if not root:
        return 0, set()

    # 统计总节点数
    def count_nodes(u):
        if not u:
            return 0
        return 1 + count_nodes(u.left) + count_nodes(u.right)

    N = count_nodes(root)

    @lru_cache(None)
    def dp(u, r):
        if not u:
            return 0
        # delete u
        best = dp(u.left, r) + dp(u.right, r)
        # keep u
        if r >= 1:
            best = max(best, 1 + dp(u.left, r-1) + dp(u.right, r-1))
        return best

    kept = dp(root, k)
    min_del = N - kept

    deleted = set()

    def reconstruct(u, r):
        if not u:
            return

        del_score = dp(u.left, r) + dp(u.right, r)
        keep_score = -1
        if r >= 1:
            keep_score = 1 + dp(u.left, r-1) + dp(u.right, r-1)

        # 平手随便选一个；这里默认“能留就留”
        if keep_score >= del_score and r >= 1:
            reconstruct(u.left, r-1)
            reconstruct(u.right, r-1)
        else:
            deleted.add(u)
            reconstruct(u.left, r)
            reconstruct(u.right, r)

    reconstruct(root, k)
    return min_del, deleted

