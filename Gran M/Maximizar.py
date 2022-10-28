# Jersson Javier Ortegate Banderas 20201020139

# Se importa linprog de la libreria de scipy
from scipy.optimize import linprog

# Valores de la funcion que se quiere maximizar (como se va a maximizar se le cambian los signos)
C = [-2, -4]
# Matriz con las restricciones:
A = [[4, 6], [2, 6], [0, 1]]
# Coeficientes de la funcion
b = [120, 72, 10]
# Limites de las variables
X0_bounds = [None, None]
X1_bounds = [None, None]

# Calculo mediante el metodo de la gran M
res = linprog(C, A_ub=A, b_ub=b, bounds=[X0_bounds, X1_bounds])

# Se imprime el resultado
print("Toma el valor maximo: ")
# Como se cambio los signos de la función para maximizarla se multiplica por -1 para que nos de el resultado correcto
print(-1*res['fun'])
print("En el punto: ")
print(res['x'])
