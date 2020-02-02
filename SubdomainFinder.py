import sys
import os
import dns.resolver

#################
## PREPARATION ##
################# 

domain = input("Input the Domain Name >>> ")
list_path = "Subdomain.txt"


#open wordlist
try:
	list_file = open(list_path)
	lines = list_file.read().splitlines()
except:
	print("File {} not found".format(list_path))
	sys.exit(1)

#################
## BRUTE FORCE ##
#################

for line in lines:
	subdomain = line + "." + domain
	try:
		answers = dns.resolver.query(subdomain, 'a')
		for result in answers:
			print ("[+] {} {}".format(subdomain, result))
	except:
		pass

	#not shubham