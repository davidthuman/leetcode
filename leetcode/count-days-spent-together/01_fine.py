"""
Accepted
51 / 51 testcases passed
David Thuman submitted at Oct 24, 2026 20:39

Runtime 1 ms Beats 15.18%

Memory 19.42 MB Beats 18.29%
"""

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        a_a_m, a_a_d = [int(s) for s in arriveAlice.split("-")]
        l_a_m, l_a_d = [int(s) for s in leaveAlice.split("-")]

        a_b_m, a_b_d = [int(s) for s in arriveBob.split("-")]
        l_b_m, l_b_d = [int(s) for s in leaveBob.split("-")]

        # We want to find the correct "start" and "end" dates to subtract

        # Alice arrives before Bob arrives -> start = Bob arrive
        if (a_a_m < a_b_m) or (a_a_m == a_b_m and a_a_d <= a_b_d):
            start = (a_b_m, a_b_d)
        else:
            start = (a_a_m, a_a_d)

        # Alice leaves before Bob leaves -> end = Alice arrive
        if (l_a_m < l_b_m) or (l_a_m == l_b_m and l_a_d <= l_b_d):
            end = (l_a_m, l_a_d)
        else:
            end = (l_b_m, l_b_d)

        # Calculate the days between the start and end
        
        # Start is after end
        if (start[0] > end[0]) or (start[0] == end[0] and start[1] > end[1]):
            return 0

        month_diff = end[0] - start[0]

        # Same month
        if month_diff == 0:
            day_diff = end[1] - start[1]
            return day_diff + 1

        days = 1

        for x in range(month_diff):
            days = days + days_in_month[(start[0] - 1) + x]
            if x == 0:
                days = days - start[1]

        days = days + end[1]

        return days
