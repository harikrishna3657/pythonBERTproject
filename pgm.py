import requests
from bs4 import BeautifulSoup
f=open('url.txt','r')
url = f.read()
f.close()

res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)

output = ''
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
]

for t in text:
    if t.parent.name not in blacklist:
        output += '{} '.format(t)

#print(output)
output = [output]

import ktrain
p = ktrain.load_predictor('model_BERT')

topic = p.predict(output)[0]
print(url)
print("\n")
#print(output)
print("\n")
print(topic)
