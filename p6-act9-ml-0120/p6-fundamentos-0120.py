# Nicole Robles NC 0120
# ==========================================
# 1. VARIABLES EN PYTHON
# ==========================================
# Ejemplo 1: Creación de variables
nombre = "Ana"
edad = 25
print("1.1 Nombre:", nombre, "| Edad:", edad)
# Ejemplo 2: Valores flotantes y booleanos
precio = 19.99
es_estudiante = True
print("1.2 Precio:", precio, "| Es estudiante?:", es_estudiante)
# Ejemplo 3: Reasignación de variables
x = 10
x = "Ahora soy una cadena de texto"
print("1.3 Reasignación x:", x)
# ==========================================
# 2. MÚLTIPLES VARIABLES
# ==========================================
# Ejemplo 1: Múltiples valores a múltiples variables
x_var, y_var, z_var = "Manzana", "Banana", "Cereza"
print("2.1 Frutas:", x_var, y_var, z_var)
# Ejemplo 2: Un mismo valor a múltiples variables
a = b = c = "Python"
print("2.2 Mismo valor:", a, b, c)
# Ejemplo 3: Desempaquetar una lista
frutas = ["Naranja", "Mango", "Uva"]
p, q, r = frutas
print("2.3 Desempaquetado:", p, q, r)
# ==========================================
# 3. TIPOS DE DATOS
# ==========================================
# Ejemplo 1: Cadenas (str) y Enteros (int)
usuario_nombre = "Carlos"
usuario_edad = 30
print("3.1 Tipo nombre:", type(usuario_nombre), "| Tipo edad:", type(usuario_edad))
# Ejemplo 2: Listas (list) y Tuplas (tuple)
colores = ["rojo", "verde", "azul"]
coordenadas = (10.5, 20.8)
print("3.2 Lista:", colores, "| Tupla:", coordenadas)
# Ejemplo 3: Diccionarios (dict) y Booleanos (bool)
usuario_datos = {"nombre": "Sofia", "rol": "admin"}
activo = True
print("3.3 Diccionario:", usuario_datos, "| Booleano:", activo)
# ==========================================
# 4. OPERADORES ARITMÉTICOS
# ==========================================
# Ejemplo 1: Suma (+) y Resta (-)
suma = 15 + 5
resta = 20 - 8
print("4.1 Suma (15+5):", suma, "| Resta (20-8):", resta)
# Ejemplo 2: Multiplicación (*) y División (/)
producto = 4 * 3
division = 10 / 2
print("4.2 Multiplicación (4*3):", producto, "| División (10/2):", division)
# Ejemplo 3: Módulo (%), Potencia (**) y División Entera (//)
residuo = 10 % 3
potencia = 2 ** 3
div_entera = 7 // 2
print("4.3 Módulo (10%3):", residuo, "| Potencia (2**3):", potencia, "| Div. Entera (7//2):", div_entera)
# ==========================================
# 5. OPERADORES DE COMPARACIÓN
# ==========================================
num1, num2 = 5, 10
print("5.1 Igualdad (5 == 10):", num1 == num2)
print("5.1 Diferencia (5 != 10):", num1 != num2)
val1, val2 = 15, 8
print("5.2 Mayor que (15 > 8):", val1 > val2)
print("5.2 Menor que (15 < 8):", val1 < val2)
n1, n2 = 10, 10
print("5.3 Mayor o igual (10 >= 10):", n1 >= n2)
print("5.3 Menor o igual (10 <= 10):", n1 <= n2)
# ==========================================
# 6. OPERADORES LÓGICOS
# ==========================================
var_and = 5
print("6.1 Operador AND (5 > 3 y 5 < 10):", var_and > 3 and var_and < 10)
var_or = 12
print("6.2 Operador OR (12 < 5 o 12 > 10):", var_or < 5 or var_or > 10)
es_mayor = True
print("6.3 Operador NOT (inversión de True):", not es_mayor)
print("------------------ Nicole Robles NC 0120 ------------------")