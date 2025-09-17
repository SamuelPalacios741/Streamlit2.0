import streamlit as st

st.title("Los inicios de Chief Keef y el nacimiento del drill")
st.write("Keith Farrelle Cozart, conocido como Chief Keef, nació en Chicago en 1995. Se hizo famoso a los 16 años con la canción I Don’t Like, que impulsó el subgénero drill, caracterizado por letras crudas sobre la violencia y la vida en los barrios marginales. Su influencia fue tan grande que artistas como Kanye West, Drake y Lil Uzi Vert reconocieron la importancia de su estilo.")

st.markdown("""
### Curiosidades sobre Chief keef

- **Nacimiento:** Keith Farrelle Cozart nació en Chicago en 1995.
- **Apodo:** Es conocido mundialmente como *Chief Keef*.
- **Inicios musicales:** Empezó a rapear y grabar música desde su adolescencia, usando grabadoras caseras.
- **Explosión de fama:** Se hizo viral en 2012 con la canción *I Don’t Like*, que más tarde fue remixada por Kanye West.
- **Creador del Drill:** Es considerado pionero del subgénero *drill*, caracterizado por letras sobre la vida en los barrios de Chicago.
- **Influencia cultural:** Inspiró a una nueva generación de raperos, tanto en EE.UU. como en Europa.
- **Estilo polémico:** Su música ha sido criticada por la violencia explícita, pero al mismo tiempo es vista como un reflejo de la realidad social.
""")

##st.info("Usa el menú lateral para moverte entre Inicio, Análisis y Configuración.")

tab1, tab2, tab3, tab4 = st.tabs(["Incios", "Drill", "Influencias", "Cultura"])

with tab1:
   st.header("Inicios")
   st.image("https://preview.redd.it/u7c5ufwfkvh11.jpg?auto=webp&s=0412ce5b80270450a854ad54ee31edcc94313ada")
   



with tab2:
   st.header("ChicagoDrill")
   st.write("El Chicago drill es un subgénero del rap que nació en la ciudad de Chicago a principios de la década de 2010. Su nombre viene de la palabra “drill”, que en el argot callejero significa “atacar” o “enfrentarse”.")
   st.image("https://media2.ntslive.co.uk/resize/1600x1600/bc4420e3-b9e1-4700-bf50-ec872aed8676_1677110400.png")
   st.markdown("""
### Curiosidades del Chicago Drill

- **Origen:** Nació a inicios de la década de 2010 en los barrios del sur de Chicago.
- **Significado:** La palabra *"drill"* en el argot callejero significa "atacar" o "enfrentarse".
- **Letras:** Se caracterizan por ser crudas y explícitas, reflejando la violencia, las pandillas y la vida en la calle.
- **Sonido:** Bases oscuras, con ritmos pesados y repetitivos, donde predominan los bajos.
- **Exponente principal:** Chief Keef es considerado el pionero, especialmente con su éxito *I Don’t Like* (2012).
- **Expansión:** El estilo se extendió a otros lugares, influyendo en el *UK Drill* (Londres) y el *NY Drill* (Nueva York).
- **Impacto cultural:** Más que un género musical, es un reflejo de la situación social en Chicago y un movimiento que marcó la música urbana.
""")
   
with tab3:
   st.header("Influencia musical")
   st.write("La música de Chief Keef no solo impulsó su carrera, sino que también cambió el rumbo del rap moderno. Su estilo crudo y directo abrió la puerta al drill como un movimiento global, inspirando a artistas de talla mundial y marcando una nueva forma de producir y difundir música desde las calles hacia la industria.")
   st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnN5umWBMPIfKCr0s5rE1wH0TS7keit5fq3w&s")
   st.markdown("""
### Curiosidades de la influencia musical

- **Inspiró** a artistas como Kanye West, Drake, Lil Uzi Vert y 21 Savage.

- **Fue** clave en el surgimiento de otros raperos de Chicago como Lil Durk, G Herbo y Polo G.

- **Influyó** en el crecimiento del trap y el uso de YouTube/SoundCloud como plataformas de lanzamiento.

- **El drill**, gracias a él, se expandió a ciudades como Londres (UK Drill) y Nueva York (NY Drill).
""")
   
with tab4:
   st.header("Cultura Drill")
   st.write("Más allá de un género musical, el drill se convirtió en una expresión cultural de la juventud en Chicago. Sus letras y estética muestran la vida en los barrios marginales, convirtiéndose en un reflejo de las condiciones sociales y en una forma de protesta, aunque también ha sido fuertemente criticado por la violencia que representa.")
   st.image("https://substackcdn.com/image/fetch/$s_!bNNN!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F75fc6da2-7083-4296-a6ef-68886e6f1a58_4312x2588.jpeg")
   st.markdown("""
### Curiosidades de la cultura drill

- **Refleja** temas como violencia, pandillas, desigualdad y supervivencia.

- **Estética reconocida:**

- **Videos** en barrios con armas, autos y grupos de amigos.

- **Moda urbana:** hoodies, gorras, cadenas y zapatillas.

- **Fue** acusado de fomentar la violencia, pero también es visto como una voz para los jóvenes.

- **Hoy** es un movimiento global, con presencia en EE.UU., Reino Unido y otros países.
""")

import streamlit as st

# CSS con overlay
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://wallpaperaccess.com/full/113933.png");
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


