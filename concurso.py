# Clase base de las entradas
class Entrada:
    def __init__(self, concierto):
        self.concierto = concierto

    # La entrada general cuesta el precio base del concierto
    def get_precio_total(self):
        return self.concierto.precio_base

    def __str__(self):
        return f'Entrada general para {self.concierto.artista} - {self.get_precio_total():.2f} €'


# Entrada de grada, lleva un asiento asignado
class EntradaGrada(Entrada):
    def __init__(self, concierto, asiento):
        super().__init__(concierto)
        self.asiento = asiento

    # Cuesta lo mismo que la general
    def get_precio_total(self):
        return self.concierto.precio_base

    def __str__(self):
        return f'Entrada de grada para {self.concierto.artista} - {self.get_precio_total():.2f} €'


# Entrada de pista
class EntradaPista(Entrada):
    def __init__(self, concierto, de_pie):
        super().__init__(concierto)
        self.de_pie = de_pie

    # Precio base + 10%
    def get_precio_total(self):
        return self.concierto.precio_base * 1.10

    def __str__(self):
        return f'Entrada de pista para {self.concierto.artista} - {self.get_precio_total():.2f} €'


# Entrada VIP, puede incluir consumicion o no
class EntradaVIP(Entrada):
    def __init__(self, concierto, incluye_consumicion):
        super().__init__(concierto)
        self.incluye_consumicion = incluye_consumicion

    # Precio base + 20% si incluye consumicion, si no + 15%
    def get_precio_total(self):
        if self.incluye_consumicion:
            return self.concierto.precio_base * 1.20
        else:
            return self.concierto.precio_base * 1.15

    def __str__(self):
        return f'Entrada VIP para {self.concierto.artista} - {self.get_precio_total():.2f} €'


class Concierto:
    def __init__(self, artista, ciudad, precio_base, aforo_maximo, activo=True):
        self.artista = artista
        self.ciudad = ciudad
        self.precio_base = precio_base
        self.aforo_maximo = aforo_maximo
        self.entradas_vendidas = []
        self.activo = activo

    # Suma el precio de cada entrada vendida (cada tipo tiene su precio)
    def calcular_recaudacion(self):
        acc = 0.0
        for entrada in self.entradas_vendidas:
            acc += entrada.get_precio_total()
        return acc

    # Recaudacion entre el numero de entradas
    def calcular_precio_medio(self):
        if len(self.entradas_vendidas) == 0:
            return 0.0
        return self.calcular_recaudacion() / len(self.entradas_vendidas)

    # Quedan entradas si las vendidas no llegan al aforo
    def entradas_disponibles(self):
        return len(self.entradas_vendidas) < self.aforo_maximo

    def __str__(self):
        return f'Concierto de {self.artista} en {self.ciudad}'


class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.entradas_compradas = []
        self.conciertos_asistidos = set()
        self.valoraciones = {}

    def comprar_entrada(self, concierto, tipo_entrada):
        # Comprobaciones antes de comprar
        if not concierto.activo:
            raise Exception(f'El {concierto} no está activo')
        if concierto in self.conciertos_asistidos:
            raise Exception(f'{self.nombre} ya ha asistido al {concierto}')
        if not concierto.entradas_disponibles():
            raise Exception(f'No quedan entradas para el {concierto}')

        # Se crea la entrada segun el tipo que se pida
        tipo_entrada = tipo_entrada.lower()
        if tipo_entrada == 'grada':
            entrada = EntradaGrada(concierto, '1A')
        elif tipo_entrada == 'pista':
            entrada = EntradaPista(concierto, True)
        elif tipo_entrada == 'vip':
            entrada = EntradaVIP(concierto, True)
        elif tipo_entrada == 'general':
            entrada = Entrada(concierto)
        else:
            raise Exception(f'El tipo de entrada "{tipo_entrada}" no existe')

        concierto.entradas_vendidas.append(entrada)
        self.entradas_compradas.append(entrada)
        self.conciertos_asistidos.add(concierto)
        return entrada

    def valorar(self, concierto, valoracion):
        if concierto not in self.conciertos_asistidos:
            raise Exception(f'{self.nombre} no ha asistido al {concierto}')
        if valoracion < 0 or valoracion > 10:
            raise Exception('La valoración tiene que estar entre 0 y 10')

        # Si ya estaba valorado se sobrescribe
        self.valoraciones[concierto] = valoracion

    def __str__(self):
        return f'{self.nombre} (ha asistido a {len(self.conciertos_asistidos)})'