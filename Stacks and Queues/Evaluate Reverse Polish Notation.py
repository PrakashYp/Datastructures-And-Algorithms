
def evalRPN(tokens):

    stack = []
    result = 0

    for token in tokens:
        if token in {'+','-','*','/'}:
            num2 = stack.pop()
            num1 = stack.pop()

            if token == '+':
                result = num1 + num2
            elif token == '-':
                result = num1 - num2
            elif token == '*':
                result = num1 * num2
            else:
                result = int(num1 / num2)
            stack.append(result)               
        else:
            stack.append(int(token))

    return stack[-1]


print(evalRPN( ["2","1","+","3","*"]))
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(evalRPN(["4","13","5","/","+"]))




