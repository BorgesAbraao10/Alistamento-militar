# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today ().year # Qual é o ano de hoje (do dia q estou utilizando o programa)
nasceu = int (input('Digite o ano em que você nasceu:'))
idade = atual - nasceu 
print ('Quem nasceu em {} tem {} anos em {} '.format (nasceu, idade,atual))
if idade == 18:
    print ('Você precisa de alistar IMEDIATAMENTE!')
    print ('Procure uma base militar da sua cidade.')
elif idade < 18:
    saldo = 18 - idade
    print ('Ainda faltam {} anos para você se alistar'.format (saldo))
    ano = atual + saldo
    print ('Seu alistamento será em {}'.format (ano))
else:
    saldo = idade - 18
    print ('Você já deveria ter se alistado há {} anos.'.format (saldo))
    ano = atual - saldo 
    print ('Seu alistamento foi em {}'.format (ano))
    print ('Procure uma base militar da sua cidade.')

    
