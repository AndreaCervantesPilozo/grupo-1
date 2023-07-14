import pandas as pd
import requests
from bs4 import BeautifulSoup
fechas = []
pibs = []
vars = []

url = 'https://datosmacro.expansion.com/pib/ecuador'

html_doc = requests.get(url)
soup = BeautifulSoup(html_doc.text, 'html.parser')

for table in soup.findAll('table', attrs={'class': 'table tabledat table-striped table-condensed table-hover'}):
    print(table)
    fecha = table.find('td', attrs={'class':'fecha'})
    print(fecha)
    pib = table.find('td', attrs={'class':'numero eur'})
    print(pib)
    var = table.find('td', attrs={'class':'numero'})
    print(var)

    fechas.append(fecha.text)
    pibs.append(pib.text)
    vars.append(var.text)

    # if fecha is not None:
    #     fechas.append(fecha.text.strip())

# df = pd.DataFrame({'FECHA': fechas,'PIB': pib,'Var.PIB': var})
# df.to_csv('prueba3.csv', index=False, encoding='utf-8')















