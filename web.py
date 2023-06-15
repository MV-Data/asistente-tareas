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

for index, tarea in enumerate(tareas):
    checkbox = st.checkbox(tarea, key=f"checkbox_{index}")
    if checkbox:
        tareas_eliminar.append(tarea)
        #tareas.pop(index)
        #functions.write_tareas(tareas)
        #del st.session_state[tarea]
        #st.experimental_rerun()
        #       
for tarea in tareas_eliminar:
    tareas.remove(tarea)
    del st.session_state[tarea]
    
functions.write_tareas(tareas)

st.text_input(label="", placeholder="Ingrese Tarea", 
              on_change= añadir_tarea, key="nueva_tarea")
