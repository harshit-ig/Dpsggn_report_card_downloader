from concurrent.futures import thread
import os , time
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
        
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
        time.sleep(3)
        print('\n'*4)
        print("Saving To: ", os.path.abspath(file_path))
        print('\n'*4)

while True:
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
		t10 = Thread(target= multi2)
		t11 = Thread(target = multi2)
		t12 = Thread(target = multi2)
		t13 = Thread(target = multi2)
		t14 = Thread(target = multi2)
		t15 = Thread(target = multi2)
		t16 = Thread(target = multi2)
		t17 = Thread(target = multi2)
		t18 = Thread(target = multi2)
		t19 = Thread(target = multi2)
		t20 = Thread(target= multi2)
		t21 = Thread(target = multi2)
		t22 = Thread(target = multi2)
		t23 = Thread(target = multi2)
		t24 = Thread(target = multi2)
		t25 = Thread(target = multi2)
		t26 = Thread(target = multi2)
		t27 = Thread(target = multi2)
		t28 = Thread(target = multi2)
		t29 = Thread(target = multi2)
		t30 = Thread(target= multi2)
		t31 = Thread(target = multi2)
		t32 = Thread(target = multi2)
		t33 = Thread(target = multi2)
		t34 = Thread(target = multi2)
		t35 = Thread(target = multi2)
		t36 = Thread(target = multi2)
		t37 = Thread(target = multi2)
		t38 = Thread(target = multi2)
		t39 = Thread(target = multi2)
		t40 = Thread(target= multi2)
		

		
		t1.start()
		t2.start()
		t3.start()
		t4.start()
		t5.start()
		t6.start()
		t7.start()
		t8.start()
		t9.start()
		t10.start()
		t11.start()
		t12.start()
		t13.start()
		t14.start()
		t15.start()
		t16.start()
		t17.start()
		t18.start()
		t19.start()
		t20.start()
		t21.start()
		t22.start()
		t23.start()
		t24.start()
		t25.start()
		t26.start()
		t27.start()
		t28.start()
		t29.start()
		t30.start()
		t31.start()
		t32.start()
		t33.start()
		t34.start()
		t35.start()
		t36.start()
		t37.start()
		t38.start()
		t39.start()
		t40.start()
		

		t1.join()
		t2.join()
		t3.join()
		t4.join()
		t5.join()
		t6.join()
		t7.join()
		t8.join()
		t9.join()
		t10.join()
		t11.join()
		t12.join()
		t13.join()
		t14.join()
		t15.join()
		t16.join()
		t17.join()
		t18.join()
		t19.join()
		t20.join()
		t21.join()
		t22.join()
		t23.join()
		t24.join()
		t25.join()
		t26.join()
		t27.join()
		t28.join()
		t29.join()
		t30.join()
		t31.join()
		t32.join()
		t33.join()
		t34.join()
		t35.join()
		t36.join()
		t37.join()
		t38.join()
		t39.join()
		t40.join()