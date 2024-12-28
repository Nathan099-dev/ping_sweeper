import subprocess
import platform
import ipaddress
from datetime import datetime
from colorama import Fore, init


init()
GREEN = Fore.GREEN
RED = Fore.RED
GRAY = Fore.LIGHTBLACK_EX

def ping_sweep(network):
    try:
        net = ipaddress.ip_network(network, strict=False)
        param = '-n' if platform.system().lower() == 'windows' else '-c'

        print('Iniciando ping sweep em: ' + str(datetime.now()))

        for ip in net.hosts():
            ip_str = str(ip)

            resuts = subprocess.run(['ping', param, '1', ip_str], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            if resuts.returncode == 0:
                print(f' {GREEN} host {ip_str} ativo')
            else:
                  print(f' {RED} host {ip_str} inativo')
                 
               

    except ValueError as e:
        pass

    except KeyboardInterrupt:
        print(f'{GRAY} Atalho CTRL + C Pressionado... Interrompendo programa')

if __name__ == "__main__":
        network = str(input('Digite o ip da sua rede:'))      

ping_sweep(network)







