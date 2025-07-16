import streamlit as st
import random

# ----------------------------
# Configuración inicial de la página
# ----------------------------
st.set_page_config(page_title="Ruleta 🎰", page_icon="🎲")

# ----------------------------
# Construcción de la mesa (igual que tu código)
# ----------------------------
mesa = {0: "Verde"}

# Primera docena
for i in range(1, 13):
    if i == 11:
        mesa[i] = "Negro"
    elif i == 12:
        mesa[i] = "Rojo"
    elif i % 2 == 0:
        mesa[i] = "Negro"
    else:
        mesa[i] = "Rojo"

# Segunda docena
for i in range(13, 19):
    mesa[i] = "Rojo" if i % 2 == 0 else "Negro"
for i in range(19, 25):
    mesa[i] = "Negro" if i % 2 == 0 else "Rojo"

# Tercera docena
nS = 0
for i in range(25, 37):
    if i in [25, 27]:
        mesa[i] = "Rojo"
    elif i == 30:
        mesa[i] = "Rojo"
        nS = i + 2
    elif i == nS:
        mesa[i] = "Rojo"
        nS = i + 2
    else:
        mesa[i] = "Negro"

# Listas útiles
primera_docena = list(range(1, 13))
segunda_docena = list(range(13, 25))
tercera_docena = list(range(25, 37))
odd = list(range(1, 37, 2))
even = list(range(2, 37, 2))

# ----------------------------
# Interfaz de Streamlit
# ----------------------------
st.title("🎰 BIENVENIDO A LA RULETA")

st.markdown("## Selecciona tu tipo de apuesta:")
tipo_apuesta = st.selectbox("Tipo de apuesta:", ["Número", "Color", "Docena", "Paridad"])

# Obtener la apuesta del usuario
apuesta = None

if tipo_apuesta == "Número":
    apuesta = st.number_input("Selecciona un número del 0 al 36", min_value=0, max_value=36, step=1)

elif tipo_apuesta == "Color":
    apuesta = st.radio("Selecciona un color:", ["Rojo", "Negro"])

elif tipo_apuesta == "Docena":
    apuesta = st.radio("¿A qué docena apuestas?", ["1ra", "2da", "3ra"])

elif tipo_apuesta == "Paridad":
    apuesta = st.radio("Selecciona:", ["Par", "Impar"])

# Botón para girar la ruleta
if st.button("🎡 Girar la ruleta"):
    girar_ruleta = random.randint(0, 36)
    color_salida = mesa.get(girar_ruleta)

    st.subheader(f"🎯 Resultado: {girar_ruleta} - {color_salida}")

    gana = False

    if tipo_apuesta == "Número":
        gana = (girar_ruleta == apuesta)

    elif tipo_apuesta == "Color":
        gana = (color_salida == apuesta)

    elif tipo_apuesta == "Paridad":
        if girar_ruleta == 0:
            gana = False
        elif apuesta == "Par":
            gana = (girar_ruleta in even)
        elif apuesta == "Impar":
            gana = (girar_ruleta in odd)

    elif tipo_apuesta == "Docena":
        if apuesta == "1ra":
            gana = (girar_ruleta in primera_docena)
        elif apuesta == "2da":
            gana = (girar_ruleta in segunda_docena)
        elif apuesta == "3ra":
            gana = (girar_ruleta in tercera_docena)

    # Mostrar resultado final
    if gana:
        st.success("🎉 ¡FELICIDADES, HAS GANADO!")
    else:
        st.error("😢 ¡LO SENTIMOS, HAS PERDIDO!")
