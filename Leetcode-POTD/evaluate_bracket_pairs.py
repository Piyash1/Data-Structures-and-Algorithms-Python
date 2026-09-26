# 1807. Evaluate the Bracket Pairs of a String

class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        lookup = dict(knowledge)
        result = []

        i = 0
        while i < len(s):
            if s[i] == "(":
                j = i + 1
                while s[j] != ")":
                    j += 1
                key = s[i+1:j]
                
                result.append(lookup.get(key, "?"))

                i = j + 1

            else:
                result.append(s[i])
                i += 1
        
        return "".join(result)

# Example usage
if __name__ == "__main__":
    solution = Solution()
    s = "(name)is(age)yearsold"
    knowledge = [["name","bob"],["age","two"]]
    print(solution.evaluate(s, knowledge))