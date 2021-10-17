import telebot
from telebot import types
import os



token = os.getenv('TELEBOTTOKEN')
bot = telebot.TeleBot(token)


bot.send_message(1469532071, '''🔸 BOT REINICIADO 🔸''')

# Start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
    bot.send_message(message.chat.id, '''Olá, '''+ message.chat.first_name + '''! Esta é a calculadora de notas do Podion. Clique no número da opção desejada:

🔸 /um - Calcular quanto precisa tirar no 4° bimestre para passar de ano

🔸 /dois - Calcular quanto precisa tirar na prova bimestral para ficar acima da média

🔸 /tres - Descobrir a nota final do bimestre

🔸 /quatro - Descobrir quanto tirar na prova bimestral para cumprir uma meta''', reply_markup=markup)
    if message.chat.id != 1469532071:
        bot.send_message(1469532071, 'Há uma pessoa usando o bot: {}'.format(message.chat.first_name))
    else:
        print('Adm está a usar o bot.')



# Opção um
user_dict = {}
class User:
    def __init__(self, um):
        self.primeiro = um
        self.segundo = None
        self.terceiro = None
        self.simulado = None
@bot.message_handler(commands=['um'])
def send_um(message):
    try:
        msg = bot.reply_to(message, """\
Ok! Opção 1 selecionada: Vou te ajudar a calcular quanto tirar no 4° bimestre para passar de ano, beleza?

📌 Digite sua nota do 1° Bimestre
(0 - 10)""")
        bot.register_next_step_handler(msg, process_primeiro_step)
    except Exception as e:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
        markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
        bot.send_message(message.chat.id, 'Oops 🥺', reply_markup=markup)
def process_primeiro_step(message):
    try:
        chat_id = message.chat.id
        primeiro = message.text
        User.primeiro = str(primeiro)
        User.primeiro_a = (User.primeiro).replace(',','.')
        User.primeiro_a_float = float(User.primeiro_a)
        msg = bot.reply_to(message, '''📌 Digite sua nota do 2° Bimestre
(0 - 10)''')
        bot.register_next_step_handler(msg, process_segundo_step)
    except Exception as e:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
        markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
        bot.send_message(message.chat.id, 'Oops 🥺', reply_markup=markup)
def process_segundo_step(message):
    try:
        chat_id = message.chat.id
        segundo = message.text
        User.segundo = str(segundo)
        User.segundo_a = (User.segundo).replace(',','.')
        User.segundo_a_float = float(User.segundo_a)
        msg = bot.reply_to(message, '''📌 Digite sua nota do 3° Bimestre
(0 - 10)''')
        bot.register_next_step_handler(msg, process_terceiro_step)
    except Exception as e:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
        markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
        bot.send_message(message.chat.id, 'Oops 🥺', reply_markup=markup)

def process_terceiro_step(message):
    try:
        chat_id = message.chat.id
        terceiro = message.text
        User.terceiro = str(terceiro)
        User.terceiro_a = (User.terceiro).replace(',','.')
        User.terceiro_a_float = float(User.terceiro_a)
        

        msg = bot.reply_to(message, '''📌 Quanto você tirou na nota final dos simulados?
(0 - 1)
        
Se você ainda não tiver recebido, coloque "0".''')
        bot.register_next_step_handler(msg, process_simulado_step)
    except Exception as e:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
        markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
        bot.send_message(message.chat.id, 'Oops 🥺', reply_markup=markup)

