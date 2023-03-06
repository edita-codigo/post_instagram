from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import requests
from selenium.webdriver.common.by import By
import os
import openai
from PIL import Image, ImageDraw, ImageFont


driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')
time.sleep(2)






def bot():
	try:
		

		time.sleep(10)
		print('ligando openai')
		openai.api_key = "SUA-CHAVE-API-OPENAI"

		response = openai.Completion.create(
		  model="text-davinci-003",
		  prompt="crie uma frase curta reclamando da vida, com humor e muito sarcasmo.",
		  temperature=0.7,
		  max_tokens=256,
		  top_p=1,
		  frequency_penalty=0,
		  presence_penalty=0
		)
		

		#VARIVAEL PROCESSADA PELA OPENAI
		resposta = response['choices'][0]['text']

		#TAMANHO DA IMAGEM
		img = Image.new('RGB', (500, 500), color = 'black')

		#FONTE DA IMAGEM
		fonte = ImageFont.truetype('arial.ttf', size=35)

		#definir as variáveis do texto
		texto = resposta
		

		lista_palavras = texto.split(" ")

		nova_string = ""

		for indice, palavra in enumerate(lista_palavras):
		    if indice % 3 == 0 and indice != 0:
		        nova_string += "\n"
		    nova_string += palavra + " "


		print(nova_string)

		#DEFINIR A POSIÇÃO DA IMAGEM EM RELAÇÃO AO TEXTO
		draw = ImageDraw.Draw(img)
		draw.text((80, 20), nova_string, font=fonte, fill='white')

		#SALVAR IMAGEM
		img.save('postar.png')

		novapub = driver.find_elements(By.CLASS_NAME,'_abcj')
		novapub = novapub[-3]
		novapub.click()
		time.sleep(3)
		
		#CAMINHO DA IMAGEM DO SEU COMPUTADOR
		midia = r'H:/YOUTUBE PROJETOS/INSTA/postar.png'
		############################
		#PREOCESSO DE SELECIONAR A IMAGEM
		selecionardocomputador = driver.find_elements(By.CLASS_NAME,'_aba7')
		selecionardocomputador = selecionardocomputador[-1]
		time.sleep(3)
		attach = driver.find_elements(By.CSS_SELECTOR,"input[type='file']")
		attach = attach[-1]
		print('input')
		attach.send_keys(midia)
		print('publica imagem')
		time.sleep(3)
		avanca = driver.find_element(By.CLASS_NAME,'_abaa')
		avanca.click()
		time.sleep(2)
		avanca = driver.find_element(By.CLASS_NAME,'_abaa')
		avanca.click()
		time.sleep(2)
		avanca = driver.find_element(By.CLASS_NAME,'_abaa')
		avanca.click()
		time.sleep(5)
		print('publicado')
		webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

		
		#####AGUARDA 30 SEGUNDOS E FAZ NOVAMENTE
		time.sleep(30)

	

	except:
		print('AGUARDANDO...')
	
		time.sleep(1) 
		


while True:
	bot()
