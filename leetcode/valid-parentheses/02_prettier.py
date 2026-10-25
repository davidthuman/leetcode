"""
Accepted
103 / 103 testcases passed
David Thuman submitted at Oct 24, 2026 19:49

Runtime 1 ms Beats 45.90%

Memory 19.20 MB Beats 62.25%
"""

class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 == 1:
            return False
        track = []

        left = ["(", "{", "["]
        right = [")", "}", "]"]
        mapping = dict(zip(right, left))

        for c in s:
            if c in left:
                track.append(c)
            else:
                if len(track) == 0:
                    return False
                if track[-1] == mapping[c]:
                    track.pop()
                else:
                    return False

        if len(track) != 0:
            return False
            
        return True
