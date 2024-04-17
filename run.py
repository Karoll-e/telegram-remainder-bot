from app import *
import config

if config.ENV == "DEV":
    bot.infinity_polling(True)  #bot.polling()


elif config.ENV == "PROD":
    import flask
    import threading

    app = flask.Flask(__name__)

    @app.route('/'+config.telegram_key, methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(flask.request.stream.read().decode("utf-8"))])
        return "!", 200

    @app.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(url=config.webhook+config.telegram_key)
        return 'Chat with the Bot  <a href ="https://t.me/DutiesRemainderBot">here</a> \
          or   Check the project code <a href ="https://github.com/Karoll-e/telegram-remainder-bot">here</a>', 200

    if __name__ == "__main__":
        print("---", datetime.datetime.now().strftime("%H:%M"), "---")
        #if datetime.datetime.now().strftime("%H:%M") in ["05:00","05:01","06:00","06:01","07:00","07:01"]:
        threading.Thread(target=scheduler).start()
        app.run(host=config.host, port=config.port)

