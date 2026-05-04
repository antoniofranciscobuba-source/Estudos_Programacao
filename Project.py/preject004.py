passWord = 'abc123'
pas = ' '
while pas not in passWord:
    pas = str(input('Insira a PassWord: '))
    if pas == passWord:
        print('AUTORIZAÇÃO CONCEDIDA!✅')
    else:
        print('PassWord incorreta!❌')
        print('Tente novamente')
