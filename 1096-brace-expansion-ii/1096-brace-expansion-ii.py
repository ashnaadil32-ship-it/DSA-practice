class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:

        def parse(i):
            result = set()

            while i < len(expression) and expression[i] != '}':
                current = {""}

                if expression[i] == '{':
                    current, i = parse(i + 1)
                else:
                    current = {expression[i]}
                    i += 1

                # Concatenation
                while i < len(expression) and expression[i] not in ',}':
                    if expression[i] == '{':
                        nxt, i = parse(i + 1)
                    else:
                        nxt = {expression[i]}
                        i += 1

                    current = {a + b for a in current for b in nxt}

                # Union
                result |= current

                if i < len(expression) and expression[i] == ',':
                    i += 1

            return result, i + 1

        result, _ = parse(0)

        return sorted(result)