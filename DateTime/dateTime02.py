import datetime

now = datetime.datetime.now()
delta = datetime.timedelta(days=6748)

nova_data = now - delta
formato = '%d/%m/%Y'

nova = nova_data.strftime(formato)
print(nova)
