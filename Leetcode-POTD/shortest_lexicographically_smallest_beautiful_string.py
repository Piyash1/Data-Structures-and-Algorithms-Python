# 2904. Shortest and Lexicographically Smallest Beautiful String


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        positions = []

        # Store positions of all 1s
        for i in range(len(s)):
            if s[i] == '1':
                positions.append(i)

        # Not enough 1s
        if len(positions) < k:
            return ""

        answer = ""

        # Check every group of k consecutive 1s
        for i in range(len(positions) - k + 1):

            start = positions[i]
            end = positions[i + k - 1]

            candidate = s[start:end + 1]

            # Choose the shortest candidate.
            # If lengths are equal, choose lexicographically smaller.
            if (answer == "" or
                len(candidate) < len(answer) or
                (len(candidate) == len(answer) and candidate < answer)):

                answer = candidate

        return answer


# Example usage
if __name__ == "__main__":
    solution = Solution()

    s = "100011001"
    k = 3

    print(solution.shortestBeautifulSubstring(s, k))  # Answer: "11001"