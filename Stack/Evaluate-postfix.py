class Evaluate(object):

    def __init__(self):
        self.stk = []
        self.top = None

    def pop(self):
        try:
            res = self.stk.pop()
            self.top = self.stk[-1]
        except IndexError:
            self.top = None
        return res

    def push(self,data):
        self.stk.append(data)
        self.top = self.stk[-1]

    def evaluatePostfix(self, expression):
        for char in expression:
            try:
                data = int(char)
            except ValueError:
                oper2 = self.pop()
                oper1 = self.pop()
                res = self.evaluateExpression(char,oper1, oper2)
                self.push(res)
            else:
                self.push(data)
        print(self.getTop())

    def evaluatePrefix(self,expression):
        for char in expression[::-1]:
            try:
                data = int(char)
            except ValueError:
                oper1 = self.pop()
                oper2 = self.pop()
                res = self.evaluateExpression(char, oper1, oper2)
                self.push(res)
            else:
                self.push(data)
        print(self.getTop())

    def evaluateExpression(self,operand, operator1, operator2):
        if operand == '*':
            return operator1 * operator2
        elif operand == '/':
            return operator1 // operator2
        elif operand == '+':
            return operator1 + operator2
        elif operand == '-':
            return operator1 - operator2

    def infixtopostfix(self,expression):
        pass

    def getTop(self):
        return self.top

evalexper = Evaluate()
evalexper.evaluatePostfix('23*54*+9-')
evalexper.evaluatePrefix('-+*23*549')
