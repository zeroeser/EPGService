from operator import add, sub, truediv, mul


def dijkstras_two_stack_algorithm(equation: str) -> int:
    """
    :param equation: a string
    :return: result: an integer
    """
    operators = {"*": mul, "/": truediv, "+": add, "-": sub}
    prev_symbol = None
    operand_stack = []
    operator_stack = []
    number = ''
    for i in equation:
        if i.isdigit():
            number += i
            prev_symbol = i
        elif i in operators and prev_symbol not in operators:

            operator_stack.append(i)
            prev_symbol = i
            if number:
                operand_stack.append(int(number))
                number = ''
        elif i == ")":
            if number:
                operand_stack.append(int(number))
                number = ''
            prev_symbol = i
            opr = operator_stack[-1]
            operator_stack.pop()
            num1 = operand_stack[-1]
            operand_stack.pop()
            num2 = operand_stack[-1]
            operand_stack.pop()

            total = operators[opr](num2, num1)
            operand_stack.append(total)

    return operand_stack[-1]

