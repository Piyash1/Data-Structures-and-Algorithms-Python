# 2409. Count Days Spent Together

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def days_of_year(date):
            month = int(date[:2])
            day = int(date[3:])

            total = 0
            for i in range(month - 1):
                total += days_in_month[i]
            
            return total + day

        start_alice = days_of_year(arriveAlice)
        end_alice = days_of_year(leaveAlice)
        start_bob = days_of_year(arriveBob)
        end_bob = days_of_year(leaveBob)

        overlap_start = max(start_alice, start_bob)
        overlap_end = min(end_alice, end_bob)

        return max(0, overlap_end - overlap_start + 1)


# Example usage
if __name__ == "__main__":
    solution = Solution()
    arriveAlice = "08-15"
    leaveAlice = "08-18"
    arriveBob = "08-16"
    leaveBob = "08-19"
    print(solution.countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))
