from time import sleep

while True:

    print("""-=-=-=-= Calculadora -=-=-=-=
(1) Fazer calculo
(2) Sair""")
    escolha = int(input("Escolha: "))
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    if escolha == 1:

        primeiro = int(input("Primeiro numero:"))
        segundo = int(input("Segundo numero:"))

        if primeiro > 100 or segundo > 100:

            print("Apenas numeros de 0 até 100")

            break
        
        else: 

            print(f"""-=-=-=-=  Resultado do calculo  -=-=-=-=
                  
Soma: {primeiro} + {segundo} = {primeiro + segundo}
Subtração: {primeiro} - {segundo} = {primeiro - segundo}
Divisão: {primeiro} / {segundo} = {primeiro / segundo}
Multiplicação: {primeiro} * {segundo} = {primeiro * segundo} """)
            
            sleep(5)
            print("Voltando ao inicio")
            sleep(1)
            
            continue

    else:

        print("Saindo...")
        sleep(0.5)
        print("Saindo..")
        sleep(0.5)
        print("Saindo.")
        sleep(0.5)
        print("Saindo")
        sleep(0.5)
        break