import datetime

formato = '%d/%m/%Y'
minha_data = '06/11/2023'
now = datetime.datetime.strptime(minha_data, formato)
print(now)

#now = datetime.datetime.now()
#now = datetime.datetime(2023,11,6,9,1,40)
#now = datetime.date(2023,11,6)
#now = datetime.time(8,47)
#formato = '%d/%m/%Y %H:%M:%S'
#print(now.strftime(formato))
