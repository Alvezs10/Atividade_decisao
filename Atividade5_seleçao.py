nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2

if media == 10:
    print('Aluno aprovado com distinção!!')
    
elif media >= 7:
    print('Aluno aprovado!')
    
else:
    print('Aluno reprovado :(')