# Definindo as funções para calcular as métricas

def calcular_acuracia(vp, vn, fp, fn):
    return (vp + vn) / (vp + vn + fp + fn)

def calcular_sensibilidade(vp, fn):
    return vp / (vp + fn)

def calcular_especificidade(vn, fp):
    return vn / (vn + fp)

def calcular_precisao(vp, fp):
    return vp / (vp + fp)

def calcular_f_score(precisao, sensibilidade):
    if precisao + sensibilidade == 0:
        return 0
    return 2 * (precisao * sensibilidade) / (precisao + sensibilidade)

# Definindo os valores da matriz de confusão
vp = 50  # Verdadeiros Positivos
vn = 30  # Verdadeiros Negativos
fp = 10  # Falsos Positivos
fn = 5   # Falsos Negativos

# Calculando as métricas
acuracia = calcular_acuracia(vp, vn, fp, fn)
sensibilidade = calcular_sensibilidade(vp, fn)
especificidade = calcular_especificidade(vn, fp)
precisao = calcular_precisao(vp, fp)
f_score = calcular_f_score(precisao, sensibilidade)

# Exibindo os resultados
print(f"Acurácia: {acuracia:.2f}")
print(f"Sensibilidade: {sensibilidade:.2f}")
print(f"Especificidade: {especificidade:.2f}")
print(f"Precisão: {precisao:.2f}")
print(f"F-score: {f_score:.2f}")
