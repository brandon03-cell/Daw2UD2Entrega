from Koncurso import Concierto, Usuario, EntradaGrada, EntradaPista, EntradaVIP

# Exercise 1
concierto1 = Concierto('Juanjo', 'Sevilla', 40.0, 100)
concierto2 = Concierto('Terry', 'Madrid', 55.0, 200)
concierto3 = Concierto('Branson', 'Málaga', 35.0, 150)
conciertos = [concierto1, concierto2, concierto3]

# Exercise 2
usuario1 = Usuario('Melendi', 47)
usuario2 = Usuario('Bad Bunny', 32)
usuario3 = Usuario('Ozuna', 34)
usuarios = [usuario1, usuario2, usuario3]

# Exercise 3
usuario1.comprar_entrada(concierto1, 'pista')
usuario1.comprar_entrada(concierto2, 'vip')
usuario2.comprar_entrada(concierto1, 'grada')
usuario2.comprar_entrada(concierto3, 'pista')
usuario3.comprar_entrada(concierto1, 'vip')
usuario3.comprar_entrada(concierto2, 'grada')

for usuario in usuarios:
    print(usuario)
    for entrada in usuario.entradas_compradas:
        print('  ', entrada)

# Exercise 4
usuario1.valorar(concierto1, 9)
usuario2.valorar(concierto3, 7)
usuario3.valorar(concierto2, 8)

# Exercise 5
# 1. Total de entradas vendidas
total_entradas = 0
for concierto in conciertos:
    total_entradas += len(concierto.entradas_vendidas)
print('Entradas vendidas en total:', total_entradas)

# 2. Entradas vendidas de cada tipo
pista = 0
grada = 0
vip = 0
for concierto in conciertos:
    for entrada in concierto.entradas_vendidas:
        if isinstance(entrada, EntradaPista):
            pista += 1
        elif isinstance(entrada, EntradaGrada):
            grada += 1
        elif isinstance(entrada, EntradaVIP):
            vip += 1
print('Entradas de pista:', pista)
print('Entradas de grada:', grada)
print('Entradas VIP:', vip)

# 3. Recaudacion total
recaudacion = 0.0
for concierto in conciertos:
    recaudacion += concierto.calcular_recaudacion()
print(f'Recaudación total: {recaudacion:.2f} €')

# 4. Precio medio de todas las entradas
if total_entradas > 0:
    precio_medio = recaudacion / total_entradas
else:
    precio_medio = 0.0
print(f'Precio medio: {precio_medio:.2f} €')

# 5. Concierto con mas entradas vendidas
mas_vendido = conciertos[0]
for concierto in conciertos:
    if len(concierto.entradas_vendidas) > len(mas_vendido.entradas_vendidas):
        mas_vendido = concierto
print(f'Concierto con más entradas: {mas_vendido} ({len(mas_vendido.entradas_vendidas)})')

# 6. Concierto con menos entradas vendidas
menos_vendido = conciertos[0]
for concierto in conciertos:
    if len(concierto.entradas_vendidas) < len(menos_vendido.entradas_vendidas):
        menos_vendido = concierto
print(f'Concierto con menos entradas: {menos_vendido} ({len(menos_vendido.entradas_vendidas)})')