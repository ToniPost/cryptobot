import telebot
from telebot import types
import pymysql
import logging
import random
import requests
from io import BytesIO
from datetime import datetime

# Replace with your bot token
bot_token = "6601354643:AAHw3gRrYLxG-U1UcR7RWTDd9jGELf49EtY"

# Connection parameters (update host, user, password, database as needed)
db = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="bot_telegram"
)

def obtener_anuncio():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM anuncios ORDER BY RAND() LIMIT 1")
    anuncio = cursor.fetchone()
    cursor.close()
    return anuncio

def actualizar_saldo(usuario_id, recompensa):
    cursor = db.cursor()
    cursor.execute(
        "UPDATE usuarios SET saldo = saldo + %s WHERE id = %s",
        (recompensa, usuario_id),
    )
    db.commit()
    cursor.close()

def obtener_saldo(usuario_id):
    cursor = db.cursor()
    cursor.execute("SELECT saldo FROM usuarios WHERE id = %s", (usuario_id,))
    saldo = cursor.fetchone()[0] if cursor.rowcount > 0 else None
    cursor.close()
    return saldo

def registrar_transaccion(usuario_id, descripcion, monto):
    try:
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO transacciones (usuario_id, descripcion, monto, fecha) VALUES (%s, %s, %s, %s)",
            (usuario_id, descripcion, monto, datetime.now())
        )
        db.commit()
        cursor.close()
    except Exception as e:
        logging.error(f"Error al registrar transacción en la base de datos: {e}")

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=["start"])
def start(message):
    try:
        usuario_id = message.chat.id
        cursor = db.cursor()

        cursor.execute("SELECT * FROM usuarios WHERE id = %s", (usuario_id,))
        usuario = cursor.fetchone()

        if usuario is None:
            # Register new user with a default name if username is not available
            nombre_usuario = message.chat.username or "Usuario"
            
            try:
                cursor.execute(
                    "INSERT IGNORE INTO usuarios (id, nombre, saldo) VALUES (%s, %s, %s)",
                    (usuario_id, nombre_usuario, 0),
                )
                db.commit()

                bot.send_message(
                    message.chat.id,
                    f"¡Bienvenido al bot de anuncios, {nombre_usuario}! Tu saldo actual es de 0 Babidoge Coin.",
                )
            except pymysql.IntegrityError as e:
                # Handle the duplicate primary key exception
                logging.error(f"Error en /start (Usuario ya registrado): {e}")
                bot.send_message(
                    message.chat.id,
                    "Ya estás registrado en el bot. Si tienes algún problema, por favor, contacta al soporte."
                )
        else:
            bot.send_message(
                message.chat.id,
                f"¡Hola de nuevo, {message.chat.username or 'Usuario'}! Tu saldo actual es de {usuario[2]} Babidoge Coin."
            )

        # Envía el menú después de saludar al usuario
        menu(message)
        
    except Exception as e:
        logging.error(f"Error en /start: {e}")
    finally:
        cursor.close()

def menu(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    boton_ver_anuncios = types.KeyboardButton("Ver Anuncios")
    boton_enviar = types.KeyboardButton("Enviar")
    boton_ver_saldo = types.KeyboardButton("Ver Saldo")
    markup.row(boton_ver_anuncios, boton_enviar, boton_ver_saldo)
    bot.send_message(message.chat.id, "Selecciona una opción del menú:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Ver Anuncios")
def ver_anuncios(message):
    anuncio = obtener_anuncio()
    if anuncio:
        # Descargar la imagen desde la URL
        image_url = anuncio[3]
        response = requests.get(image_url)
        if response.status_code == 200:
            image_data = BytesIO(response.content)

            # Enviar la imagen junto con la descripción
            bot.send_photo(
                message.chat.id,
                image_data,
                caption=f"**Título:** {anuncio[1]}\n\n**Descripción:** {anuncio[2]}\n\n**URL:** {anuncio[4]}"
            )

            # Simula el retardo de 5 segundos antes de dar la recompensa
            bot.send_message(message.chat.id, "Espera 5 segundos para recibir tu recompensa...")
            bot.send_chat_action(message.chat.id, "typing")

            # Simula la espera de 5 segundos (puedes ajustar según tus necesidades)
            bot.send_message(message.chat.id, "¡Has recibido 5000 Babidoge Coin!")

            # Registra la transacción en la base de datos
            usuario_id = message.chat.id
            descripcion = f"Recompensa por ver anuncio: {anuncio[1]}"
            monto = 5000
            registrar_transaccion(usuario_id, descripcion, monto)
        else:
            bot.send_message(message.chat.id, "Error al descargar la imagen del anuncio.")
    else:
        bot.send_message(message.chat.id, "Lo siento, no hay anuncios disponibles en este momento.")

@bot.message_handler(func=lambda message: message.text == "Enviar")
def enviar(message):
    try:
        usuario_id = message.chat.id
        recompensa = 250 # Puedes ajustar la cantidad de saldo que deseas enviar
        actualizar_saldo(usuario_id, recompensa)

        # Registra la transacción en la base de datos
        descripcion = "Envío de Babidoge Coin a otro usuario"
        registrar_transaccion(usuario_id, descripcion, -recompensa)

        nuevo_saldo = obtener_saldo(usuario_id)

        bot.send_message(
            message.chat.id,
            f"Has enviado {recompensa} Babidoge Coin. Tu saldo actual es de {nuevo_saldo} Babidoge Coin."
        )
    except Exception as e:
        logging.error(f"Error en /enviar: {e}")

@bot.message_handler(func=lambda message: message.text == "Ver Saldo")
def ver_saldo(message):
    try:
        usuario_id = message.chat.id
        saldo = obtener_saldo(usuario_id)

        if saldo is not None:
            bot.send_message(
                message.chat.id,
                f"Tu saldo actual es de {saldo} Babidoge Coin."
            )
        else:
            bot.send_message(
                message.chat.id,
                "No se encontró el saldo para el usuario."
            )
    except Exception as e:
        logging.error(f"Error en /ver_saldo: {e}")

if __name__ == "__main__":
    bot.polling(none_stop=True)
