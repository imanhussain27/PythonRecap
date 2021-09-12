print ("Hello student! Here, you will be able to see information about your course depending on the course number you enter.")

Dict={"CS101":["3004","Haynes","8:00AM"],
"CS102":["4501","Alvarado","9:00AM"],
"CS103":["6755","Rich","10:00AM"],
"NT110":["1244","Burke","11:00AM"],
"CM241":["1411","Lee","1:00PM"]}

print("Below, you will be asked to enter your course number. The course's information will be displayed accordingly.")

course_number=input("Please enter your course number here: ")
print("Room Number: ",Dict[course_number][0])
print("Instructor Name: ",Dict[course_number][1])
print("Meeting Time: ",Dict[course_number][2])

codes={"A":"1","B":"2","C":"3","D":"4","E":"5","F":"6","G":"7","H":"8","I":"9","J":"10","K":"11","L":"12","M":"13","N":"26","O":"14","P":"15",
"Q":"16","R":"17","S":"18","T":"19","U":"20","V":"21","W":"22","X":"23","Y":"24","Z":"25","a":"27","b":"28","c":"29","d":"30","e":"31","f":"32",
"g":"33","h":"34","i":"35","j":"36","k":"37","l":"38","m":"39","n":"40","o":"41","p":"42","q":"43","r":"44","s":"45","t":"46","u":"47","v":"48",
"w":"49","x":"50","y":"51","z":"52"}

outfile=open("info_security.txt","r")

read_outfile=outfile.read()

outfile.close()

encrypt_file=open("encrypt_file.txt","w")

for l in read_outfile:
    if l in codes:
        encrypt_file.write(codes[l])

encrypt_file.close()
