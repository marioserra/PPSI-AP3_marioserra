from projeto_forca.Lib.Interface import *
from projeto_forca.Lib.arquivo import *
import forca from projeto_forca.Lib.cont_jogo

arq = 'bco_palavras.txt'

if arquivoExiste(arq):
    print ('Arquivo encontrado com sucesso!')

else:
    print('Arquivo não encontrado')


while True:
    resposta = menu(['(1)Jogar', '(2)Banco de Palavras', '(3)Inserir palavra nova', '(4)Sair'])
    if resposta == 1:
        print('Opção 1')  #aqui tem que chamar o jogo

    elif resposta == 2:          # lista as palavras do jogo
            lerArquivo(arq)

    elif resposta == 3:         # insere nova palavra no jogo
            escreveArquivo(arq)

    elif resposta == 4:          # Sai do jogo
            print ('Saindo do jogo ... Até logo!')

            break
    else:
        print ('\033[31mERRO! Digite um opção válida\033[m')

        sleep(2)
        break

cabeçalho('Jogo da Forca v.1.0')
menu (['(1)Jogar', '(2)Banco de Palavras', '(3)Inserir palavra nova', '(4)Sair'])




