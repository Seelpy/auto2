from lexer import *


def exp(input: Lexer) -> (Lexer, bool):
    inputExp1, isRuleExp1 = exp1(input.copy())
    if isRuleExp1:
        return A(inputExp1.copy())

    return input, False


def A(input: Lexer) -> (Lexer, bool):
    inputR, isRuleR = R(input.copy())
    if isRuleR:
        return A(inputR.copy())

    return input, True


def R(input: Lexer) -> (Lexer, bool):
    tmpInput = input.copy()
    nextToken = input.nextToken()
    if nextToken.value == "==":
        return input, True

    if nextToken.value == "!=":
        return input, True

    if nextToken.value == "<":
        return B(input.copy())

    if nextToken.value == ">":
        return B(input.copy())

    return tmpInput, False


def B(input: Lexer) -> (Lexer, bool):
    tmpInput = input.copy()
    nextToken = input.nextToken()
    if nextToken.value == "=":
        return input, True

    return tmpInput, True


def exp1(input: Lexer) -> (Lexer, bool):
    inputExp2, isRuleExp2 = exp2(input.copy())
    if isRuleExp2:
        return C(inputExp2.copy())

    return input, False


def C(input: Lexer) -> (Lexer, bool):
    inputPLUSO, isRulePLUSO = PLUSO(input.copy())
    if isRulePLUSO:
        return C(inputPLUSO.copy())

    return input, True


def PLUSO(input: Lexer) -> (Lexer, bool):
    tmpInput = input.copy()
    nextToken = input.nextToken()
    if nextToken.value == "+":
        return input, True

    if nextToken.value == "-":
        return input, True

    if nextToken.value == "or":
        return input, True

    return tmpInput, False


def exp2(input: Lexer) -> (Lexer, bool):
    inputExp3, isRuleExp3 = exp3(input.copy())
    if isRuleExp3:
        return D(inputExp3.copy())

    return input, False


def D(input: Lexer) -> (Lexer, bool):
    inputMULO, isRuleMULO = MULO(input.copy())
    if isRuleMULO:
        return C(inputMULO)

    return input, True


def MULO(input: Lexer) -> (Lexer, bool):
    tmpInput = input.copy()
    nextToken = input.nextToken()

    if nextToken.value == "+":
        return input, True

    if nextToken.value == "/":
        return input, True

    if nextToken.value == "div":
        return input, True

    if nextToken.value == "mod":
        return input, True

    if nextToken.value == "and":
        return input, True

    return tmpInput, False


def exp3(input: Lexer) -> (Lexer, bool):
    tmpInput = input.copy()
    nextToken = input.nextToken()
    if nextToken.value == "-":
        return exp3(input.copy())

    if nextToken.value == "+":
        return exp3(input.copy())

    if nextToken.value == "(":
        inputExp, isRuleExp = exp(input.copy())
        if isRuleExp:
            exprToken = inputExp.nextToken()
            if exprToken.value == ")":
                return inputExp, True

    if nextToken.value == "num":
        return input, True

    if nextToken.value == "true":
        return input, True

    if nextToken.value == "false":
        return input, True

    if nextToken.value == "not":
        return exp(input.copy())

    return ident(tmpInput.copy())


def ident(input: Lexer) -> (Lexer, bool):
    tmpInput = input.copy()
    nextToken = input.nextToken()
    if nextToken.name == "IDENTIFIER":
        return E(input.copy())

    return tmpInput, False


def E(input: Lexer) -> (Lexer, bool):
    tmpInput = input.copy()
    nextToken = input.nextToken()
    if nextToken is None:
        return input, True
    if nextToken.value == ".":
        input1 = input.copy()
        nextToken2 = input1.nextToken()
        if nextToken2.name == "IDENTIFIER":
            return E(input1.copy())

    if nextToken.value == "[":
        inputListExp, isRuleListExp = listexp(input.copy())
        if isRuleListExp:
            listExpr = inputListExp.nextToken()
            if listExpr.value == "]":
                return E(inputListExp.copy())

    if nextToken.value == "(":
        inputListexp, isRuleListexp = listexp(input.copy())
        if isRuleListexp:
            listExpr = inputListexp.nextToken()
            if listExpr.value == ")":
                return E(inputListexp.copy())

    return tmpInput, True


def listexp(input: Lexer) -> (Lexer, bool):
    inputExp, isRuleExp = exp(input.copy())
    if isRuleExp:
        return F(inputExp.copy())

    return input, False


def F(input: Lexer) -> (Lexer, bool):
    tmpInput = input.copy()
    nextToken = input.nextToken()
    if nextToken.value == ",":
        inputF, isRuleF = F(input.copy())
        if isRuleF:
            return F(inputF.copy())

    return tmpInput, True


if __name__ == "__main__":
    userInput = input("Введите строку: ")

    lexer = Lexer(list(TOKENS.keys()), userInput)
    output = []
    resultExp, isValid = exp(lexer)
    print(f"Результат экспрессии: {isValid}")

