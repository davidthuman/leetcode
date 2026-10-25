"""
Accepted
103 / 103 testcases passed
David Thuman submitted at Oct 24, 2026 19:43

Runtime 0 ms Beats 100.00%

Memory 19.44 MB Beats 23.33%
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        track = []
        for c in s:
            match c:
                case ")":
                    if len(track) == 0:
                        return False
                    if track[-1] == "(":
                        track.pop()
                    else:
                        return False
                case "}":
                    if len(track) == 0:
                        return False
                    if track[-1] == "{":
                        track.pop()
                    else:
                        return False
                case "]":
                    if len(track) == 0:
                        return False
                    if track[-1] == "[":
                        track.pop()
                    else:
                        return False
                case _:
                    track.append(c)
        if len(track) != 0:
            return False
        return True
