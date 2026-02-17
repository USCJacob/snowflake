from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        g = defaultdict(list)
        indeg = [0] * (n + 1)

        for u, v in relations:
            g[u].append(v)
            indeg[v] += 1

        q = deque(i for i in range(1, n + 1) if indeg[i] == 0)

        semesters = 0
        taken = 0

        while q:
            semesters += 1
            for _ in range(len(q)):          # one semester = one BFS layer
                u = q.popleft()
                taken += 1
                for v in g[u]:
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        q.append(v)

        return semesters if taken == n else -1



from typing import List
from functools import lru_cache

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        # pre[i] = bitmask of prerequisites for course i (0-indexed)
        pre = [0] * n
        for u, v in relations:
            u -= 1
            v -= 1
            pre[v] |= 1 << u

        full = (1 << n) - 1

        @lru_cache(None)
        def dp(mask: int) -> int:
            if mask == full:
                return 0

            # courses available to take now: not taken + prerequisites satisfied
            avail = 0
            for i in range(n):
                bit = 1 << i
                if mask & bit:
                    continue
                if (pre[i] & mask) == pre[i]:
                    avail |= bit

            # If we can take all available courses this semester
            if avail.bit_count() <= k:
                return 1 + dp(mask | avail)

            # Otherwise, choose any submask of avail with exactly k courses
            best = 10**9
            sub = avail
            while sub:
                # iterate all submasks; keep only size k
                if sub.bit_count() == k:
                    best = min(best, 1 + dp(mask | sub))
                sub = (sub - 1) & avail

            return best

        return dp(0)
