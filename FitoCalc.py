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

pi2 = (math.pi / 2)
pi4 = (math.pi / 4)
pi6 = (math.pi / 6)
pi12 = (math.pi / 12)
pi16 = (math.pi / 16)
axbxc = (a * b * c)
abc2 = ((a * b) + (b * c) + (a * c))

def forma1(a):
  V = pi6 * (a**3)
  A = math.pi * (a**2)
  return V, A

def forma2(a, b):
  V = pi6 * (b**2) * a
  raizdifquad = math.sqrt((a**2) - (b**2))
  A = ((math.pi*b) / 2) * (b + ((a**2) / raizdifquad) * math.asin(raizdifquad / a))
  return V, A

def forma3(a, b, c):
  V = pi6 * axbxc
  somabc = b + c
  raizdifquad = math.sqrt((4 * (a**2)) - (somabc**2))
  A = pi4 * somabc * ((somabc / 2) + ((2 * (a**2)) / raizdifquad) * math.asin(raizdifquad / (2 * a)))
  return V, A

def forma4(a, c):
  V = pi4 * (a**2) * c
  A = math.pi * a * ((a / 2) + c)
  return V, A

def forma5(a, b):
  V = math.pi * (b**2) * ((a / 4) - (b / 12))
  A = math.pi * a * b
  return V, A

def forma6(a, b):
  V = pi4 * (b**2) * (a - (b / 3))
  A = math.pi * b * (a - (((4 - math.sqrt(3)) / 4) * b))
  return V, A

def forma7(a, b):
  V = pi12 * a * (b**2)
  A = pi4 * b * (b + math.sqrt(4 * (a**2) + (b**2)))
  return V, A

def forma8(a, b):
  V = pi12 * a * (b**2)
  A = pi2 * b * math.sqrt((a**2) + (b**2))
  return V, A

def forma9(a, b):
  V = pi4 * a * (b**2)
  A = pi4 * (b**2) * (b + math.sqrt((2 * (a**2) - (a * b) + (b**2)) / 2))
  return V, A

def forma10(a, b, c):
  V = axbxc
  A = 2 * abc2
  return V, A

def forma11(a, b, c):
  V = pi4 * axbxc
  A = pi4 * abc2
  return V, A

def forma12(a, b, c):
  V = pi4 * axbxc
  A = pi2 * abc2
  return V, A


#relacionando as medidas com as funções para cálculo
funcoes = {
    1: lambda row: forma1(row['a']),
    2: lambda row: forma2(row['a'], row['b']),
    3: lambda row: forma3(row['a'], row['b'], row['c']),
    4: lambda row: forma4(row['a'], row['c']),
    5: lambda row: forma5(row['a'], row['b']),
    6: lambda row: forma6(row['a'], row['b']),
    7: lambda row: forma7(row['a'], row['b']),
    8: lambda row: forma8(row['a'], row['b']),
    9: lambda row: forma9(row['a'], row['b']),
    10: lambda row: forma10(row['a'], row['b'], row['c']),
    11: lambda row: forma11(row['a'], row['b'], row['c']),
    12: lambda row: forma12(row['a'], row['b'], row['c']),
}
resultados = df.apply(lambda row: funcoes[row['formato']](row), axis=1)

#escrevendo no arquivo
df['volume'] = resultados.apply(lambda x: x[0])
df['area']   = resultados.apply(lambda x: x[1])