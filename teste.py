import re

count = 0

while count == 0:

    expressao = input("Digite a expressao a analisar: ")

    def separaString(i):
        separa = re.split(r'\s',i)
        if separa is None:
            return None
        if separa:
            return separa

    def numeroNegativo(i):
        negativo = re.compile(r'^-\d*\d$')
        busca = re.search(negativo, i)
        if busca:
            return True
        else:
            return False

    def numeroPositivo(i):
        positivo = re.compile(r'\d*')
        busca = re.search(positivo, i)
        if busca:
            return True
        else:
            return False

    def letra(i):
        letras = re.compile(r'[a-zA-Z]')
        busca = re.search(letras, i)
        if busca:
            return True
        else:
            return False

    palavraSeparada = separaString(expressao)

    print(" EXPRESSÃO COMPLETA: \n"+str(palavraSeparada))

    for i in palavraSeparada:
        if numeroNegativo(i):
            print("("+str(i)+") NÚMERO (NEGATIVO)")
        elif i == '+':
            print("(+) -> OPERADOR DE SOMA")
        elif i == '-':
            print("(-) -> OPERADOR DE SUBTRAÇÃO")
        elif i == '*':
            print("(*) -> OPERADOR DE MULTIPLICAÇÃO")
        elif i == '**':
            print("(**) -> OPERADOR DE EXPONENCIAÇÃO")
        elif i == '/':
            print("(/) -> OPERADOR DE DIVISÃO")
        elif i == ')':
            print(" ) -> DELIMITADOR PARENTESES")
        elif i == '(':
            print(" ( -> DELIMITADOR PARENTESES")
        elif letra(i):
            print("("+i+") -> CARACTERE INVÁLIDO")
        elif numeroPositivo(i):
            print("("+str(i)+") -> NUMERO (POSITIVO)")
        else:
            print("ERRO: CARACTERE INVALIDO")