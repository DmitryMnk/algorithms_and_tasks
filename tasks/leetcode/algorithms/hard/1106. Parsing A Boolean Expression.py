from collections import deque


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        # def logical_and(*args):
        #     return all(args)
        #
        # def logical_or(*args):
        #     return any(args)
        #
        # def logical_not(a):
        #     return not a
        #
        # stack = deque()
        # args = []
        # table = {
        #     '&': logical_and,
        #     '|': logical_or,
        #     '!': logical_not,
        #     't': True,
        #     'f': False
        # }
        #
        # for c in expression:
        #     if c in ['&', '|', '!']:
        #         stack.append(table[c])
        #     elif c in ['t', 'f']:
        #         args.append(table[c])
        #     elif c == ')':
        #         print(stack)
        #         while stack:
        #             func = stack.pop()
        #             result = func(*args)
        #             print(func)
        #             args = [result]
        # return result

        st = deque()
        for c in expression:
            if c == "," or c == "(":
                continue
            if c in ["t", "f", "!", "&", "|"]:
                st.append(c)
            elif c == ")":
                has_true = False
                has_false = False
                while st[-1] not in ["!", "&", "|"]:
                    top_value = st.pop()
                    if top_value == "t":
                        has_true = True
                    elif top_value == "f":
                        has_false = True
                op = st.pop()
                if op == "!":
                    st.append("t" if not has_true else "f")
                elif op == "&":
                    st.append("f" if has_false else "t")
                else:
                    st.append("t" if has_true else "f")
        return st[-1] == "t"


solution = Solution()
print(solution.parseBoolExpr("!(&(f,t))"))