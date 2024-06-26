turno = input('Digite o turno que você estuda: matutino(M), vespertino(V) ou noturno(N)-->')
print()
if turno.upper() == 'M':
    print('Bom Dia!')

elif turno.upper() == 'V':
    print('Boa Tarde!')
    
elif turno.upper() == 'N':
    print('Boa Noite!')
    
else:
    print('Turno inválido')