class Solution:
    def countMentions(self, n, events):
        res = [0] * n
        online = [0] * n
        all_count = 0

        # sort
        events.sort(key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))

        for event in events:
            if event[0] == "OFFLINE":
                online[int(event[2])] = int(event[1]) + 60
            else:
                time = int(event[1])
                if event[2] == "ALL":
                    all_count += 1
                elif event[2] != "HERE":
                    i = 2
                    s = event[2]
                    while i < len(s):
                        id_str = ""
                        while i < len(s) and s[i] != ' ':
                            id_str += s[i]
                            i += 1
                        idd = int(id_str)
                        res[idd] += 1
                        i += 3
                else:
                    for i in range(n):
                        if online[i] <= time:
                            res[i] += 1

        for i in range(n):
            res[i] += all_count

        return res