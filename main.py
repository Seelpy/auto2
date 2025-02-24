
def exp(input: str) -> (str, bool):
    input.strip()

    inputExp1, isRuleExp1 = exp1(input)
    if isRuleExp1:
        return A(inputExp1)

    return "", False


def A(input: str) -> (str, bool):
    input.strip()

    inputR, isRuleR = R(input)
    if isRuleR:
        return A(inputR)

    return input, True


def R(input: str) -> (str, bool):
    input.strip()

    if input.startswith("=="):
        return input.removeprefix("==").strip(), True

    if input.startswith("!="):
        return input.removeprefix("!=").strip(), True

    if input.startswith("<"):
        input.removeprefix("<").strip()

        return B(input)

    if input.startswith(">"):
        input.removeprefix(">").strip()

        return B(input)

    return "", False


def B(input: str) -> (str, bool):
    input.strip()

    if input.startswith("="):
        return input.removeprefix("=").strip(), True

    return input, True


def exp1(input: str) -> (str, bool):
    input.strip()

    inputExp2, isRuleExp2 = exp2(input)
    if isRuleExp2:
        return C(inputExp2)

    return "", False


def C(input: str) -> (str, bool):
    input.strip()

    inputPLUSO, isRulePLUSO = PLUSO(input)
    if isRulePLUSO:
        return C(inputPLUSO)

    return input, True


def PLUSO(input: str) -> (str, bool):
    input.strip()

    if input.startswith("+"):
        return input.removeprefix("+").strip(), True

    if input.startswith("-"):
        return input.removeprefix("-").strip(), True

    if input.startswith("or"):
        return input.removeprefix("or").strip(), True

    return "", False


def exp2(input: str) -> (str, bool):
    input.strip()

    inputExp3, isRuleExp3 = exp3(input)
    if isRuleExp3:
        return D(inputExp3)

    return "", False


def D(input: str) -> (str, bool):
    input.strip()

    inputMULO, isRuleMULO = MULO(input)
    if isRuleMULO:
        return C(inputMULO)

    return input, True


def MULO(input: str) -> (str, bool):
    input.strip()

    if input.startswith("+"):
        return input.removeprefix("+").strip(), True

    if input.startswith("/"):
        return input.removeprefix("/").strip(), True

    if input.startswith("div"):
        return input.removeprefix("div").strip(), True

    if input.startswith("mode"):
        return input.removeprefix("mod").strip(), True

    if input.startswith("and"):
        return input.removeprefix("and").strip(), True

    return "", False


def exp3(input: str) -> (str, bool):
    input.strip()

    if input.startswith("-"):
        input.removeprefix("-").strip()

        return exp3(input)

    if input.startswith("+"):
        input.removeprefix("+").strip()

        return exp3(input)

    if input.startswith("("):
        input.removeprefix("(").strip()

        inputExp, isRuleExp = exp(input)
        if isRuleExp:
            if inputExp.startswith(")"):
               return inputExp.removeprefix(")").strip(), True

    if input.startswith("num"):
        return input.removeprefix("num").strip(), True

    if input.startswith("true"):
        return input.removeprefix("true").strip(), True

    if input.startswith("false"):
        return input.removeprefix("false").strip(), True

    if input.startswith("not"):
        input.removeprefix("not").strip()

        return exp(input)

    return ident(input)


def ident(input: str) -> (str, bool):
    input.strip()

    if input.startswith("id"):
        input.removeprefix("id").strip()
        
        return E(input)

    return "", False


def E(input: str) -> (str, bool):
    input.strip()

    if input.startswith(".id"):
        input.removeprefix(".id").strip()

        return E(input)

    if input.startswith("["):
        input.removeprefix("[").strip()

        inputListExp, isRuleListExp = listexp(input)
        if isRuleListExp:
            if inputListExp.startswith("]"):
                inputListExp.removeprefix("]").strip()

                return E(inputListExp)

    if input.startswith("("):
        input.removeprefix("(").strip()

        inputListexp, isRuleListexp = listexp(input)
        if isRuleListexp:
            if inputListexp.startswith(")"):
                inputListexp.removeprefix(")").strip()

                return E(inputListexp)

    return "", True


def listexp(input: str) -> (str, bool):
    input.strip()

    inputExp, isRuleExp = exp(input)
    if isRuleExp:
        return F(inputExp)

    return "", False


def F(input: str) -> (str, bool):
    input.strip()

    if input.startswith(", "):
        input.removeprefix(", ").strip()

        inputF, isRuleF = F(input)
        if isRuleF:
            return F(inputF)

    return input, True

if __name__ == "__main__":
    user_input = input("Введите строку: ")
    print(exp(user_input))
