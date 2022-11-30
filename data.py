#Crie um programa que lê o ano de nascimento de uma pessoa e o ano atual. Calcule e
#mostre qual é: a idade da pessoa em anos, a idade da pessoa em meses, a idade da
#pessoa em dias e a idade da pessoa em semanas.


anoNascimento=int(input("Qual ano você nasceu? "))
anoAtual=int(input("Em que ano estamos? "))

anos=anoAtual-anoNascimento
meses=anoNascimento*12
dias=anoNascimento*365
semanas=anoNascimento*52

int(anos)
int(meses)
int(dias)
int(semanas)

print("você tem anos",anos)
print("você tem meses", meses)
print("você tem dias", dias)
print("você tem semanas",semanas)