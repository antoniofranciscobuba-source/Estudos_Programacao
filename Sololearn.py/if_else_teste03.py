age = 16
is_student = True
if age < 18:
    if is_student:
        print('20% discount')
    else:
        print('10% discount')
else: 
    print('Regular price')
    
# Outro exemplo
temperature = 33
if temperature < 35:
    print('Hypotermia')
elif temperature > 39:
    print('Febre')