def process_simulado_step(message):
    try:
        chat_id = message.chat.id
        simulado = message.text
        User.simulado_resposta = str(simulado)
        User.simulado_resposta_a = (User.simulado_resposta).replace(',','.')
        User.simulado_resposta_a_float = float(User.simulado_resposta_a)
                            
        if User.primeiro_a_float >= 0 and User.primeiro_a_float <= 10 and User.segundo_a_float >= 0 and User.segundo_a_float <= 10 and User.terceiro_a_float >= 0 and User.terceiro_a_float <= 10 and User.simulado_resposta_a_float >= 0  and User.simulado_resposta_a_float <= 1:
            b4s = (60 - 10*User.simulado_resposta_a_float - 2*User.primeiro_a_float - 2*User.segundo_a_float - 3*User.terceiro_a_float)/3   
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
            markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
            bot.send_message(message.chat.id, '''
👉 Sua nota no 1° Bimestre = {:.3f}
👉 Sua nota no 2° Bimestre = {:.3f}
👉 Sua nota no 3° Bimestre = {:.3f}
👉 Sua nota no Simulado = {:.3f}

📗 Sendo essas as suas notas, você precisará de: {:.3f} no 4° Bimestre para passar de ano sem recuperação.'''.format(User.primeiro_a_float,User.segundo_a_float,User.terceiro_a_float,User.simulado_resposta_a_float,b4s), reply_markup=markup)
        else:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
            markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
            bot.send_message(message.chat.id, 'Digite valores válidos.', reply_markup=markup)
    except Exception as e:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
        markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
        bot.send_message(message.chat.id, 'Oops 🥺', reply_markup=markup)

        

# Opção dois
user2_dict = {}
class User2:
    def __init__(self, dois):
        self.parcial2 = dois
        self.bimestral2 = None
@bot.message_handler(commands=['dois'])
def send_dois(message):
    try:
        msg = bot.reply_to(message, """\
Ok! Opção 2 selecionada: Vou te ajudar a calcular quanto tirar na prova bimestral para ficar acima da média, beleza?

📌 Quanto você tirou na Prova Parcial?
(0 - 10)""")
        bot.register_next_step_handler(msg, process_parcial2_step)
    except Exception as e:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
        markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
        bot.send_message(message.chat.id, 'Oops 🥺', reply_markup=markup)

