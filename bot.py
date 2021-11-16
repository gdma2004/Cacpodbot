########################################################
#   _____                           _ _           _    #
#  / ____|                         | | |         | |   #
# | |     __ _  ___ _ __   ___   __| | |__   ___ | |_  #
# | |    / _` |/ __| '_ \ / _ \ / _` | '_ \ / _ \| __| #
# | |___| (_| | (__| |_) | (_) | (_| | |_) | (_) | |_  #
#  \_____\__,_|\___| .__/ \___/ \__,_|_.__/ \___/ \__| #
#                  | |                                 #
#                  |_|                                 #
########################################################


# Feito por Gabriel Dantas
# https://github.com/gdma2004

# ChatBot para auxiliar no cálculo das notas do pódion
# Versão "minimal" do código, com foco em estabilidade






# BIBLIOTECAS

import telebot
import regex as re
from telebot import types
from typing import TextIO




# API TOKEN/ENVIAR AO HOST QUE O BOT FOI RECONECTADO

bot = telebot.TeleBot(api_token)
bot.send_message(1469532071, 'Bot reiniciado.')




# START: EXIBE O MENU DE OPÇÕES

@bot.message_handler(commands=['start'])
def start(message):
    
    try: 
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
        markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
        
        bot.send_message(message.chat.id, '''Olá, '''+ message.chat.first_name + '''! Esta é a calculadora de notas do Podion. Clique no número da opção desejada:

🔸 /um - Calcular quanto precisa tirar no 4° bimestre para passar de ano

🔸 /dois - Calcular quanto precisa tirar na prova bimestral para ficar acima da média

🔸 /tres - Descobrir a nota final do bimestre

🔸 /quatro - Descobrir quanto tirar na prova bimestral para cumprir uma meta''', reply_markup=markup)
        if message.chat.id != 1469532071:
            bot.send_message(1469532071, 'Há uma pessoa usando o bot: {} {}'.format(message.chat.first_name, message.chat.last_name))
        else:
            pass
    except Exception as e:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
        markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
        bot.send_message(message.chat.id, 'Oops 🥺', reply_markup=markup)




# MENU 1

@bot.message_handler(commands=['um'])
def um(message):
        
        bot.send_message(message.chat.id, '🔴 Ok! Opção 1 selecionada: Vou te ajudar a calcular quanto tirar no 4° bimestre para passar de ano, beleza?\n\nIndique suas notas do 1°, 2°, 3° bimestres e do simulado separando-as com "/".\n\nExemplo: 7,6/6,8/8,67/0,78')
        @bot.message_handler(func=lambda message: bool(re.search(r'^\d+[,\.]?\d*/\d+[,\.]?\d*/\d+[,\.]?\d*/\d+[,\.]?\d*', message.text)))
        def echo_message(message):
            try: 
                markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
                markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
                informação = str(message.text)
                informação_a = informação.replace(',','.')
                b1,b2,b3,simulado = informação_a.split('/')
                b1_float = float(b1)
                b2_float = float(b2)
                b3_float = float(b3)
                simulado_float = float(simulado)
                b4 = (60 - 10*simulado_float - 2*b1_float - 2*b2_float - 3*b3_float)/3
                if b1_float >= 0 and b1_float <= 10 and b2_float >= 0 and b2_float <= 10 and b3_float >= 0 and b3_float <= 10 and simulado_float >= 0 and simulado_float <= 1:
                    bot.send_message(message.chat.id, '''
👉 Sua nota no 1° Bimestre = {:.3f}
👉 Sua nota no 2° Bimestre = {:.3f}
👉 Sua nota no 3° Bimestre = {:.3f}
👉 Sua nota no Simulado = {:.3f}

📗 Sendo essas as suas notas, você precisará de: {:.3f} no 4° Bimestre para passar de ano sem recuperação.'''.format(b1_float,b2_float,b3_float,simulado_float,b4), reply_markup=markup)
                else:
                    bot.send_message(message.chat.id, 'Digite valores válidos.')

            except Exception as e:
                markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
                markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
                bot.send_message(message.chat.id, 'Oops 🥺', reply_markup=markup)
            
        
    

# MENU 2

