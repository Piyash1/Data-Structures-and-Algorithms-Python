# You are given timings of n meetings in the form of (start[i], end[i]) where start[i] is the start time of meeting i and end[i] is the finish time of meeting i. Return the maximum number of meetings that can be accommodated in a single meeting room, when only one meeting can be held in the meeting room at a particular time. 

class Solution:
    def maximumMeetings(self,start,end):
        meetings = []
        for i in range(len(start)):
            meetings.append((start[i], end[i]))
            
        meetings.sort(key=lambda x: x[1])
        
        count = 1
        last_end = meetings[0][1]
        
        for i in range(1, len(meetings)):
            if meetings[i][0] > last_end:
                count += 1
                last_end = meetings[i][1]
        return count
    
sol = Solution()
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]
print(sol.maximumMeetings(start, end))  # Output: 4