def process_parcial2_step(message):
    try:
        chat_id = message.chat.id
        parcial2 = message.text
        User.parcial2 = str(parcial2)
        User.parcial2_a = (User.parcial2).replace(',','.')
        User.parcial2_a_float = float(User.parcial2_a)
        if User.parcial2_a_float >= 0 and User.parcial2_a_float <= 10:
            bimestral2 = (6 - User.parcial2_a_float * 0.4) / 0.6
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
            markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
            bot.send_message(message.chat.id, '''
👉 Sua nota na prova parcial = {:.3f}

📗 Sendo essa sua nota na prova parcial, você precisará tirar no mínimo {:.3f} na prova bimestral para ficar acima da média.'''.format(User.parcial2_a_float, bimestral2), reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Digite valores válidos.')
    except Exception as e:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
        markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
        bot.send_message(message.chat.id, 'Oops 🥺', reply_markup=markup)

# Opção tres
user3_dict = {}
class User3:
    def __init__(self, tres):
        self.parcial = tres
        self.bimestral = None
@bot.message_handler(commands=['tres'])
def send_um(message):
    try:
        msg = bot.reply_to(message, """\
Ok! Opção 3 selecionada: Vou te ajudar a calcular sua nota final do bimestre, beleza?

📌 Quanto você tirou na Prova Parcial?
(0 - 10)""")
        bot.register_next_step_handler(msg, process_parcial_step)
    except Exception as e:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
        markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
        bot.send_message(message.chat.id, 'Oops 🥺', reply_markup=markup)

def process_parcial_step(message):
    try:
        chat_id = message.chat.id
        parcial = message.text
        User.parcial = str(parcial)
        User.parcial_a = (User.parcial).replace(',','.')
        User.parcial_a_float = float(User.parcial_a)
        msg = bot.reply_to(message, '''📌 Quanto você tirou na prova Bimestral?
(0 - 10)''')
        bot.register_next_step_handler(msg, process_bimestral_step)
    except Exception as e:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
        markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
        bot.send_message(message.chat.id, 'Oops 🥺', reply_markup=markup)

def process_bimestral_step(message):
    try:
        chat_id = message.chat.id
        bimestral = message.text
        User.bimestral = str(bimestral)
        User.bimestral_a = (User.bimestral).replace(',','.')
        User.bimestral_a_float = float(User.bimestral_a)
        if User.parcial_a_float >= 0 and User.parcial_a_float <=10 and User.bimestral_a_float >= 0 and User.bimestral_a_float <=10:
            nota_final = ((User.parcial_a_float*0.4) + (User.bimestral_a_float*0.6))
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
            markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
            bot.send_message(message.chat.id, '''
👉 Sua nota na P. Parcial = {:.3f}
👉 Sua nota na P. Bimestral = {:.3f}

📗 Sendo essas as sua notas, sua nota final do bimestre é de: {:.3f}'''.format(User.parcial_a_float,User.bimestral_a_float,nota_final), reply_markup=markup)
        else:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
            markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
            bot.send_message(message.chat.id, 'Digite valores válidos.', reply_markup=markup)

    except Exception as e:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
        markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
        bot.send_message(message.chat.id, 'Oops 🥺', reply_markup=markup)


# Opção 4
user4_dict = {}
class User4:
    def __init__(self, quatro):
        self.meta = quatro
        self.parcial4 = None
@bot.message_handler(commands=['quatro'])
def send_um(message):
    try:
        msg = bot.reply_to(message, """\
Ok! Opção 4 selecionada: Vou te ajudar a descobrir quanto tirar na prova bimestral para cumprir uma meta, beleza?

📌 Qual sua meta?
(0 - 10)""")
        bot.register_next_step_handler(msg, process_meta_step)
    except Exception as e:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
        markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
        bot.send_message(message.chat.id, 'Oops 🥺', reply_markup=markup)

def process_meta_step(message):
    try:
        chat_id = message.chat.id
        meta = message.text
        User.meta = str(meta)
        User.meta_a = (User.meta).replace(',','.')
        User.meta_a_float = float(User.meta_a)
        msg = bot.reply_to(message, '''📌 Quanto você tirou na prova Parcial?
(0 - 10)''')
        bot.register_next_step_handler(msg, process_parcialb_step)
    except Exception as e:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
        markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
        bot.send_message(message.chat.id, 'Oops 🥺', reply_markup=markup)

def process_parcialb_step(message):
    try:
        chat_id = message.chat.id
        parcialb = message.text
        User.parcialb = str(parcialb)
        User.parcialb_a = (User.parcialb).replace(',','.')
        User.parcialb_a_float = float(User.parcialb_a)
        if User.parcialb_a_float >= 0 and User.parcialb_a_float <=10 and User.meta_a_float >= 0 and User.meta_a_float <=10:
            notadaprovabimestral = (User.meta_a_float - 0.4*(User.parcialb_a_float))/0.6
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
            markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
            bot.send_message(message.chat.id, '''
👉 Sua meta = {:.3f}
👉 Sua nota na P. Parcial = {:.3f}

📗 Sendo esse o seu objetivo, você deverá tirar: {:.3f} na prova bimestral.'''.format(User.meta_a_float,User.parcialb_a_float,notadaprovabimestral), reply_markup=markup)
        else:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
            markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
            bot.send_message(message.chat.id, 'Digite valores válidos.', reply_markup=markup)
    except Exception as e:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
        markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
        bot.send_message(message.chat.id, 'Oops 🥺', reply_markup=markup)

# About
@bot.message_handler(commands=['sobre'])
def sobre(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add('/start','/um', '/dois', '/tres', '/quatro', '/sobre')
    bot.send_message(message.chat.id, '''Sou um bot de Telegram desenvolvido pelo @gdma2004 na linguagem "Python". Seus dados são confidenciais e o programa é código aberto. Caso queira acessar o repositório, o link está aqui embaixo!

🔗 https://github.com/gdma2004/Cacpodbot''', reply_markup=markup)



# Finais
bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()

bot.polling()
