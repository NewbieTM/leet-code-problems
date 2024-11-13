#https://github.com/NewbieTM/leet-code-problems/new/main/Sliding%20Window
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''

        t_count = {}
        for el in t:
            t_count[el] = t_count.get(el, 0) + 1

        required = len(t_count)
        formed = 0
        window_count = {}
        l, r = 0, 0
        min_len = float('inf')
        min_window = ""

        while r < len(s):
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1

            if char in t_count and window_count[char] == t_count[char]:
                formed += 1

            while l <= r and formed == required:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    min_window = s[l:r + 1]

                left_char = s[l]
                window_count[left_char] -= 1
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    formed -= 1
                l += 1

            r += 1

        return min_window
