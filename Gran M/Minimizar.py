# Jersson Javier Ortegate Banderas 20201020139

# Se importa linprog de la libreria de scipy
from scipy.optimize import linprog

# Valores de la funcion que se quiere minimizar
C = [120, 200]
# Matriz con las restricciones:
A = [[1, 1], [60, 24]]
# Coeficientes de la funcion
b = [65, 3000]
# Limites de las variables
X0_bounds = [23, None]
X1_bounds = [20, None]

# Calculo mediante el metodo de la gran M (se establece como igualdad (eq), y que una de las restricciones es de igualdad)
res = linprog(C, A_eq=A, b_eq=b, bounds=[X0_bounds, X1_bounds])

# Se imprime el resultado
print("Toma el valor minimo: ")
print(res['fun'])
print("En el punto: ")
print(res['x'])
