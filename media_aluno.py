# m-dia-de-aluno
#Média do aluno.exemple

escolha = 0
sair = int(1)
cont = int(2)
while escolha != sair :
#cores
    red = '\033[00;31m' # Red
    white = '\033[0;37m' # White
    green = '\033[32m' # Green
    orange = '\033[05;33m' # Orange
    blue = '\033[05;34m' # blue
    pink = '\033[0;35m' # pink

    num_aluno = input(orange+"digite nome do aluno:")
    nota = float(input (white+" \n digite a primeira nota do aluno:"))
    nota_y = float(input ("\n digite a segunda nota do aluno:"))
    nota_x = float(input ("\n digite a terceira  nota do aluno:"))
    nota_two = float (nota_y)
    nota_one = float (nota)
    nota_tree = float (nota_x)
    tres = int(3)
    def valores (n1,n2,n3,n4):
        return (n1+n2+n3)/n4
    media = valores (nota_one,nota_two,nota_tree,tres)
    me = float(media)
    if (me < 6) :
        print (red+"\n o aluno de nome :{} teve media de {} e foi reprovado.".format(num_aluno,me))
    else:
        print (green+"\n o aluno de nome :{} teve media  {} e foi  aprovado".format(num_aluno,me))
    print (blue+"\n obrigado por usar este script,tenha um otimo dia !")
    print ("\n(1)sair\n(2)verificar aluno")

    escolha = int (input(blue+"\n voce deseja sair o verificar media de outro aluno?\n"+orange))
    if escolha != cont :
        print (red+"vc saiu do sistema")
        break

