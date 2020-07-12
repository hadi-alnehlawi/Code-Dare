def solution(X, Y, D):
    divide = Y // D
    calculate = divide * D + X
    if calculate > Y:
        return (divide - (X // D))
    elif calculate < Y:
        return divide + 1
    else:
        return divide
