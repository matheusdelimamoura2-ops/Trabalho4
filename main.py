i = 0
j = 0
s = ""
t = ""
alinha_l = []
nome_arquivo = 'Sequencia1.txt'
def p(i,j):
    if s[i-1] == t[j-1]:
        print(s[i-1],t[j-1])
        return 1
    elif s[i-1] != t[j-1] :
        print(s[i-1],t[j-1])
        return -1
def entrada(s,t):
 g = -2
 p_1 = 1
 p_2 = -1
 a = input("Digite qual linha para s: ")
 b = input("Digite qual linha para t: ")
 c = input("Digite 1 se quer alinhamento global , digite 2 se quer o alinhamento semi-global ou digite 3 para alinhamento local: ")
 d = input("Digite 1 se quer  pontuação padrão ou 2 se quer pontuação de g persornalizada : ")
 if d == "2":
     g = int(input("Qual a  pontuação do g : "))
 with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
     for i, linha in enumerate(arquivo, start=1):
         if str(i) == a :
             s = linha.strip()
             print(s)
         if str(i) == b:
             t = linha.strip()
             print(t)
 return s,t,c,g,p_1,p_2
def similaridade(s,t,g) :
 m = len(s)
 n = len(t)
 matriz = [[0 for _ in range(n+1)] for _ in range(m+1)]
 for i in range(m+1):
  matriz[i][0] = i * g
 for j in range(n+1):
    matriz[0][j] = j * g
 for i in range(1,m+1):
    for j in range(1,n+1):
        matriz[i][j] = max(matriz[i-1][j] + g , matriz[i][j-1] + g, matriz[i-1][j-1] + p(i,j))
 for linha in matriz:
  print(" ".join(f"{num:>5}" for num in linha))
 return matriz
def similaridade_semiglobal(s,t,g) :
 m = len(s)
 n = len(t)
 matriz = [[0 for _ in range(n+1)] for _ in range(m+1)]
 for i in range(1,m+1):
    for j in range(1,n+1):
        matriz[i][j] = max(matriz[i-1][j] + g , matriz[i][j-1] + g, matriz[i-1][j-1] + p(i,j))
 for linha in matriz:
  print(" ".join(f"{num:>5}" for num in linha))
 return matriz
def similaridade_local(s,t,g) :
 m = len(s)
 n = len(t)
 matriz = [[0 for _ in range(n+1)] for _ in range(m+1)]
 for i in range(1,m+1):
    for j in range(1,n+1):
        matriz[i][j] = max(0,matriz[i-1][j] + g , matriz[i][j-1] + g, matriz[i-1][j-1] + p(i,j))
 for linha in matriz:
  print(" ".join(f"{num:>5}" for num in linha))
 return matriz
def alinha(i,j,m_sim,) :
 global s,t,g
 alinha_s = ""
 alinha_t = ""
 if i == 0 and j == 0:
  return alinha_s,alinha_t
 elif i > 0 and m_sim[i][j] == m_sim[i-1][j] + g :
     alinha_s,alinha_t = alinha(i - 1, j, m_sim)
     alinha_s += s[i-1]
     alinha_t += "_"
 elif i > 0 and j > 0 and m_sim[i][j] == m_sim[i - 1][j - 1] + p(i,j) :
     alinha_s,alinha_t = alinha(i-1,j-1,m_sim)
     alinha_s += s[i-1]
     alinha_t += t[j-1]
 elif j > 0 and m_sim[i][j] == m_sim[i][j-1] + g :
    alinha_s,alinha_t = alinha(i,j-1,m_sim)
    alinha_s += "_"
    alinha_t += t[j-1]
 return alinha_s,alinha_t
def alinha_local(i,j,m_sim,) :
 global s,t
 alinha_s = ""
 alinha_t = ""
 if m_sim[i][j] == 0:
   return alinha_s,alinha_t
 elif i > 0 and m_sim[i][j] == m_sim[i-1][j] + g :
     alinha_s,alinha_t = alinha_local(i - 1, j, m_sim)
     alinha_s += s[i-1]
     alinha_t += "_"
 elif i > 0 and j > 0 and m_sim[i][j] == m_sim[i - 1][j - 1] + p(i,j) :
     alinha_s,alinha_t = alinha_local(i-1,j-1,m_sim)
     alinha_s += s[i-1]
     alinha_t += t[j-1]
 elif j > 0 and m_sim[i][j] == m_sim[i][j-1] + g :
    alinha_s ,alinha_t = alinha_local(i,j-1,m_sim)
    alinha_s += "_"
    alinha_t += t[j-1]
 return alinha_s,alinha_t
