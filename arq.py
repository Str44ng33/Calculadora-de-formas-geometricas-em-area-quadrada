print ('este programa que fiz na escola enquanto tava entendiado calcula a area quadrada de uma forma geometrica com as medidas de cm, metros, km, etc...')
print ('escolha oque você quer calcular a area quadrada de uma forma seguinte;')
print ('1.triangulo')
print ('2. trapezio')
print ('3. circulo')
#projeto matemática que tive ideia no meu colégio ainda kkkkkkk
print ('4. coroa circular')
cu = int(input('>>>: '))
print('qual a unidade de medida deste calculo??')
print('1. CM')
print('2. metros')
print('3. kilometros')
uni = int(input('>>>: '))
if uni == 1:
    unidade = 'cm'
if uni == 2:
    unidade = 'm'
if uni == 3:
    unidade = 'km'    
if cu == 1:
    print ('qual base do triangulo?')
    base = int(input('>>>: '))
    print (f'ok a base é {base} qual a altura???')
    altura = int(input('>>>: '))
    tria = (base * altura) / 2
    print (f'a area quadradra é: {tria}{unidade} quadrados')
if cu == 2:
    print ('qual a base MAIOR do trapezio?')
    basemaior = int(input('>>>: '))
    print ('qual a base MENOR do trapezio?')
    basemenor = int(input('>>>: '))
    print (f'ok a base maior é {basemaior} e base menor é {basemenor} qual a altura???')
    altura = int(input('>>>: '))
    trape1 = basemaior + basemenor
    trape2 = trape1 * altura
    trape3  = trape2 / 2
    print (f'{trape3}{unidade}')
if cu == 3:
    print ('qual o raio do circulo')
    raio = int(input('>>>:'))
    print (f'ok o raio é {raio}')
    result = 3.14 * (raio * raio)
    print (f'a area quadradra do circulo é: {result} quadrados')
if cu == 4:
    print('me diga o raio maior da coroa')   
    R = int(input('>>>: '))
    print('me diga o raio menor da coroa')
    r = int(input('>>>'))
    resultado = 3.14 * ((R * R)-(r * r))
    print (f'{resultado}')
#projeto matemática que tive ideia no meu colégio ainda kkkkkkk
