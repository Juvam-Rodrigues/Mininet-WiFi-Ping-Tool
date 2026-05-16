       
def pingTodos(net):
    total = 0
    sucesso = 0
    for hostOrigem in net.hosts:

        for hostDestino in net.hosts:
            ipOrigem = hostOrigem.cmd("hostname -I").strip().split()[0]

            if hostOrigem != hostDestino:

                ipDestino = hostDestino.cmd("hostname -I").strip().split()[0]

                print(f"{hostOrigem} - {ipOrigem} ---> {hostDestino} - {J}: ", end="")

                resultado = hostOrigem.cmd(f"ping -c 1 {ipDestino}")
                total += 1

                if "1 received" in resultado:
                    print("OK") 
                    sucesso += 1
                else:
                    print("FALHOU")
        print("")

    if total > 0:
        porcentagem = (sucesso / total) * 100
    else:
        porcentagem = 0

    print(f"Taxa de sucesso: {porcentagem:.2f}% ({sucesso}/{total})")