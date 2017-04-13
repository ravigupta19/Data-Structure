class BalanacedParentheses(object):

    def __init__(self):
        self.stk = []
        self.top = None

    def pop(self):
        self.stk.pop()
        try:
            self.top = self.stk[-1]
        except IndexError:
            self.top  = None

    def push(self,data):
        self.stk.append(data)
        self.top = self.stk[-1]


    def balancedParantheses(self, string):
        for para in string:
            if para == '(' or para =='{' or para == '[':
                self.push(para)
            elif para == '}' or para == ')' or para == ']':
                if self.arePair(self.top, para):
                    self.pop()
                else:
                    return False
        return self.isEmpty()


    def arePair(self,opening, closing):
        return(
                opening == '(' and closing == ')'
            or opening == '[' and closing == ']'
            or opening == '{' and closing == '}'
        )

    def isEmpty(self):
        return len(self.stk) == 0

stk = BalanacedParentheses()
print(stk.balancedParantheses(input()))