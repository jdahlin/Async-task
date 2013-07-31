import sys
from datetime import date

if sys.argv[1] == '-i':
    print "==========Insertion mode=========="
    print 
    with open('arquivo.txt', 'w') as arquivo:
        title = raw_input("Insira um cabecalho: ")
        text = raw_input("Insira o texto: ")
        date = unicode(date.today())
        arquivo.write(date)
        arquivo.write('\n----------------------\n')        
        arquivo.write(title)
        arquivo.write('\n----------------------\n')
        arquivo.write(text)
        arquivo.write('\n\n')

    arquivo.close()
    
if sys.argv[1] == '-l':
    print "=====List Mode=====\n"
    with open('arquivo.txt', 'r') as arquivo:
        texto = arquivo.read()
        print texto

    arquivo.close()
