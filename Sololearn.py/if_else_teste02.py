age = 20
if age >= 18:
    print('Regular price')
else: 
    print('Discount')

# Segundo exercicio
age = 20
if age >= 18:
    print('Regular price')
else:
    print('Discount')
print('Proceed to payment')

# Mais um exercicio
age = 19
is_student = True
if age < 18 or is_student:
    print('Discount')
else: 
    print('Regular price')

# Aqui não precisamos utilizar o else, porque so precisamos saber se é menor ou não.
age = 16
if age < 18:
    print('Apply Discount')
print('Proceed to payment')

# Nessa parte a gente pode utilizar o elif para adicionar um outro valor
age = 50
if age < 18:
    print('Junior discount')
elif age >= 75:
    print('Senior discount')
else: 
    print('No discount')
print('Proceed to payment')

# Nesta parte a gente pode aninhar os resultados
age = 16
is_student = True 
if age < 18:
    if is_student:
        print('20% discount')
    else:
        print('10% discount')
else:
    print('Regular price')