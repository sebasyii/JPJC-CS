class Stack:
    def __init__(self):
        self.__data = []

    def __str__(self):
        output = ''
        for i in range(len(self.__data)):
            output = output + "\n" + "|{0:^10}|".format(self.__data[i])
        return output

    def IsEmpty(self):
        return len(self.__data) == 0

    def Push(self, data):
        self.__data.insert(0, data)

    def Pop(self):
        return self.__data.pop(0)

    def Peek(self):
        return self.__data[0]

    def Size(self):
        return len(self.__data)


def infixToPostFix(infixExpression):
    precedence = {"*": 3, "/": 3,
                  "+": 2, "-": 2,
                  "(": 1}
    opStack = Stack()
    postfixList = []
    tokenList = infixExpression.split()
    opStack.Push("(")
    tokenList.append(")")
    for token in tokenList:
        if token.isalpha() or token.isdigit():
            postfixList.append(token)
        elif token == "(":
            opStack.Push(token)
        elif token == "+" or token == "*" or token == "/":
            while (opStack.Peek() in "+-*/") and (precedence[opStack.Peek()] >= precedence[token]):
                postfixList.append(opStack.Pop())
            opStack.Push(token)
        elif token == ")":
            topToken = opStack.Pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = opStack.Pop()
    return postfixList


def evalPostfix(postfixExpression):
    opStack = Stack()
    tokenList = postfixExpression.split()
    print(tokenList)
    for token in tokenList:
        if token.isdigit():
            opStack.Push(token)
        else:
            op_X = opStack.Pop()
            op_Y = opStack.Pop()
            op_X = float(op_X)
            op_Y = float(op_Y)
            if token == "+":
                result = op_X + op_Y
            elif token == "-":
                result = op_Y - op_X
            elif token == "*":
                result = op_Y * op_X
            elif token == "/":
                result = op_Y / op_X
            opStack.Push(result)
    return opStack.Pop()


print(evalPostfix("5 6 2 + * 12 4 / -"))
