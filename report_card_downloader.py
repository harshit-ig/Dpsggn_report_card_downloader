import os
import requests
from threading import Thread

if not os.path.exists('report_card'):
    os.mkdir('report_card')

def download(url: str, dest_folder: str):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    filename = url.split('/')[-1].replace("~", "_")
    file_path = os.path.join(dest_folder, filename)

    r = requests.get(url, stream=True)
    if r.ok:
        print("saving to", os.path.abspath(file_path))
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())



print("""RC_(RC-CODE)_(TERMI/TERMII)_(YEAR)_(REGISTRATION-NUMBER).pdf

You Can Find Your RC Code In The Filename Of Your Report Card.
""")





rccodeavailable = input("Do you have your RC code(Y/N): ")




if rccodeavailable.upper() == "Y":
	rccode = int(input("Enter Your RC Code: "))
	regno = int(input("Enter Your Registration Number: "))
	year = int(input("""
	
For Class 9th Report Card : 2019
For Class 11th Report Card : 2021

	"""))
	url = f"https://www.dpsggncampuscare.org/ExamPDF/RC_{rccode}~TERMII~{year}~{regno}.pdf"
	download(url, dest_folder="report_card")
	
else:
	regno = int(input("Enter Your Registration Number: "))
	year = int(input(
"""
class 9th : 2019
class 11th : 2021

"""))

	rccode= list(range(999,99999) )[::-1]

	def ds ():
		global rccode
		return rccode.pop()


	initdirlen = len(os.listdir("report_card"))
	

	def multi(rccode):
		global year
		global regno
		url = f"https://www.dpsggncampuscare.org/ExamPDF/RC_{rccode}~TERMII~{year}~{regno}.pdf"
		download(url, dest_folder="report_card")
		print(f'now trying with rc code {rccode}')
	
	def multi2():
		for _ in range(2000):
			multi(ds())
			if len(os.listdir("report_card"))  != initdirlen:
				break
		

	t1 = Thread(target = multi2)
	t2 = Thread(target = multi2)
	t3 = Thread(target = multi2)
	t4 = Thread(target = multi2)
	t5 = Thread(target = multi2)
	t6 = Thread(target = multi2)
	t7 = Thread(target = multi2)
	t8 = Thread(target = multi2)
	t9 = Thread(target = multi2)
	
	
	t11 = Thread(target = multi2)
	t22 = Thread(target = multi2)
	t33 = Thread(target = multi2)
	t44 = Thread(target = multi2)
	t55 = Thread(target = multi2)
	t66 = Thread(target = multi2)
	t77 = Thread(target = multi2)
	t88 = Thread(target = multi2)
	t99 = Thread(target = multi2)
	

	
	t1.start()
	t2.start()
	t3.start()
	t4.start()
	t5.start()
	t6.start()
	t7.start()
	t8.start()
	t9.start()

	t11.start()
	t22.start()
	t33.start()
	t44.start()
	t55.start()
	t66.start()
	t77.start()
	t88.start()
	t99.start()



	t1.join()
	t2.join()
	t3.join()
	t4.join()
	t5.join()
	t6.join()
	t7.join()
	t8.join()
	t9.join()


	t11.join()
	t22.join()
	t33.join()
	t44.join()
	t55.join()
	t66.join()
	t77.join()
	t88.join()
	t99.join()
