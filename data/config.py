from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста
CHANEL_ID = env.str("CHANEL_ID")
PAYPAL_CLIENT_ID = env.str("PAYPAL_CLIENT_ID")
PAYPAL_CLIENT_SECRET = env.str("PAYPAL_CLIENT_SECRET")