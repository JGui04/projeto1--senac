"""
Crie um programa que após receber o nome, cargo, departamento,salarioBase
realize um reajuste salarial d 8.5% para salarioBase até 1600 e reajuste de
7% para salario maior que 1600.
No final imprima nome, cargo e o novo salario
"""
# Variáveis nome, cargo e o salarioBase.
nome = str(input("Digite seu nome:\n"))
cargo = str(input("\nDigite seu cargo:\n"))
dept = str(input("\nDigite seu departamento:\n"))
salarioBase = int(input("\nDigite seu salario:\n"))

# Processor a ser feito de acordo com o valor atribuido no salarioBase.
if salarioBase < 1600:
   novoSalario =  salarioBase*1.085
# Se for veradeiro imprime
   print(f"\n Parabéns {nome}, e seu cargo: {cargo}, você teve um aumento de 8,5% e seu novo salário é {novoSalario}.\n")

# Caso a primeira seja falso
else:
    novoSalario = salarioBase*1.070
    # Imprime
    print(f"\n Parabéns {nome},e seu cargo: {cargo}, você teve um aumento de 7% e seu novo salário é {novoSalario}.\n")