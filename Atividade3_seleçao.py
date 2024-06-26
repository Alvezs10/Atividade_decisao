#FAÇA UM PROGRAMA QUE VERIFIQUE SE UMA LETRA DIGITADA É 'F' OU 'M'
gen = input('Informe seu genero com "M" ou "F": ')

if gen == 'M' or gen == 'm':
    print('Masculino')
    
elif gen == 'F' or gen == 'f':
    print('Feminino')

else:
    print('Sexo Inválido')