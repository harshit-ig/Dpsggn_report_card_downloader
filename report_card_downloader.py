import os
import requests


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
    else:  # HTTP status code 4XX/5XX
        print("Download failed: status code {}\n{}".format(r.status_code, r.text))








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
	year = int(input("""
	
class 9th : 2019
class 11th : 2021

	"""))
	rccode= 999
	initdirlen = len(os.listdir("report_card"))
	
	while True:
		url = f"https://www.dpsggncampuscare.org/ExamPDF/RC_{rccode}~TERMII~{year}~{regno}.pdf"

		print(f"Now trying with RC code : {rccode}")
		download(url, dest_folder="report_card")
		if len(os.listdir("report_card"))  != initdirlen:
			break
		else:
			rccode +=1