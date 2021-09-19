from logging import error
import os
import sys
from typing import Type
import telebot
from telebot.types import Message, MessageID
import re

bot = telebot.TeleBot('Token')




#comando start (exibe o menu)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '''Olá! Esta é a calculadora de notas do Podion. Clique no número da opção desejada:

🔸 /um - Calcular quanto precisa tirar no 4° bimestre para passar de ano.

🔸 /dois - Calcular quanto precisa tirar na prova bimestral para ficar acima da média.

🔸 /tres - Descobrir a nota final do bimestre.

🔸 /sobre - Exibir uma pequena descrição do programa.''')



#seleção do menu 1
@bot.message_handler(commands=['um'])
def um(message):
    bot.send_message(message.chat.id, '🔴 Ok! Opção 1 selecionada: Vou te ajudar a calcular quanto tirar no 4° bimestre para passar de ano, beleza?')
    bot.send_message(message.chat.id, 'Quanto você tirou no 1°, 2° e 3° bimestres respectivamente? Separe as notas com "/" (0 - 10)')
    @bot.message_handler(func=lambda message: bool(re.search(r"\d+[,\.]?\d*/\d+[,\.]?\d*/\d+[,\.]?\d*", message.text)) == True)
    def echo_message(message):
        try:
            informação = str(message.text)
            informação_a = informação.replace(',','.')
            b1,b2,b3 = informação_a.split('/')
            b1_float = float(b1)
            b2_float = float(b2)
            b3_float = float(b3)
            b4 = ((b1_float * 2 + b2_float * 2 + b3_float * 3 - 60) / 3) * -1
            if b1_float >= 0 and b1_float <= 10 and b2_float >= 0 and b2_float <= 10 and b3_float >= 0 and b3_float <= 10:
                bot.send_message(message.chat.id, '''
👉 Sua nota no 1° Bimestre = {:.3f}
👉 Sua nota no 2° Bimestre = {:.3f}
👉 Sua nota no 3° Bimestre = {:.3f}

Sendo essas as suas notas, você precisará de: {:.3f} no 4° Bimestre para passar de ano.'''.format(b1_float,b2_float,b3_float,b4))
            else:
                bot.send_message(message.chat.id, 'Digite valores válidos.')
        except (RuntimeError, TypeError, NameError, IndexError, BufferError, TabError, ValueError):
            bot.send_message(message.chat.id, 'Oops')   

#seleção do menu 2 
@bot.message_handler(commands=['dois'])
def dois(message):
    bot.send_message(message.chat.id, '🔴 Ok! Opção 2 selecionada: Vou te ajudar a calcular quanto tirar na prova bimestral para ficar acima da média, beleza?')
    bot.send_message(message.chat.id, 'Quanto você tirou na prova parcial? Escreva a nota entre ";" (0 - 10)')
    @bot.message_handler(func=lambda message: bool(re.search(r";\d+[,\.]?\d*;", message.text)) == True)
    def echo_message(message):
        try:
            pp = str(message.text)
            pp_a = pp.replace(',','.')
            pp_a_a = pp_a.replace(';','')
            pp_a_float = float(pp_a_a)
            if pp_a_float >= 0 and pp_a_float <= 10:
                pb = (6 - pp_a_float * 0.4) / 0.6
                bot.send_message(message.chat.id, '''
👉 Sua nota na prova parcial = {:.3f}

Sendo essa sua nota na prova parcial, você precisará tirar no mínimo {:.3f} na prova bimestral para ficar acima da média.'''.format(pp_a_float,pb))
            else:
                bot.send_message(message.chat.id, 'Digite uma nota válida.')
        except (RuntimeError, TypeError, NameError, IndexError, BufferError, TabError, ValueError):
            bot.send_message(message.chat.id, 'Oops')


#seleção do menu 3
@bot.message_handler(commands=['tres'])
def tres(message):
    bot.send_message(message.chat.id, '🔴 Ok! Opção 3 selecionada: Vou te ajudar a calcular sua nota final do bimestre, beleza?')
    bot.send_message(message.chat.id, 'Quanto você tirou na Prova Parcial e na Prova Bimestral respectivamente? Separe as notas com "/" (0 - 10)')
    @bot.message_handler(func=lambda message: bool(re.search(r"\d+[,\.]?\d*/\d+[,\.]?\d*", message.text)) == True)
    def echo_message(message):
        try:
            resposta = str(message.text)
            resposta_a = resposta.replace(',','.')
            pp,pb = resposta_a.split('/')
            pp_float = float(pp)
            pb_float = float(pb)
            nota_final = ((pp_float*0.4) + (pb_float*0.6))
            if pp_float >= 0 and pp_float <=10 and pb_float >= 0 and pb_float <=10:
                bot.send_message(message.chat.id, '''
👉 Sua nota na Prova Parcial = {:.3f}
👉 Sua nota da Prova Bimestral = {:.3f}

Sendo essas as sua notas, sua nota final do bimestre é de: {:.3f}'''.format(pp_float,pb_float,nota_final))
            else:
                bot.send_message(message.chat.id, 'Digite valores válidos.')
        except (RuntimeError, TypeError, NameError, IndexError, BufferError, TabError, ValueError):
            bot.send_message(message.chat.id, 'Oops')

#sobre
@bot.message_handler(commands=['sobre'])
def start(message):
    bot.send_message(message.chat.id, '''Olá! Sou um bot de Telegram desenvolvido pelo @gdma2004 na linguagem "Python". Seus dados são confidenciais e o programa é código aberto. Caso queira acessar o repositório, o link está aqui embaixo!

🔗 link''')




#loop
bot.polling()




