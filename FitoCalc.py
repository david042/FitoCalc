import pandas as pd
import math as math

# link para o arquivo
google_sheet_csv_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vT0A5AnVng08eEehtYZV11l8NW5Z4eMs1yHAPCm3zZj8Aq5O3zuj-2KohXz0H9qblzoHngC9W1p8vn1/pub?output=csv'

try:
    df = pd.read_csv(google_sheet_csv_url)
    print("Planilha carregada com sucesso!")
except Exception as e:
    print(f"Ocorreu um erro ao carregar a planilha: {e}")

# cálculo de volume e área

pi2 = (math.pi / 2)
pi4 = (math.pi / 4)
pi6 = (math.pi / 6)
pi12 = (math.pi / 12)
abc2 = lambda a, b, c: (a * b) + (b * c) + (a * c)

def forma1(a):
  ''' esfera '''
  V = pi6 * (a**3)
  A = math.pi * (a**2)
  return V, A

def forma2(a, b):
  ''' esferóide prolado '''
  V = pi6 * (b**2) * a
  raizdifquad = math.sqrt((a**2) - (b**2))
  A = ((math.pi*b) / 2) * (b + ((a**2) / raizdifquad) * math.asin(raizdifquad / a))
  return V, A

def forma3(a, b, c):
  ''' elipsóide '''
  V = pi6 * (a * b * c)
  somabc = b + c
  raizdifquad = math.sqrt((4 * (a**2)) - (somabc**2))
  A = pi4 * somabc * ((somabc / 2) + ((2 * (a**2)) / raizdifquad) * math.asin(raizdifquad / (2 * a)))
  return V, A

def forma4(a, c):
  ''' cilindro '''
  V = pi4 * (a**2) * c
  A = math.pi * a * ((a / 2) + c)
  return V, A

def forma5(a, b):
  ''' cilindro com 2 semiesferas '''
  V = math.pi * (b**2) * ((a / 4) - (b / 12))
  A = math.pi * a * b
  return V, A

def forma6(a, b):
  ''' cilindro com 2 cones '''
  V = pi4 * (b**2) * (a - (b / 3))
  A = math.pi * b * (a - (((4 - math.sqrt(3)) / 4) * b))
  return V, A

def forma7(a, b):
  ''' cone '''
  V = pi12 * a * (b**2)
  A = pi4 * b * (b + math.sqrt(4 * (a**2) + (b**2)))
  return V, A

def forma8(a, b):
  ''' duplo cone '''
  V = pi12 * a * (b**2)
  A = pi2 * b * math.sqrt((a**2) + (b**2))
  return V, A

def forma9(a, b):
  ''' cone + meia esfera '''
  V = pi4 * a * (b**2)
  A = pi2 * (b**2) * (b + math.sqrt((2 * (a**2) - (a * b) + (b**2)) / 2))
  return V, A

def forma10(a, b, c):
  ''' caixa retangular '''
  V = (a * b * c)
  A = 2 * abc2(a, b, c)
  return V, A

def forma11(a, b, c):
  ''' prisma com base elíptica '''
  V = pi4 * (a * b * c)
  A = pi2 * abc2(a, b, c)
  return V, A

def forma12(a, b, c):
  ''' prisma elíptico com construção transapical '''
  V = pi4 * (a * b * c)
  A = pi2 * abc2(a, b, c)
  return V, A

def forma13(a, b, c):
  ''' prisma com base paralelograma '''
  V = (1 / 2) * (a * b * c)
  raizsomquad = math.sqrt((a**2) + (b**2))
  A = a * b + ((raizsomquad / 4) * c)
  return V, A

def forma14(a, b, c):
  ''' prisma semi-elíptico '''
  V = pi4 * (a * b * c)
  A = pi4 * abc2(a, b, c) + (a * c)
  return V, A

def forma15(a, b, c):
  ''' prisma em forma de foice '''
  V = pi4 * (a * b * c)
  A = pi4 * abc2(a, b, c) + (a * c)
  return V, A

def forma17(a, b, c):
  ''' cimbelóide '''
  V = (2 / 3) * a * (c**2) * math.asin(b / (2 * c))
  raizdifquad = math.sqrt((a**2) - (4 * (c**2)))
  A = pi2 * a * c + (b * (c + (((a**2) / (2 * raizdifquad)) * math.asin(raizdifquad / a))))
  return V, A

def forma18(a, b, c):
  ''' prisma com base triangular '''
  V = (math.sqrt(3) / 4) * c * (a**2)
  A = 3 * a * c + ((math.sqrt(3) / 2) * (a**2))
  return V, A

def forma20(a, b, c):
  ''' prisma elíptico com inflação transapical '''
  V = pi4 * (a * b * c)
  A = pi2 * abc2(a, b, c)
  return V, A

def forma21(a, b, c):
  ''' gomfonemoide '''
  V = ((a * b) / 4) * (a + ((pi4 - 1) * b)) * math.asin(c / (2 * a))
  A = (b / 2) * ((2 * a) + (math.pi * a * math.asin(c / (2 * a))) + ((pi2 - 2) * b))
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
    13: lambda row: forma13(row['a'], row['b'], row['c']),
    14: lambda row: forma14(row['a'], row['b'], row['c']),
    15: lambda row: forma15(row['a'], row['b'], row['c']),
    17: lambda row: forma17(row['a'], row['b'], row['c']),
    18: lambda row: forma18(row['a'], row['b'], row['c']),
    20: lambda row: forma20(row['a'], row['b'], row['c']),
    21: lambda row: forma21(row['a'], row['b'], row['c']),
}
resultados = df.apply(lambda row: funcoes[row['formato']](row), axis=1)

#escrevendo no arquivo
df['volume'] = resultados.apply(lambda x: x[0])
df['area']   = resultados.apply(lambda x: x[1])