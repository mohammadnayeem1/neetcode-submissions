"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda intervals:intervals.start)
        if not intervals:
            return True
        last = intervals[0].end
        for interval in intervals[1:]:
            if interval.start < last:
                return False
            else:
                last = interval.end
        return True