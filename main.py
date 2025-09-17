import streamlit as st

st.title("Chief Keef y su prohibición en Chicago")
st.write("Este proyecto explora la vida y carrera de Chief Keef, uno de los raperos más influyentes de la escena drill, y las razones por las cuales se le prohibió presentarse en Chicago. Analizaremos su impacto cultural, las controversias legales y sociales que lo rodean, así como datos y gráficos sobre su música y popularidad.")

st.image("https://preview.redd.it/fashion-highlight-chief-keef-v0-kl23ihxdm3pa1.jpg?width=446&format=pjpg&auto=webp&s=07a3fc8d1a85220deaccd21a816a53f6fb8f3f89")


import streamlit as st

# CSS con overlay
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://wallpapercave.com/wp/wp1868832.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    background-repeat: no-repeat;
    position: relative;
    color: white;
}

/* Overlay oscuro */
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0, 0, 0, 0.5); /* Cambia 0.5 para más/menos oscuridad */
    z-index: -1;
}

/* Header transparente */
[data-testid="stHeader"] {
    background: rgba(0, 0, 0, 0.3);
}

/* Sidebar oscuro */
[data-testid="stSidebar"] {
    background: rgba(0, 0, 0, 0.9);
    color: white;
    text-color: white;
}

/* Botones y entradas */
.stButton>button, .stSelectbox, .stTextInput>div>div>input {
    background-color: rgba(255, 0, 0, 0.7);
    color: white;
    border-radius: 10px;
    border: none;
}

/* Tablas */
[data-testid="stSidebar"] {
    background: rgba(0, 0, 0, 0.9); /* antes estaba en 0.7 */
    color: white;
    text-color: white;
}
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
