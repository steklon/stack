import stack


def is_balanced(brackets):
    stack_ = stack.Stack()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    for bracket in brackets:
        if bracket in opening_brackets:
            stack_.push_(bracket)
        elif bracket in closing_brackets:
            if stack_.is_empty():
                return False
            elif opening_brackets.index(
                    stack_.peek()) is not closing_brackets.index(bracket):
                return False
            else:
                stack_.pop_()
    return stack_.is_empty()


def check_balanced(brackets):
    if is_balanced(brackets):
        return "Сбалансированно"
    else:
        return "Несбалансированно"
