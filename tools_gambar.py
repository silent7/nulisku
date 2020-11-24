import requests, json, os, pyfiglet, time
os.system('clear')
head = pyfiglet.figlet_format("Nulis.Py")
print (head)
print ("isi sesuai yang mau di tulis")
print
text = input("masukan text : ")
print ("proses....")
hubung = requests.get('https://salism3.pythonanywhere.com/nulis?text=' + text)
for i in json.loads(hubung.content)['images']:
	img = requests.get(i)
	open('/storage/emulated/0/gambar1.jpg', 'wb').write(img.content)
	print ("selesai!")
	time.sleep(1)
	print ("disimpan di (/storage/emulated/0/gambar1.jpg)")


#CodedByYonDev
#InspiredByJejakCyber