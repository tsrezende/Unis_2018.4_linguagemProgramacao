#-*-conding:latin1 -*-

#programa para ler 3 valores para verificar se formam um triangulo

a = input('Insira o primeiro valor: ')
b = input('Insira o segundo valor: ')
c = input ('Insira o terceiro valor: ')

if (a==b and b==c):
    print 'Area do triangulo e de ',a*b/2
else:
    print 'Nao forma um triangulo, os valores inseridos foram' ,a,',',b,'e',c