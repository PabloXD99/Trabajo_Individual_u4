import re

path = "textou4.txt"

try:
	archivo = open(path,'r')
except:
	print("El archivo no se encuentra")
	quit()

texto = ""

for linea in archivo:
	texto += linea




#1	Variables válidas. Ejemplo: suma, i, cont7, etc.
regexvariables = r'(\b[A-Za-z0-9-_]+\s*[=])+'
resultvariables = re.findall(regexvariables,texto)
print("\n Las variables declaradas:\n", resultvariables)




#2	Enteros y decimales. 2.7, 3.1416, 0.2, etc.
regexentero = r'[+,-]?[0-9]+'
regexdecimal = r'[+,-]?[[0-9]*[.]]?[0-9]+'
resultentero = re.findall(regexentero,texto)
resultdecimal = re.findall(regexdecimal,texto)
print("\n Los numeros enteros son:\n", resultentero)
print("\n Los numeros decimales son:\n", resultdecimal)



#3	Operadores aritméticos (suma, resta, multiplicación, división, etc.)
regexparametrico = r'[\d+]+\s*[\+|\-|\*|\/]+\s*[\d+]+'
resultparametrico = re.findall(regexparametrico,texto)
print("\n Los operadores aritmeticos son:\n", resultparametrico)



#4	Operadores relacionales. (mayor, menor, igual, diferente, etc.)
regexrelacional = r'([A-Za-z0-9|a-z0-9]+\s*[|<|>|!=|<=|>=]=+\s*[A-Za-z0-9|a-z0-9])+'
resultrelacional = re.findall(regexrelacional, texto)
print("\n Los operadores relacionales son:\n", resultrelacional)



#5	Palabras reservadas.
regexreservada = r'\b(False|def|if|raise|None|del|import|return|True|elif|in|try|and|else|is|while|as|except|lambda|with|assert|finally|nonlocal|yield|break|for|not|class|from|or|continue|global|pass\s)+|\s[:]+'
resultreservada = re.findall(regexreservada,texto)
print("\n Las palabras reservadas son:\n", resultreservada)