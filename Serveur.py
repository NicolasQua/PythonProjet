import socket
import psutil
import shutil

infini = 1

#Création d’un objet socket :
socket_ecoute = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#Liaison du socket d’écoute à un port :
port_d_ecoute = 1143
socket_ecoute.bind(('', port_d_ecoute))

while infini == 1:    #le programme tourne en boucle 
	#listening of the socket :
	socket_ecoute.listen()

	#accept connection from the client:
	connexion_client, adresse_client = socket_ecoute.accept()

	#show who's connected to the socket :
	print("Connexion de: " + str(adresse_client))
	
	#receieve the message of the client 
	message = connexion_client.recv(1024).decode('utf-8')
	
	
	#les informations sont mit dans une liste 
	message_split = message.split('-')
	
	#print (message)		#ligne de test pour voir le message brut 
	
	#on affiche la liste dans l'ordre convenu avec le client 
	print("Poste " + message_split[0] +   " connecté sous " + message_split[1] + " sous l'adresse IP " + str(adresse_client[0]))
	print("=-=-=-=-CPU-=-=--=-=\nTémpérature du CPU:" + message_split[2] + "° \nUtilisation du CPU: " + message_split[6] + "%")
	print("=-=-=-=-Disque-=-=-=-=\nEspace total:" + message_split[3] + " Gb \nEspace utilisé:" + message_split[4] +"Gb \nEspace libre :" + message_split[5] + "Gb")
	print("=-=-=-Mémoire vive-=-=-=-=-=\nEspace total:" + message_split[7] + " Gb \nUtilisation: " + message_split[8] + "%") 
	print("-----------------------------------------------------------------\n\n")
