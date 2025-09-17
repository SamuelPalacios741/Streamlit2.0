import streamlit as st

st.title("¿Por qué Chief Keef tiene prohibido presentarse en Chicago?")
st.write("Chief Keef estuvo involucrado en múltiples polémicas relacionadas con violencia, posesión de armas y tensiones entre pandillas en Chicago. Sus letras y conciertos fueron considerados por las autoridades como un factor que podía incitar a la violencia. Por ello, en varias ocasiones se cancelaron sus presentaciones en la ciudad. Incluso, en 2015 se intentó hacer un concierto holográfico, pero fue apagado por la policía en cuestión de minutos. Hasta la fecha, sigue teniendo dificultades para organizar shows en Chicago, aunque su música siga sonando en todo el mundo.")

st.image("https://preview.redd.it/16-17-year-old-chief-keef-when-he-first-moved-to-the-v0-4nbz45c5z6he1.jpeg?width=2048&auto=webp&s=b907aae49b1a2c94bd117f534f1b95ae008ca422")

tab1, tab2, tab3 = st.tabs(["Problemas", "Conciertos", "Opiniones"])

with tab1:
   st.header("Problemas legales")
   st.write("La carrera de Chief Keef ha estado marcada por diversos conflictos con la ley. Desde muy joven enfrentó cargos relacionados con armas y drogas, lo que contribuyó a su imagen polémica y a la percepción de que su música estaba ligada a la violencia en Chicago.")
   st.image("https://thejasminebrand.com/wp-content/uploads/2024/10/IMG_8483.jpeg")
   st.markdown("""
### ¿Cuales fueron esos problemas legales?
               
-**Arrestado** varias veces por posesión ilegal de armas.

-**Enfrentó** cargos relacionados con drogas y disturbios.

-**Vivió** períodos de arresto domiciliario durante su adolescencia.

-**Sus** problemas legales alimentaron la narrativa de que su música estaba directamente conectada con la violencia callejera.
 """)
   



with tab2:
   st.header("Conciertos cancelados")
   st.write("Las presentaciones de Chief Keef en Chicago han sido constantemente objeto de censura por parte de las autoridades, quienes consideran que sus shows pueden incitar a la violencia entre pandillas rivales. Incluso intentos innovadores como los conciertos en holograma fueron interrumpidos por la policía.")
   st.image("https://i.ytimg.com/vi/BpO5YlF3984/maxresdefault.jpg")
   st.markdown("""
### Conciertos Cancelados

-**Varias** presentaciones prohibidas en Chicago por seguridad pública.

-**En 2015**, un concierto holográfico fue apagado por la policía pocos minutos después de iniciar.

-**Los organizadores** de eventos en Chicago enfrentan presión de las autoridades para no contratarlo.

-**A pesar** de las restricciones, Chief Keef mantiene giras exitosas en otras ciudades y países.
""")
   
with tab3:
   st.header("Opiniones de la comunidad")
   st.write("La percepción de Chief Keef está dividida: mientras algunos lo ven como un peligro por glorificar la violencia, otros lo consideran una voz auténtica que refleja la dura realidad de Chicago. Su música abrió un debate sobre los límites entre el arte, la censura y la libertad de expresión.")
   st.image("https://images.sk-static.com/images/media/img/col3/20230525-134525-396254.jpg")
   st.markdown("""
### Estas son las opiniones

-**Críticos:** Acusan al drill de fomentar la violencia y reforzar conflictos de pandillas.

-**Seguidores:** Lo defienden como un narrador de la realidad, no como promotor de ella.

-**Comunidad musical:** Reconoce su aporte cultural y su influencia global.

-**El caso** de Chief Keef abrió la discusión sobre la relación entre arte, política y sociedad en Chicago.
""")

import streamlit as st

# CSS con overlay
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://wallpapers.com/images/hd/chief-keef-call-me-still-ldayb01w9kd8zttl.jpg");
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
    background: rgba(0, 0, 0, 0.7);
    color: white;
}

/* Botones y entradas */
.stButton>button, .stSelectbox, .stTextInput>div>div>input {
    background-color: rgba(255, 0, 0, 0.7);
    color: white;
    border-radius: 10px;
    border: none;
}

/* Tablas */
[data-testid="stDataFrame"] {
    background: rgba(0, 0, 0, 0.6);
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)



   
