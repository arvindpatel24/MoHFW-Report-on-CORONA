import requests as rq
import bs4
import re

try:
	user_agent = {'User-agent': 'Mozilla/5.0'}
	req=rq.get('https://www.mohfw.gov.in/',headers=user_agent)
	soup = bs4.BeautifulSoup(req.content, 'html.parser')

	table = soup.findAll('table', attrs = {'class':'table table-striped table-dark'})
	gist = soup.findAll('ol', attrs = {'dir':'ltr'})

	tr = []
	for t in table:
		x = t.findAll('tr')
		tr.append(x)
	States,Indian,Foreign,Cured,Death = [],[],[],[],[]
	for i in range(1,len(tr[0])-1):
	    States.append(tr[0][i].findAll('td')[1].text)
	    Indian.append(tr[0][i].findAll('td')[2].text)
	    Foreign.append(tr[0][i].findAll('td')[3].text)
	    Cured.append(tr[0][i].findAll('td')[4].text)
	    Death.append(tr[0][i].findAll('td')[5].text)

	print("\n\n***************CORONA-REPORT***************")
	print("\t\t1.Summary")
	print("\t\t2.Search By State Name")
	print("\t\t3.Complete State-Wise Report")
	choice = int(input())
	if(choice == 1):
		for i in range(5):
			print(gist[0].findAll('p')[i].find('strong').text)
	elif(choice == 2):
		print("Name of State : ")
		found = False
		city_name = input()
		for i in range(len(States)):
		    if re.search(city_name,States[i], re.IGNORECASE):
		    	found = True
		    	print("\t\tState-",States[i],'| Indian-',Indian[i],' |Foreign-',Foreign[i],' |Cured-',Cured[i],' |Death-',Death[i])
		if(not found):
			print("Great:)  Your state isn't affected by Corona. But still 'BE SAFE BE HEALTHY'  ")
	elif(choice == 3):
		print(('{0:40}{1:10}{2:10}{3:10}{4:10}'.format('States','Indian','Foreign','Cured','Death')))
		for i in range(20):
			print(('{0:40}{1:10}{2:10}{3:10}{4:10}'.format(States[i],Indian[i],Foreign[i],Cured[i],Death[i])))


except:
	print("Servor Error")



