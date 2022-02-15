import telebot
import yaml


# создали бот
bot = telebot.TeleBot("my token")


@bot.message_handler(commands=['start'])
def start(message):
    with open("channel.yaml") as f:
        channel = yaml.full_load(f.read())['channel']
    response = bot.get_chat_member(chat_id=channel, user_id=message.from_user.id)
    if check_sub_channel(response):
        bot.send_message(message.from_user.id, 'Done!')
    else:
        bot.send_message(message.from_user.id, 'You should to sub to the {} for further work'.format(channel))


def check_sub_channel(chat_member):
    if chat_member.status != 'left':
        return True
    else:
        return False


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.from_user.id, 'I don\'t understand this command')


bot.polling()
