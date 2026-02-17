from typing import List
import collections

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        # build graph
        g = collections.defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        self.ans = 0

        def dfs(u: int, parent: int) -> int:
            """
            return: longest downward path length (in edges) starting from u and going into its subtree
            side effect: update self.ans as the best diameter seen so far (in edges)
            """
            best1 = best2 = 0  # top-2 longest child depths (in edges)

            for v in g[u]:
                if v == parent:
                    continue
                depth = dfs(v, u) + 1  # edge u-v + child's downward depth
                if depth > best1:
                    best2 = best1
                    best1 = depth
                elif depth > best2:
                    best2 = depth

            # diameter passing through u uses the two longest downward chains
            self.ans = max(self.ans, best1 + best2)
            return best1

        # pick any existing node as root (edges might not include 0)
        root = edges[0][0] if edges else 0
        dfs(root, -1)
        return self.ans
