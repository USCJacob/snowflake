from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # sort by end time
        intervals.sort(key=lambda x: x[1])

        end = intervals[0][1]
        keep = 1  # number of non-overlapping intervals we keep

        for s, e in intervals[1:]:
            if s >= end:          # no overlap
                keep += 1
                end = e

        return len(intervals) - keep




from bisect import bisect_right
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])  # sort by end
        ends = [e for _, e, _ in jobs]

        n = len(jobs)
        dp = [0] * (n + 1)  # dp[i]: best profit using first i jobs (jobs[0..i-1])

        for i in range(1, n + 1):
            s, e, p = jobs[i - 1]
            # j = number of jobs with end <= s  (so dp[j] is valid)
            j = bisect_right(ends, s)
            dp[i] = max(dp[i - 1], p + dp[j])

        return dp[n]




from typing import List
from bisect import bisect_left
from functools import lru_cache

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # sort by start time
        events.sort(key=lambda x: x[0])
        starts = [s for s, e, v in events]
        n = len(events)

        # precompute next index for each event
        nxt = [0] * n
        for i, (s, e, v) in enumerate(events):
            nxt[i] = bisect_left(starts, e + 1)  # first start >= e+1 => start > e

        @lru_cache(None)
        def dp(i: int, t: int) -> int:
            if i == n or t == 0:
                return 0
            # skip i
            best = dp(i + 1, t)
            # take i
            best = max(best, events[i][2] + dp(nxt[i], t - 1))
            return best

        return dp(0, k)
