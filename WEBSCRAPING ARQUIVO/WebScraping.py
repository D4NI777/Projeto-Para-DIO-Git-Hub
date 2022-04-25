import requests
#Requerimento da pagina

from bs4 import BeautifulSoup
#Busca dados da pagina requerida

requerimento = requests.get('https://g1.globo.com/') #codigo para fazer o requerimento

conteudo = requerimento.content #variavel guarda o conteudo da pagina requerida

site = BeautifulSoup(conteudo, 'html.parser')
#converte a pag requerida de html para um objeto BeautifulSoup
noticia = site.find('div', attrs={'class':'feed-post-body'})
#parametros: tipo de string que está o item que vc procura, attrs={'class':'nome da classe'}(dentro de um dicionario)
titulo = noticia.find('a', attrs={'class':'feed-post-link gui-color-primary gui-color-hover'})
#buscando o titulo dentro da noticia
print(titulo.text)
#.text serve para mostra somente o texto dentro da tag e não a tag com todos os parametros