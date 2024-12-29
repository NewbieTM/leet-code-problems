#https://leetcode.com/problems/time-based-key-value-store/description/
# Main idea is to find the index in the array by key, in which we wanna insert out given timestamp
class TimeMap:

    def __init__(self):
        self.timemap = {}
        self.sorted_times = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[(key,timestamp)] = value
        self.sorted_times[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.sorted_times:
            return ''

        times_for_key = self.sorted_times[key]
        l, r = 0, len(times_for_key)
        while l < r:
            mid = (l + r) // 2
            if times_for_key[mid] < timestamp:
                l = mid + 1
            else:
                r = mid
           
        if l < len(times_for_key) and times_for_key[l] == timestamp:
            return self.timemap[(key, times_for_key[l])]
        elif l > 0:
            return self.timemap.get((key, times_for_key[l - 1]), '')
        else:
            return ''
        

# OR (LESS MEMORY USAGE)

class TimeMap:

    def __init__(self):
        self.sorted_times = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.sorted_times[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        v_and_t_per_key = self.sorted_times.get(key,[])
        
        l,r = 0, len(v_and_t_per_key) - 1
        while l <= r:
            mid = (l + r) // 2
            if v_and_t_per_key[mid][1] <= timestamp:
                res = v_and_t_per_key[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res


