class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetings.sort()
        used = []
        count = [0] * n
        available = [i for i in range(n)]
        heapq.heapify(available)
        for start, end in meetings:
            while used and used[0][0] <= start:
                _,room = heapq.heappop(used)
                heapq.heappush(available, room)
            if not available:
                end_time, room = heapq.heappop(used)
                end = end_time + (end-start)
                heapq.heappush(available, room)
            room =heapq.heappop(available)
            heapq.heappush(used,(end,room))
            count[room]+=1

        return count.index(max(count))