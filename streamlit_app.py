import streamlit as st 
from streamlit_lottie import st_lottie
import requests 

st.set_page_config(page_title="Mi paginaWeb", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None 
    return r.json()

animacion_lottie = load_lottieurl("https://lottie.host/caa472bd-5e9a-419e-bdc0-6905330eaec8/5Jgw8uO76V.json")

def css_local(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
css_local("css/style.css")   
with st.container():
    st.subheader("Hola Mundo!")
    st.title("Hola, me llamo andres tengo 19 y estoy haciendo mis practicas")


with st.container():
    st.write("---")
    col_iz, col_der= st.columns(2)
    with col_iz:
        st.header("Objetivos")
        st.write("##")
        st.write("""Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
    nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    """)
    with col_der:
        st_lottie(animacion_lottie, height=500, key="coding")   

with st.container():
    st.write("---")
    st.header("Forms")
    st.write("##")

    contacto = """
        <form action="https://formsubmit.co/afgoodoy@misena.edu.co" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Tu nombre" required>
            <input type="email" name="email" placeholder="Tu correo" required>
            <textarea name="message" placeholder="Tu mensage" requiered></textarea>
            <button type="submit">Send</button>
        </form>
    """
    col_der, col_iz, centro= st.columns(3)
    with col_iz:
        st.markdown(contacto, unsafe_allow_html=True)
    with col_der:
        st.empty()