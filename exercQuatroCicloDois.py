#-*-conding:latin1 -*-

for num in range(1,101):
    if (num==1):
        print 'numero', num, 'falso'
        num=num+1
    if (num%2!=0 or num==2) and (num%3!=0 or num==3) and (num%5!=0 or num==5) and  (num%7!=0 or num==7):
        print 'numero',num,'verdadeiro'
    else:
         print 'numero',num,'falso'
