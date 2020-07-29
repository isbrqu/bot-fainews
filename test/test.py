from pedco import Pedco
from decouple import config

username = config('PEDCO_USERNAME')
password = config('PEDCO_PASSWORD')

p = Pedco()
p.login(username, password)
