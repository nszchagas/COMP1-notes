lookahead = ''


def nextToken() -> str:
    token = input("Próximo token:\n")
    return token if token else -1


def reconhece(value: str) -> bool:
    if (lookahead == value):
        lookahead = parser()
        return True
    else:
        return False


def parser():
    nextToken()
    E()


def E(state: int = 0) -> None:
    if state == 0 or state == 4:
        T()
        E(3)
        return
    elif state == 3:
        reconhece('+')
        E(4)
    else:
        print("erro")


def T(state: int = 7) -> None:
    if state == 7:
        F()
        T(10)
    elif state == 10:
        if (lookahead == -1):
            return
        reconhece('x')
        T(11)
    elif state == 1:
        F()
        T(10)
    else:
        print("erro")


def F(state: int = 14) -> None:
    if state == 14:
        if lookahead == 'id':
            reconhece('id')
        else:
            reconhece('(')
            E()
            reconhece(')')
    else:
        print("erro")


while lookahead != -1: 
    lookahead = parser()
