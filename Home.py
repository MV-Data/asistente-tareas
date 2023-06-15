import streamlit as st
import functions


#st.set_page_config(layout="wide") si quiero configurar para que se ajuste al tamaño, x ej en móviles

tareas = functions.get_tareas()
checkbox_states = {tarea: False for tarea in tareas}

def añadir_tarea():
    tarea = st.session_state["nueva_tarea"] + "\n"
    tareas.append(tarea)
    checkbox_states[tarea] = False
    functions.write_tareas(tareas)

def eliminar_tarea(tarea):
    tareas.remove(tarea)
    del checkbox_states[tarea]

def confirmar_eliminar(tarea):
    st.session_state["tarea_a_eliminar"] = tarea

def cancelar_eliminar():
    st.session_state["tarea_a_eliminar"] = None

st.title("Mi Asistente Personal")
st.subheader("Desarrollado por Alicia Linares y sus arepas.\n Soluciones de datos")
#st.write('El objetivo de esta app es incrementar su productividad.')
st.markdown("<h7>Haga <b>doble click</b> en la tarea que desea eliminar.\n</h7>", 
            unsafe_allow_html=True)

tarea_a_eliminar = st.session_state.get("tarea_a_eliminar")

for tarea in tareas:
    checkbox_state = st.checkbox(tarea, key=tarea, value=checkbox_states[tarea])
    checkbox_states[tarea] = checkbox_state
    if checkbox_state and tarea != tarea_a_eliminar:
        confirmar_eliminar(tarea)

if tarea_a_eliminar:
    st.write(f"¿Estás seguro de eliminar la tarea '{tarea_a_eliminar}'?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Sí"):
            eliminar_tarea(tarea_a_eliminar)
            cancelar_eliminar()
    with col2:
        if st.button("No"):
            cancelar_eliminar()

functions.write_tareas(tareas)

st.text_input(label="", placeholder="Ingrese Tarea", 
              on_change=añadir_tarea, key="nueva_tarea")
