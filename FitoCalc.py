import pandas as pd
import math as math

#link para o arquivo
google_sheet_csv_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vT0A5AnVng08eEehtYZV11l8NW5Z4eMs1yHAPCm3zZj8Aq5O3zuj-2KohXz0H9qblzoHngC9W1p8vn1/pub?output=csv'

try:
    df = pd.read_csv(google_sheet_csv_url)
    print("Planilha carregada com sucesso!")
except Exception as e:
    print(f"Ocorreu um erro ao carregar a planilha: {e}")

#cálculo de volume e área
def forma1(a):
  V = (math.pi/6)*(a**3)
  A = math.pi*(a**2)
  return V, A

def forma2(a,b):
  V = (math.pi/6)*(b**2)*a
  raizdifquad = math.sqrt((a**2)-(b**2))
  A = ((math.pi*b)/2)*(b+((a**2)/raizdifquad)*math.asin(raizdifquad/a))
  return V, A

def forma3(a,b,c):
  V = (math.pi/6)*a*b*c
  somabc = b+c
  raizdifquad = math.sqrt((4*(a**2))-(somabc**2))
  A = (math.pi/4)*somabc*((somabc/2)+((2*(a**2))/raizdifquad)*math.asin(raizdifquad/(2*a)))
  return V, A

def forma4(a,c):
  V = (math.pi/4)*(a**2)*c
  A = math.pi*a*((a/2)+c)
  return V, A

#relacionando as medidas com as funções para cálculo
funcoes = {
    1: lambda row: forma1(row['a']),
    2: lambda row: forma2(row['a'], row['b']),
    3: lambda row: forma3(row['a'], row['b'], row['c']),
    4: lambda row: forma4(row['a'], row['c']),
}
resultados = df.apply(lambda row: funcoes[row['formato']](row), axis=1)

#escrevendo no arquivo
df['volume'] = resultados.apply(lambda x: x[0])
df['area']   = resultados.apply(lambda x: x[1])