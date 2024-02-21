# Programa para calcular IMC
# Desenvolvido por Everton

print("****************************")
print("*     CALCULADORA DE IMC   *")
print("****************************")
print()

#Criação das variáveis
nome = ""
peso = 0
altura = 0.0
imc = 0.0

#Entrada dos dados

nome = input("Digite o seu nome: ")
peso = int(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

#Processar os valores para obter o IMC

imc = peso / altura **2
if imc < 18.5:
    situacao = "Abaixo do peso"

elif imc >= 18.5 and imc < 25:
    situacao = "Peso normal"
elif imc >= 25 and imc < 30:
    situacao = "Sobrepeso"
elif imc >= 30 and imc < 34:
    situacao = "Obesidade Grau I"
elif imc >= 35 and imc < 39:
    situacao = "Obesidade Grau II"
elif imc <= 40:
    situacao = "Obesidade Grau III ou Mórbida"

#Saída do processamento
print()
print("******************")
print("*    RESULTADO    *")
print("*                 *")
print("NOME: " + nome)
print("PESO: " + str(peso)+ "Kg")
print("ALTURA: " + str(altura) + "m")
print("IMC: " + str(imc))
