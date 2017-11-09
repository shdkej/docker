from bs4 import BeautifulSoup
import xlsxwriter,re,urllib2,base64,requests

def spider(max_pages):
	page = 1
	head = ['id','tr-mfgPartNumber','product type','tr-unitPrice','tr-unitPrice','tr-vendor','tr-image','tr-vendor']
	url = 'https://www.digikey.kr/products/ko/sensors-transducers/optical-sensors-photointerrupters-slot-type-logic-output/547/page/' + str(page)
	while page <= max_pages:
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text,'lxml')
		att = []
		for i in range(0,len(head)):
			for company in soup.find_all('td',head[i]):
				if(head[i]==head[6]):
					imgsrc = company.find('img')['src']
					imgs = "http:" + imgsrc
					image = urllib2.urlopen(imgs)
					image_64 = base64.encodestring(image.read())
					att.append(image_64)
				elif(head[i]==head[0]):
					writeexcel('d',i)
				elif(head[i]==head[2]):
					writeexcel('stockable',i)
				else:
					for content in company.stripped_strings:
						att.append(content)
			writeexcel(att,i)
			del att[:]
		page += 1
	

start = [1,1,1,1,1,1,1,1,1]
def writeexcel(att,num):
	title = ['id','name','product type','price','cost','vendor','image','internal reference']
	if start[0]==1:
		for i in range(0,len(title)):
			worksheet.write(0,i,title[i])
	if type(att)==list:
		for j in range(0,len(att)):
			worksheet.write(start[num],num,att[j-1])
			start[num] += 1
	else:
		worksheet.write(start[num],num,att)
		start[num] += 1

def clean_text(text):
	cleaned_text = re.sub('[a-zA-Z]','',text)
	cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\)\'\"]','',cleaned_text)
	return cleaned_text


if __name__ == '__main__':
	workbook = xlsxwriter.Workbook('test1.xlsx')
	worksheet = workbook.add_worksheet()
	spider(10)
	workbook.close()
#	writeexcel()
