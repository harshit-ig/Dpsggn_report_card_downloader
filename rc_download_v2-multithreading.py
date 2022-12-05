import os , time
import requests
from threading import Thread

if not os.path.exists('report_card'):
    os.mkdir('report_card')

flag = 0

def download(url: str, dest_folder: str):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    filename = url.split('/')[-1].replace("~", "_")
    file_path = os.path.join(dest_folder, filename)

    r = requests.get(url, stream=True)
    if r.ok:
        
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
        time.sleep(3)
        print('\n'*4)
        print("Saving To: ", os.path.abspath(file_path))
        global flag
        flag =1
        print('\n'*4)

while True:
	if flag == 1:
		time.sleep(20)
		continue
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

		rccode= list(range(999,99999)) [::-1]

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
					global flag
					flag = 0
					break
		
		threadlist = []
		for i in range (100):
			t1 = Thread(target=multi2)
			t1.start()
			threadlist.append(t1)