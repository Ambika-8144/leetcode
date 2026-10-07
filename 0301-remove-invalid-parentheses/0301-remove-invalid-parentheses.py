class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        def isValid(string):
            balance = 0

            for ch in string:
                if ch == '(':
                    balance += 1

                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = [s]
        visited = {s}

        while queue:

            next_level = []

            for string in queue:

                if isValid(string):
                    return [x for x in queue if isValid(x)]

                for i in range(len(string)):

                    # Only remove parentheses
                    if string[i] not in "()":
                        continue

                    new_string = string[:i] + string[i+1:]

                    if new_string not in visited:
                        visited.add(new_string)
                        next_level.append(new_string)

            queue = next_level

        return [""]