from pedco import Pedco
from pedco import Mechanical
from decouple import config

username = config('PEDCO_USERNAME')
password = config('PEDCO_PASSWORD')

m = Mechanical()
m.login(username, password)

p = Pedco()
p.login(username, password)

if olddis and newdis.author in teachers.names:
    same_url = (newdis.url == olddis.url)
    updated = (newdis.updated != olddis.updated)
    if (same_url and updated) or not same_url:
        if not same_url:

pedco.screenshot_discussion()
olddis = Discussion.of_forum(forum).last()
pedco.open(newdis.url)
print(ctime(), '- publicación en', subject.name)
