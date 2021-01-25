#On importe de la librairie netmiko "ConnectHandler"

from netmiko import ConnectHandler

#Configuration des devices auxquels on souhaite accéder via leurs adresses IP, username, et mots de passes
iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.130',
    'username': 'osama',
    'password': 'cisco',
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.131',
    'username': 'osama',
    'password': 'cisco',
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.132',
    'username': 'david',
    'password': 'cisco',
}

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.133',
    'username': 'osama',
    'password': 'cisco',
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.134',
    'username': 'osama',
    'password': 'cisco',
}

#Ouverture du fichier "iosv_l2_accès" sous le nom de "f", lines = reçoit lire f et séparer les lignes

with open('iosv_l2_accès') as f:
        lines = f.read().splitlines()
print (lines)

#La variable all_devices reçoit les switchs auxquels elle devra envoyer ce script
all_devices = [iosv_l2_s5, iosv_l2_s4, iosv_l2_s3]

#Boucle pour tous les devices de la variable all_devices, on connecte le docker aux devices)
#output reçoit la commande "envoyer directement en conf t le contenu de la commande lines)
#afficher output
 
for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)

#Ouverture du fichier "iosv_l2_principaux" sous le nom de "f", lines = reçoit lire f et séparer les lignes
with open('iosv_l2_principaux') as f:
    lines = f.read().splitlines()
print (lines)

#La variable all_devices reçoit les switchs auxquels elle devra envoyer ce script
all_devices = [iosv_l2_s2, iosv_l2_s1]

#Boucle pour tous les devices de la variable all_devices, on connecte le docker aux devices)
#output reçoit la commande "envoyer directement en conf t le contenu de la commande lines)
#afficher output
for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)
