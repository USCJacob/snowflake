from typing import List
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        n = len(s)
        maxL = max((len(w) for w in wordSet), default=0)

        @lru_cache(None)
        def dfs(i: int) -> List[str]:
            if i == n:
                return [""]  # 空串表示“后面没有词了”
            res = []
            # 枚举下一段单词 s[i:j]
            for j in range(i + 1, min(n, i + maxL) + 1):
                w = s[i:j]
                if w in wordSet:
                    for tail in dfs(j):
                        res.append(w if tail == "" else w + " " + tail)
            return res

        return dfs(0)
