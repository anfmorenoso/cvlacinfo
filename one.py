from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
# import sys
# import codecs
# sys.stdout = codecs.getwriter("iso-8859-1")(sys.stdout, 'xmlcharrefreplace')

filename = "con.txt"
f = open(filename, "w", encoding="utf8")
g = open("wea.txt", "w", encoding="utf8")

myurl = 'http://scienti.colciencias.gov.co:8081/cvlac/visualizador/generarCurriculoCv.do?cod_rh=0000639508'
#myurl = 'http://scienti.colciencias.gov.co:8081/cvlac/visualizador/generarCurriculoCv.do?cod_rh=0000499625' #restrepo

#opening connection
uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()

#html parser
# page_soup = soup(page_html, "html.parser")
page_soup = soup(open("cvlacisp.html", encoding='latin-1'), "html.parser")
bqs = page_soup.findAll("blockquote")
tabs = page_soup.findAll("table")

cnt = 0
a = []

#g.write( str(tabs[37]) )

for n in range(1,len(tabs)):
    #f.write( str(n) + " " + str(tabs[n]) + "\n" )
    try:
        tex = tabs[n].tr.td.h3.text
        a.append(n);
        f.write( tex + "\n" )
    except AttributeError:
        f.write( "lmfao " + str(n) + "\n")

#imprimir arreglo de cosas que tienen título h3
f.write( "[" )
for i in a:
    f.write( str(i) + " " )
f.write( "]" )
articulos( 37, tabs )

#g.write( str(tabs[10]) )

def articulos( id, sopa ):
    blqs = sopa[id].findAll("blockquote")

    cowsep = [x.strip() for x in blqs[0].text.strip().replace('\n','').split(',')]
    for item in cowsep:
        if '"' in item:
            print(item)

    g.write( str( blqs[4].text ) )
