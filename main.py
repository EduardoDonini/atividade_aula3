import statistics

def calcular_desvio_padrao(empresas):
    return statistics.stdev(empresas)

def calcular_moda(empresas):
    return statistics.mode(empresas)

def calcular_media(empresas):
    return sum(empresas) / len(empresas)

def calcular_variancia(empresas):
    return statistics.variance(empresas)


def analise_salario(*empresas):
    resultados = []
    for empresa in empresas:
        desvio_padrao = calcular_desvio_padrao(empresa)
        moda = calcular_moda(empresa)
        media = calcular_media(empresa)
        variancia = calcular_variancia(empresa)
        
        resultados.append((desvio_padrao, moda, media, variancia))
    
    return resultados



empresa1 = [1000,6000,1200,8000,1400]

empresa2 = [5000,4000,3000,2000,7000]

empresa3 = [1200,1300,8000,3000,15000]

empresa4 = [1400,1750,2000,4500,5900,7000]

empresa5 = [1400,1750,2000,4500,5900,7000]

resultado_empresa1 = analise_salario(empresa1)
resultado_empresa2 = analise_salario(empresa2)
resultado_empresa3 = analise_salario(empresa3)
resultado_empresa4 = analise_salario(empresa4)
resultado_empresa5 = analise_salario(empresa5)

print("------Análise da empresa 1------")
print(f"Desvio Padrão: {resultado_empresa1[0][0]}")
print(f"Moda: {resultado_empresa1[0][1]}")
print(f"Média: {resultado_empresa1[0][2]}")
print(f"Variância: {resultado_empresa1[0][3]}")
print()

print("------Análise da empresa 2------")
print(f"Desvio Padrão: {resultado_empresa2[0][0]}")
print(f"Moda: {resultado_empresa2[0][1]}")
print(f"Média: {resultado_empresa2[0][2]}")
print(f"Variância: {resultado_empresa2[0][3]}")
print()

print("------Análise da empresa 3------")
print(f"Desvio Padrão: {resultado_empresa3[0][0]}")
print(f"Moda: {resultado_empresa3[0][1]}")
print(f"Média: {resultado_empresa3[0][2]}")
print(f"Variância: {resultado_empresa3[0][3]}")
print()

print("------Análise da empresa 4------")
print(f"Desvio Padrão: {resultado_empresa4[0][0]}")
print(f"Moda: {resultado_empresa4[0][1]}")
print(f"Média: {resultado_empresa4[0][2]}")
print(f"Variância: {resultado_empresa4[0][3]}")
print()

print("------Análise da empresa 5------")
print(f"Desvio Padrão: {resultado_empresa5[0][0]}")
print(f"Moda: {resultado_empresa5[0][1]}")
print(f"Média: {resultado_empresa5[0][2]}")
print(f"Variância: {resultado_empresa5[0][3]}")
print()

# Escolheria a empresa 2 pelo fato da média do salário ser muito boa e o desvio padrão ser o menor.
