import graphics as gf
janela = gf.GraphWin("Minha Janela",450,300)
def cabeça(janela):
	cabeça = gf.Circle(gf.Point(80,80),20)
	cabeça.draw(janela)
def tronco(janela):
	tronco = gf.Line(gf.Point(80,100),gf.Point(80,150))
	tronco.draw(janela)
def braço_esquerdo(janela):
	braço_esquerdo = gf.Line(gf.Point(80,110),gf.Point(40,120))
	braço_esquerdo.draw(janela)
def braço_direito(janela):
	braço_direito = gf.Line(gf.Point(80,110),gf.Point(120,120))
	braço_direito.draw(janela)
def perna_esquerda(janela):
	perna_esquerda = gf.Line(gf.Point(80,150),gf.Point(60,190))
	perna_esquerda.draw(janela)
def perna_direita(janela):
	perna_direita = gf.Line(gf.Point(80,150),gf.Point(100,190))
	perna_direita.draw(janela)
def forca(janela):
	linha1 = gf.Line(gf.Point(80,60),gf.Point(80,30))
	linha1.draw(janela)
	linha2 = gf.Line(gf.Point(80,30),gf.Point(30,30))
	linha2.draw(janela)
	linha3 = gf.Line(gf.Point(30,30),gf.Point(30,200))
	linha3.draw(janela)

forca(janela)

palavra_certa = 'contrabaixo'
erros = 0
acertos = 0
errada_x = 190
certa_x = 150
tentadas = ''
texto = gf.Text(gf.Point(310,280),'Você já tentou essa letra')
texto.setSize(15)
texto.setTextColor("red")
while erros < 6 and acertos < len(palavra_certa):
	tentativa = janela.getKey()
	if tentativa in tentadas:
		texto.draw(janela)
	else:
		texto.undraw()
		if tentativa in palavra_certa:
			cont = 0
			certa_x = 150
			while cont < len(palavra_certa):
				if tentativa == palavra_certa[cont]:		
					letra = gf.Text(gf.Point(certa_x,230),tentativa)
					letra.setSize(20)
					letra.draw(janela)
					acertos += 1
				cont += 1
				certa_x = 150 + (cont * 18) 
		else:
			erros += 1
			letra = gf.Text(gf.Point(errada_x,30),tentativa)
			letra.setSize(20)
			letra.draw(janela)
			errada_x += 18
			if erros == 1:
				cabeça(janela)
			if erros == 2:
				tronco(janela)
			if erros == 3:
				braço_esquerdo(janela)
			if erros == 4:
				braço_direito(janela)
			if erros == 5:
				perna_esquerda(janela)
			if erros == 6:
				perna_direita(janela)
	tentadas += tentativa
if erros == 6:
	palavra = gf.Text(gf.Point(225,150),'Fim de Jogo, você perdeu')
	palavra.setSize(25)
	palavra.draw(janela)
else:
	palavra = gf.Text(gf.Point(225,150),'Fim de Jogo, parabéns')
	palavra.setSize(25)
	palavra.draw(janela)

janela.getMouse()
