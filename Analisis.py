
import streamlit as st
import pandas as pd
import altair as alt

st.title("📊 Análisis de la Carrera de Chief Keef")

st.markdown("""
En esta sección analizamos la popularidad de Chief Keef a través de algunos de sus álbumes
más importantes, mostrando su impacto en números de reproducciones y comparaciones visuales.
""")

# ----------------------------
# 📌 1. TABLA DE DATOS
# ----------------------------
data = {
    "Álbum": ["Finally Rich", "Bang 3", "Thot Breaker", "Dedication"],
    "Año": [2012, 2015, 2017, 2017],
    "Canciones Populares": [
        "Love Sosa, I Don’t Like",
        "Superheroes, Ain’t Missing You",
        "Can You Be My Friend",
        "Keke Palmer"
    ],
    "Reproducciones (millones)": [500, 150, 100, 80]
}

df = pd.DataFrame(data)

st.subheader("📋 Tabla de Datos: Discografía y Popularidad")
st.dataframe(df)

# ----------------------------
# 📊 2. GRÁFICO DE BARRAS
# ----------------------------
st.subheader("📊 Reproducciones por Álbum")
bar_chart = alt.Chart(df).mark_bar(cornerRadiusTopLeft=8, cornerRadiusTopRight=8).encode(
    x=alt.X("Álbum", sort="-y", title="Álbum"),
    y=alt.Y("Reproducciones (millones)", title="Millones de reproducciones"),
    color=alt.Color("Álbum", legend=None)
).properties(
    width=600,
    height=400,
    title="Popularidad de los álbumes de Chief Keef"
)
st.altair_chart(bar_chart, use_container_width=True)

# ----------------------------
# 📈 3. GRÁFICO DE LÍNEAS
# ----------------------------
st.subheader("📈 Evolución por Año")
line_chart = alt.Chart(df).mark_line(point=True).encode(
    x=alt.X("Año:O", title="Año de lanzamiento"),
    y=alt.Y("Reproducciones (millones)", title="Millones de reproducciones"),
    color=alt.value("steelblue")
).properties(
    width=600,
    height=400,
    title="Evolución de popularidad (2012-2017)"
)
st.altair_chart(line_chart, use_container_width=True)

# ----------------------------
# 🟠 4. GRÁFICO CIRCULAR
# ----------------------------
st.subheader("🟠 Distribución por Álbum")
pie_chart = alt.Chart(df).mark_arc(innerRadius=50).encode(
    theta=alt.Theta("Reproducciones (millones)", stack=True),
    color=alt.Color("Álbum", title="Álbum"),
    tooltip=["Álbum", "Reproducciones (millones)"]
).properties(
    width=500,
    height=400,
    title="Porcentaje de reproducciones por álbum"
)
st.altair_chart(pie_chart, use_container_width=True)

# ----------------------------
# 📌 5. INTERPRETACIÓN
# ----------------------------
st.markdown("""
### 🔎 Interpretación de los resultados
- El álbum **Finally Rich (2012)** concentra más del 50% de las reproducciones, siendo su trabajo más influyente.
- Los lanzamientos posteriores (*Bang 3* y *Thot Breaker*) tuvieron impacto, pero no lograron superar su debut.
- Su relevancia inicial marcó un antes y un después en el rap y el drill, consolidándolo como pionero del género.
""")


import streamlit as st

# CSS con overlay
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://m.gettywallpapers.com/wp-content/uploads/2023/01/Chief-Keef-Wallpaper-4k.jpg");
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
