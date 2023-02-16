# coding: utf-8

import socket
import time
import os
import platform   #recevoir os
import shutil	#temperature
import psutil

infini = 1

nom_hote_serveur = "rt202p15lin"	#machine hote Saisir l'ip ou l'alias du serveur
port_d_ecoute_serveur = 1143		#port socket

nomMachine = socket.gethostname()	#Nom machine
systeme = platform.system()			#OS 

while infini == 1:
	connexion_serveur  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#connection au serveur
	connexion_serveur.connect((nom_hote_serveur, port_d_ecoute_serveur))
	
	temperature = '30'						# Temperature En cours de travail
	usageCpu = str(psutil.cpu_percent(3))	# % CPU utilisé
	ram = psutil.virtual_memory()			# recuperation information ram 
	ramtotal = str(ram.total // (2**30))	
	rampercent = str(ram.percent)			
	
	totaldisque, used, free = shutil.disk_usage("/")	#information sur les disques dur
	totaldisque = str(totaldisque // (2**30))
	used = str(used // (2**30))
	free = str(free // (2**30))
	
	#Envoit des information au serveur
	connexion_serveur.send(nomMachine.encode() + b"-" + systeme.encode() + b"-" + temperature.encode() + b"-" + totaldisque.encode() + b"-" + used.encode() + b"-" + free.encode() + b"-" + usageCpu.encode() + b"-" + ramtotal.encode() + b"-" + rampercent.encode())
	connexion_serveur.close()	#Fermeture du socket
	time.sleep(10) #Envoit les information toute les 10 sec


#connexion_serveur.close()	fermeture
