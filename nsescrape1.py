from bs4 import BeautifulSoup
import requests
import os

res = requests.get("https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=-10006&symbol=NIFTY&symbol=NIFTY&instrument=-&date=-&segmentLink=17&symbolCount=2&segmentLink=17")
soup = BeautifulSoup(res.text, 'lxml')

rows = soup.find_all('table', {'id':'octable'})
# print(len(rows))
wf = './scrapefile2.txt'
write_var = open(wf, 'w');
data_list = []
for td in range(0, len(rows)):
	table_td = rows[td].find_all('tr')
	#print(table_td)
	for td2 in range(2, len(table_td)-2):
		td3 = table_td[td2]
		# print(td3)
		td4 = td3.find_all('td')
		# for td_data in range(1, 2):
		#print(td4[1])
		#oip = int(td4[1].text)
		oip = td4[1].text
		lt = td4[15].text
		# print("oip is "+oip+'---'+"lt is "+lt)
		if(oip != "-" and lt != "-"):
			# print(int(oip.replace(',', ''))*int(lt.replace(',', '')))
			product = int(oip.replace(',', ''))*int(lt.replace(',', ''))
			print(product)
			data_list.append(product)
			write_var.write(str(product))
			write_var.write('\n')
		else:
			print('NA')
			product = "NA"
			# data_list.append(product)
			write_var.write(product)
			write_var.write('\n')
		
		
			# table_td2 = td_data.find_all('td')
			# print(len(table_td2))
		print('-----------------------------')
		data_list.sort()
print(data_list)


# wf = './scrapefile2.txt'
# write_var = open(wf, 'w');
# for row_data in rows:
	# print (row_data.children[1].textContent.trim(" "))
	# print ()
	# write_var.write(row_data.text+'\n')
	
write_var.close()
os.startfile('F:\\Pyspace\\scrapefile2.txt')