import os

ch=1
while(ch!=5):
	print("1.Add the details and capture the face of the student\n2.Start identifing the faces\n3.Start detecting RFID tags\n4.Generate the final result\n5.exit")
	ch=int(input())
	if(ch==1):
		os.system("python3 add_student.py")
		user=input("Enter User ID: ")
		os.system("python3 create_person.py "+user)
		os.system("python3 add_person_faces.py "+user)
	if(ch==2):
		os.system("python3 train.py")
		os.system("python3 get_status.py")
		pic="test.jpg"
		os.system("python3 detect.py "+pic)
		os.system("python3 spreadsheet.py")
		os.system("python3 identify.py")
	if(ch==3):
		os.system("python3 rfid.py")
	if(ch==4):
		os.system("python3 result_spreadsheet.py")
		os.system("python3 results.py")
	if(ch<1 & ch>5):
		print("Please enter a valid input")
		