def alinha_semiglobal(i,j,m_sim) :
 global s,t,g,m,n
 alinha_s = ""
 alinha_t = ""
 if i == 0 and j == 0:
  return  alinha_s,alinha_t
 elif i == 0:
   alinha_s, alinha_t = alinha_semiglobal(i,j - 1, m_sim)
   alinha_s += "_"
   alinha_t += t[j-1]
 elif j == 0:
     alinha_s, alinha_t = alinha_semiglobal(i-1,j, m_sim)
     alinha_s +=  s[i-1]
     alinha_t += "_"
 elif i > 0 and j > 0 and m_sim[i][j] == m_sim[i - 1][j - 1] + p(i,j) :
     alinha_s,alinha_t = alinha_semiglobal(i-1,j-1,m_sim)
     alinha_s += s[i-1]
     alinha_t += t[j-1]
     print(i,j)
 elif i > 0 and m_sim[i][j] == m_sim[i-1][j] + g :
     alinha_s,alinha_t =  alinha_semiglobal(i - 1, j, m_sim)
     alinha_s += s[i-1]
     alinha_t += "_"
     print(i,j)
 elif j > 0 and m_sim[i][j] == m_sim[i][j-1] + g :
    alinha_s,alinha_t = alinha_semiglobal(i,j-1,m_sim)
    alinha_s += "_"
    alinha_t += t[j-1]
    print(i,j)
 if i == m and j == n :
    if i < len(s):
     while i <= len(s):
      alinha_s += s[i-1]
      alinha_t += "_"
      i += 1
    elif j < len(t):
     while i <= len(t):
      alinha_s += "_"
      alinha_t += t[j-1]
      i += 1
 return alinha_s,alinha_t
def m_pontuacao(m_sim,m,n) :
 global s,t
 m = len(s)
 n = len(t)
 c,d = 0,n
 print(m,n)
 maior = m_sim[0][n]
 for i in range(0,m+1):
  if m_sim[i][n] >= maior:
      maior = m_sim[i][n]
      c = i
      d = n
 for j in range(0,n+1):
  if m_sim[m][j] >= maior:
      maior = m_sim[m][j]
      c = m
      d = j
 return c,d
def m_pontuacao_local(m_sim,m,n) :
 a = (0.0,0)
 lista = []
 c,d = 0,0
 for i in range(1,m+1):
  for j in range(1,n+1):
   if max(m_sim[i][j],m_sim[c][d]) == m_sim[i][j]:
     a = (m_sim[i][j], i, j)
     c = i
     d = j
     if len(lista) < 3 :
      lista.append(a)
     else:
      lista.pop(0)
      lista.append(a)
 return lista[0][1],lista[0][2],lista[1][1],lista[1][2],lista[2][1],lista[2][2]
s,t,c,g,p_1,p_2 = entrada(s,t)
m = len(s)
n = len(t)
if c == "2":
 m_sim = similaridade_semiglobal(s,t,g)
 m,n = m_pontuacao(m_sim,m,n)
 alinha_s,alinha_t = alinha_semiglobal(m,n,m_sim)
 print(alinha_s)
 print(alinha_t)
elif c == "1":
 m_sim = similaridade(s,t,g)
 alinha_s,alinha_t = alinha(m, n,m_sim)
 print(alinha_s)
 print(alinha_t)
elif  c == "3":
 m_sim = similaridade_local(s,t,g)
 m,n,m_1,n_1,m_2,n_2 = m_pontuacao_local(m_sim,m,n)
 alinha_s,alinha_t = alinha_local(m,n,m_sim)
 alinha_l.append(alinha_s)
 alinha_l.append(alinha_t)
 alinha_s,alinha_t = alinha_local(m_1, n_1,m_sim)
 alinha_l.append(alinha_s)
 alinha_l.append(alinha_t)
 alinha_s,alinha_t = alinha_local(m_2, n_2,m_sim)
 alinha_l.append(alinha_s)
 alinha_l.append(alinha_t)
 for linha in alinha_l:
  print(linha)
