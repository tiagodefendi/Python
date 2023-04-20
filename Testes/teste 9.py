def maiusculaMinuscula(string):
    n1 = 0
    n2 = 0
    for i in string:
        if i.isupper():
            n1 += 1
            return n1
        else:
            n2 += 1
    print(n1)
    print(n2)

def main():
    string = "Ana's Julia's LinDas"
    maiusculaMinuscula(string)
    print(f'A string tem {n1} letras maiusculas e {n2}, minusculas', maiusculaMinuscula(string))
main()