@bot.message_handler(commands=['dois'])
def dois(message):
    
    bot.send_message(message.chat.id, '🔴 Ok! Opção 2 selecionada: Vou te ajudar a calcular quanto tirar na prova bimestral para ficar acima da média, beleza?\n\nQuanto você tirou na prova Parcial?')

    @bot.message_handler(func=lambda message: bool(re.search(r'^[0-9,.]+$', message.text)))
    def echo_message(message):
        try:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
            markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
            pp = str(message.text)
            pp_a = pp.replace(',','.')
            pp_a_float = float(pp_a)

            if pp_a_float >= 0 and pp_a_float <= 10:
                pb = (6 - pp_a_float * 0.4) / 0.6
                bot.send_message(message.chat.id, '''
👉 Sua nota na P. Parcial = {:.3f}

📗 Sendo essa a sua nota, você precisará de: {:.3f} na Prova Bimestral para ficar acima da média.'''.format(pp_a_float,pb), reply_markup=markup)
            else:
                bot.send_message(message.chat.id, 'Digite uma nota válida.')

        except Exception as e:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
            markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
            bot.send_message(message.chat.id, 'Oops 🥺', reply_markup=markup)




# MENU 3

@bot.message_handler(commands=['tres'])
def tres(message):
    
    bot.send_message(message.chat.id, '🔴 Ok! Opção 3 selecionada: Vou te ajudar a calcular sua nota final do bimestre, beleza?\n\nIndique suas notas da prova parcial e da prova bimestral separando-as com "/".\n\nExemplo: 7,6/6,8')

    @bot.message_handler(func=lambda message: bool(re.search(r'^\d+[,\.]?\d*/\d+[,\.]?\d*', message.text)))
    def echo_message(message):
        try:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
            markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
            resposta = str(message.text)
            resposta_a = resposta.replace(',','.')
            pp,pb = resposta_a.split('/')
            pp_float = float(pp)
            pb_float = float(pb)
            nota_final = ((pp_float*0.4) + (pb_float*0.6))
            if pp_float >= 0 and pp_float <=10 and pb_float >= 0 and pb_float <=10:
                bot.send_message(message.chat.id, '''
👉 Sua nota na P. Parcial = {:.3f}
👉 Sua nota da P. Bimestral = {:.3f}

📗 Sendo essas as suas notas, você ficará com {:.3f} na média final do bimestre.'''.format(pp_float,pb_float,nota_final), reply_markup=markup)
            else:
                bot.send_message(message.chat.id, 'Digite valores válidos.')

        except Exception as e:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
            markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
            bot.send_message(message.chat.id, 'Oops 🥺', reply_markup=markup)




# MENU 4

@bot.message_handler(commands=['quatro'])
def quatro(message):
    
    bot.send_message(message.chat.id, '🔴 Ok! Opção 4 selecionada: Vou te ajudar a descobrir quanto tirar na prova bimestral para cumprir uma meta, beleza?\n\nIndique sua nota da prova parcial e sua meta separando-as com ";".\n\nExemplo: 7,6;8,7')

    @bot.message_handler(func=lambda message: bool(re.search(r'^\d+[,\.]?\d*;\d+[,\.]?\d*', message.text)))
    def echo_message(message):
        try:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
            markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
            resposta = str(message.text)
            resposta_a = resposta.replace(',','.')
            prova_parcial,meta = resposta_a.split(';')
            prova_parcial_float = float(prova_parcial)
            meta_float = float(meta)
            bimestral = (meta_float - 0.4*(prova_parcial_float))/0.6
            if prova_parcial_float >= 0 and prova_parcial_float <=10 and meta_float >= 0 and meta_float <=10:
                bot.send_message(message.chat.id, '''
👉 Sua nota na P. Parcial = {:.3f}
👉 Sua meta = {:.3f}

📗 Sendo esse seu objetivo, você deverá tirar {:.3f} na prova bimestral para cumprir sua meta.'''.format(prova_parcial_float, meta_float, bimestral), reply_markup=markup)
            else:
                bot.send_message(message.chat.id, 'Digite valores válidos.')

        except Exception as e:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
            markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
            bot.send_message(message.chat.id, 'Oops 🥺', reply_markup=markup)




# MENU SOBRE 

@bot.message_handler(commands=['sobre'])
def sobre(message):
    
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
    bot.send_message(message.chat.id, '''Sou um bot de Telegram desenvolvido pelo @gdma2004 na linguagem "Python". Seus dados são confidenciais e o programa é código aberto. Caso queira acessar  o repositório, o link está aqui embaixo!

🔗 https://github.com/gdma2004''', reply_markup=markup)




# LOOP

bot.polling()
