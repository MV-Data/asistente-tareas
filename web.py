import streamlit as st
import functions


tareas = functions.get_tareas()

def añadir_tarea():
   tarea =  st.session_state["nueva_tarea"] + "\n"
   tareas.append(tarea)
   functions.write_tareas(tareas)


st.title("Mi Asistente Personal")
st.subheader("Desarrollado por Alicia Linares y sus arepas.\n Soluciones de datos")
st.write('El objetivo de esta app es la de incrementar su productividad')

tareas_eliminar = []

for index in range(len(tareas)-1, -1, -1):
    tarea = tareas[index]
    checkbox = st.checkbox(tarea, key=f"checkbox_{index}")
    if checkbox:
        tareas_eliminar.append(index)

for index in tareas_eliminar:
    tarea = tareas[index]
    tareas.pop(index)
    del st.session_state[f"checkbox_{index}"]

functions.write_tareas(tareas)

st.text_input(label="", placeholder="Ingrese Tarea", 
              on_change= añadir_tarea, key="nueva_tarea")

