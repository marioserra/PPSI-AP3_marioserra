def leiaInt (msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um numero inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print ('\m\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def linha (tam = 42):
    return '_'*tam


def cabeçalho(txt):
    print (linha())
    print (txt.center(42))
    print (linha())

def menu (lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print (f'{c} - {item}')
        c += 1
    print (linha())
    opc = leiaInt('Sua Opção: ')
    return opc

def lerArquivo(nome):
    try:
        a=open(nome, 'rt')
    except:
        print ('Erro ao ler o arquivo')
    else:
        cabeçalho('Banco de Palavras')
        print(a.read())

def escreveArquivo(nome):
    try:
        a=open(nome, 'a')
    except:
        print ('Erro ao inserir palavra no arquivo')
    else:
        palavra = input('Digite sua palavra:\n')
        a = open(nome, 'a')
        a.write(palavra + '\n')
        print("Sua palavra foi inserida ")
        a.close()

        cabeçalho('Banco de Palavras')
        print(a.read)