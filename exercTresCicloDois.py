#-*-conding:latin1 -*-

#ler 3 numeros e mostre o menos deles

num1 = input ('Insira o primeiro numero: ')
num2 = input ('Insira o segundo numero: ')
num3 = input ('Insira o terceiro numero:')

if (num1>=num2 and num2>num3):
    print 'O menor numero e :',num3
else:
    if (num1>num2 and num3>=num2):
        print 'O menor numero e: ',num2
    else:
        if(num2>num1 and num1>num3):
            print 'O menor numero e:',num3
        else:
            if(num3>num1 and num1>num2):
                print 'O menor numero e:',num2
            else:
                if(num3>num2 and num2>num1):
                    print 'O menor numero e:',num1
                else:
                    if(num2>num3 and num3>num1):
                        print'O menor numero e:',num1

