import streamlit as st
import functions

tareas = functions.get_tareas()
checkbox_states = {tarea: False for tarea in tareas}

def añadir_tarea():
    tarea = st.session_state["nueva_tarea"] + "\n"
    tareas.append(tarea)
    checkbox_states[tarea] = False
    functions.write_tareas(tareas)

st.title("Mi Asistente Personal")
st.subheader("Desarrollado por Alicia Linares y sus arepas.\n Soluciones de datos")
st.write('El objetivo de esta app es incrementar su productividad')

tareas_eliminar = []

for tarea in tareas:
    checkbox_state = st.checkbox(tarea, key=tarea, value=checkbox_states[tarea])
    checkbox_states[tarea] = checkbox_state
    if checkbox_state:
        tareas_eliminar.append(tarea)

for index,tarea in enumerate(tareas_eliminar):
    tareas.pop(index)
    del checkbox_states[tarea]

functions.write_tareas(tareas)

st.text_input(label="", placeholder="Ingrese Tarea", on_change=añadir_tarea, key="nueva_tarea")
