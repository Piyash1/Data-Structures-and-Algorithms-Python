
# 1541. Minimum Insertions to Balance a Parentheses String

class Solution:
    def minInsertions(self, s: str) -> int:
        open_count = 0
        insertions = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                open_count += 1
                i += 1

            else:  # s[i] == ')'
                # Check whether we have a pair of closing parentheses
                if i + 1 < len(s) and s[i + 1] == ')':
                    if open_count > 0:
                        open_count -= 1
                    else:
                        # Insert a missing opening parenthesis
                        insertions += 1

                    # We processed both closing parentheses
                    i += 2

                else:
                    # We have only one closing parenthesis
                    if open_count > 0:
                        open_count -= 1
                        insertions += 1
                    else:
                        # Insert '(' and another ')'
                        insertions += 2

                    i += 1

        # Every remaining '(' needs two closing parentheses
        insertions += open_count * 2

        return insertions


# Example usage
if __name__ == "__main__":
    solution = Solution()

    s = "(()))"
    print(solution.minInsertions(s))
