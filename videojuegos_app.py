import streamlit as st

# Título de la app
st.title("Aplicación de Videojuegos")

# Descripción
st.write("Bienvenido a la aplicación de videojuegos. Selecciona tu videojuego favorito y obtén estadísticas e información adicional.")

... # Crear una lista de videojuegos populares
... videojuegos = ['The Legend of Zelda', 'Minecraft', 'Fortnite', 'Call of Duty', 'Among Us']
... 
... # Selector para elegir un videojuego
... eleccion = st.selectbox('Selecciona tu videojuego favorito:', videojuegos)
... 
... # Mostrar detalles del videojuego seleccionado
... if eleccion == 'The Legend of Zelda':
...     st.write("*The Legend of Zelda* es una serie de videojuegos de aventura desarrollada por Nintendo. Es conocida por su exploración en mundo abierto y su innovador diseño de rompecabezas.")
...     st.image("https://upload.wikimedia.org/wikipedia/commons/a/a9/The_Legend_of_Zelda_logo.svg", width=300)
...     st.write("¡Juega como Link y salva a la Princesa Zelda del malvado Ganon!")
... elif eleccion == 'Minecraft':
...     st.write("*Minecraft* es un videojuego de construcción y aventura donde los jugadores exploran un mundo generado proceduralmente, construyen estructuras y luchan contra criaturas.")
...     st.image("https://upload.wikimedia.org/wikipedia/commons/a/a1/Minecraft_Logo.png", width=300)
...     st.write("¡Construye, explora y sobrevive en un mundo hecho completamente de bloques!")
... elif eleccion == 'Fortnite':
...     st.write("*Fortnite* es un videojuego de batalla real donde 100 jugadores compiten para ser el último en pie en una isla llena de armas y recursos.")
...     st.image("https://upload.wikimedia.org/wikipedia/commons/a/a7/Fortnite_logo.svg", width=300)
...     st.write("¡Lucha, construye y sobrevive en una intensa batalla por la victoria!")
... elif eleccion == 'Call of Duty':
...     st.write("*Call of Duty* es una franquicia de videojuegos de disparos en primera persona conocida por sus intensos combates, gráficos realistas y modos multijugador competitivos.")
...     st.image("https://upload.wikimedia.org/wikipedia/commons/9/9d/Call_of_Duty_Logo.png", width=300)
...     st.write("¡Prepárate para el combate con una de las sagas más populares de la historia de los videojuegos!")
... elif eleccion == 'Among Us':
...     st.write("*Among Us* es un juego multijugador de deducción social donde los jugadores deben descubrir al 'impostor' entre ellos mientras completan tareas en una nave espacial.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/e/e3/Among_Us_Logo.png", width=300)
    st.write("¡Colabora con tu equipo para identificar al impostor o embárcate en un sabotaje en una nave espacial!")
    
# Mostrar recomendaciones basadas en la elección
st.write("*Recomendaciones*")

if eleccion == 'The Legend of Zelda':
    st.write("Si te gusta 'The Legend of Zelda', puedes probar también: 'Super Mario Odyssey', 'Horizon Zero Dawn', o 'The Witcher 3'.")
elif eleccion == 'Minecraft':
    st.write("Si te gusta 'Minecraft', te recomendamos: 'Terraria', 'Don't Starve', o 'Roblox'.")
elif eleccion == 'Fortnite':
    st.write("Si te gusta 'Fortnite', podrías probar: 'Apex Legends', 'PUBG', o 'Battlefield V'.")
elif eleccion == 'Call of Duty':
    st.write("Si te gusta 'Call of Duty', te recomendamos: 'Battlefield', 'Halo', o 'Rainbow Six Siege'.")
elif eleccion == 'Among Us':
    st.write("Si te gusta 'Among Us', puedes probar: 'Mafia', 'Secret Hitler', o 'Project Winter'.")

# Sección de estadísticas del juego
st.write("*Estadísticas del juego elegido*")

# Crear un diccionario con las estadísticas
estadisticas = {
    'The Legend of Zelda': {'Lanzamiento': '1986', 'Plataforma': 'Nintendo', 'Género': 'Aventura'},
    'Minecraft': {'Lanzamiento': '2011', 'Plataforma': 'Multiplataforma', 'Género': 'Construcción/Supervivencia'},
    'Fortnite': {'Lanzamiento': '2017', 'Plataforma': 'Multiplataforma', 'Género': 'Battle Royale'},
    'Call of Duty': {'Lanzamiento': '2003', 'Plataforma': 'Multiplataforma', 'Género': 'FPS'},
    'Among Us': {'Lanzamiento': '2018', 'Plataforma': 'Multiplataforma', 'Género': 'Deducción social'}
}

# Mostrar las estadísticas
st.write(f"Lanzamiento: {estadisticas[eleccion]['Lanzamiento']}")
st.write(f"Plataforma: {estadisticas[eleccion]['Plataforma']}")
st.write(f"Género: {estadisticas[eleccion]['Género']}")

# Barra de progreso de popularidad
st.write("*Popularidad* (escala del 1 al 10):")
if eleccion == 'The Legend of Zelda':
    st.progress(9)
elif eleccion == 'Minecraft':
    st.progress(10)
elif eleccion == 'Fortnite':
    st.progress(9)
elif eleccion == 'Call of Duty':
    st.progress(8)
else:
