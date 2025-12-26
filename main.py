import telebot
from config import token
import ya

bot = telebot.TeleBot(token)

careers = {
    "творческий": ["Художник", "Дизайнер", "Архитектор", "Скульптор", "Фотограф", "Режиссёр", "Сценарист", "Актёр", "Писатель", "Композитор", "Музыкант", "Декоратор"],
    "технический": ["Программист", "Системный администратор", "Инженер", "Техник", "Аналитик", "Разработчик", "Тестировщик", "Администратор баз данных", "Инженер-программист", "Веб-разработчик", "Сетевой инженер", "Специалист по кибербезопасности", "Администратор систем"],
    "социальный": ["Социальный работник", "Психолог", "Педагог", "Учитель", "Воспитатель", "Социолог", "Педагог-психолог", "Медицинская сестра", "Фельдшер", "Логопед", "Реабилитолог"]
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я помогу тебе выбрать карьеру. Напиши 'творческий', 'технический' или задай вопрос о профессии. А если вам мало тех профессий то напиши.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text.lower() 

    if user_input in careers: 
        recommendations = ", ".join(careers[user_input])
        bot.send_message(message.chat.id, f"Вот профессии в направлении '{user_input}': {recommendations}.")
    else:
        ai_response = ya.gpt(user_input) 
        bot.send_message(message.chat.id, ai_response) 
        

bot.infinity_polling()
