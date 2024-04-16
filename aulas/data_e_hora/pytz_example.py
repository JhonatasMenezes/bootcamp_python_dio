import pytz 
from datetime import datetime

data_oslo = datetime.now(pytz.timezone("Europe/Oslo"))
data_sao_paulo = datetime.now(pytz.timezone("America/Sao_Paulo"))


print(data_oslo)
print(data_sao_paulo)
