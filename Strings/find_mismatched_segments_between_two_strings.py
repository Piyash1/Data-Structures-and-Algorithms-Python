# 4106. Find Mismatched Segments Between Two Strings

class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        result = []
        i = 0

        while i < len(s1):
            
            # skip matching char
            if s1[i] == s2[i]:
                i += 1
            
            else:
                # remember start of mismatch
                start = i

                # continue while char are different
                while i < len(s1) and s1[i] != s2[i]:
                    i += 1

                result.append([s1[start:i], s2[start:i]])

        return result


# Example usage
if __name__ == "__main__":
    solution = Solution()
    s1 = "earth"
    s2 = "empty"
    print(solution.findMismatchedSegments(s1, s2))
