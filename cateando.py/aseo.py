## crear una tabla donde permita saber
## que persona le toca hacer el ASEO cada jueves
## siendo 8 personas y dividiendolas en dos areas de ASEO
import calendar
from datetime import datetime, timedelta

# Lista de personas
personas = ["jhon", "adrian", "diego", "jorge", "duver", "nixon", "richard", "adrean"]

def generar_turnos(personas):
    # Crea lista de turnos de 2 en 2
    turnos = [(personas[i], personas[i+1]) for i in range(0, len(personas), 2)]
    return turnos

def obtener_proximos_jueves(fecha_inicio, cantidad_jueves):
    jueves = []
    fecha_actual = fecha_inicio
    
    while len(jueves) < cantidad_jueves:
        if fecha_actual.weekday() == calendar.THURSDAY:
            jueves.append(fecha_actual)
        fecha_actual += timedelta(days=1)
        
    return jueves

# Fecha de inicio del primer turno
fecha_inicio = datetime(2024, 10, 31)  # Primer jueves del año
cantidad_jueves = 16  # Número de jueves (doble rotación de 8 personas)

# Obtener lista de jueves
fechas_jueves = obtener_proximos_jueves(fecha_inicio, cantidad_jueves)

# Generar turnos de limpieza en ciclos de rotación
turnos = generar_turnos(personas)

# Asignar turnos rotativos cada jueves
for i, fecha in enumerate(fechas_jueves):
    pareja = turnos[i % len(turnos)]
    print(f"{fecha.strftime('%d-%m-%Y')}: Turno de limpieza para {pareja[0]} y {pareja[1]}")
