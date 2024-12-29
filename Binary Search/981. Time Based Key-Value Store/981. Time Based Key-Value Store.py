#https://leetcode.com/problems/time-based-key-value-store/description/
# Main idea of get function is to search for insert position (index) in array
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
        

