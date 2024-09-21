import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import r_regression

# Valores de X (domínio) - treino
X = np.array([[10],[15],[20],[25],[30]])

# Valores de Y (subconjunto img) 
Y = np.array([1003,1005,1010,1011,1014])

# Valores aleatórios para previbilidade
P = np.array([[40],[50],[60]])

# Regressao linear obj com SciKitLearn
model = LinearRegression()
model.fit(X,Y)
fx=f"A função f(x) é y={model.intercept_} + {model.coef_}x"
previsao = model.predict(P)

print("\n************************\n")
print(f" Coeficiente linear B de y = a + bx => {model.coef_}")
print(f" Coeficiente angular A de y = a + bx => {model.intercept_}")
print(f" Coeficiente de Correlação {r_regression(X,Y)}")
print(f" Previsão usando o modelo:    {fx} ")
print(f" Score: {model.score(X,Y)}")
print(f" Previsão {P} = {previsao}",end=' ')
print("\n************************\n")