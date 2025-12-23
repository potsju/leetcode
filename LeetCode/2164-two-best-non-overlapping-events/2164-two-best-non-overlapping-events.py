import heapq

class Solution(object):
    def maxTwoEvents(self, events):
        events.sort()  # sort by start time
        heap = []      # (end, value)
        best_so_far = 0
        ans = 0

        for start, end, value in events:
            # remove events that ended before current starts
            while heap and heap[0][0] < start:
                _, v = heapq.heappop(heap)
                best_so_far = max(best_so_far, v)

            # combine current event with best previous
            ans = max(ans, best_so_far + value)

            # push current event
            heapq.heappush(heap, (end, value))

        return ans
