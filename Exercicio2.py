"Uma escola deseja fornecer a cada professor um programa que leia o nome e as notas de um aluno em determinada disciplina,"
"mostre a média anual do aluno e se ele foi aprovado ou reprovado ,A média da escola é 7."
"e ao final informe a média da turma naquela disciplina."

somamedia =  0
materia = input("Informe a discplina:")
qtdalunos = int(input("Informe a quantidade de alunos:"))

for i in range(qtdalunos):
    nota1 = float(input("Nota do 1º bimestre:"))
    nota2 = float(input("Nota do 2º bimestre:"))
    nota3 = float(input("Nota do 3º bimestre:"))
    nota4 = float(input("Nota do 4º bimestre:"))

    media= (nota1 + nota2 + nota3 + nota4) / 4
    print(f"Média do aluno = {media}")

    if media >= 7:
        print("APROVADO!")
    else:
        print("REPROVADO!")

    somamedia += media

mediaturma= media/qtdalunos


print(f"Media da turma em: {materia} = {mediaturma} ")

