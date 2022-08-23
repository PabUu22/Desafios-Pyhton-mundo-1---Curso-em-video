#Faça o progama que leia algo pelo teclado e mostre na tela seu tipo primitivo é mostre na tela todas sua especificações.
x = input('Digite algo! ')
print('É do tipo:', type(x))
print( 'É um numero? ',x.isdecimal())
print( 'Tem letra?', x.isalpha())
print('Tem letra e numero?',x.isalnum())
print('Tem letras minusculas',x.islower())
