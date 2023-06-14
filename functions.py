#FILEPATH='C://Workspace_proyectos//Curso_Python_20_apps//app1//files//tareas.txt'
FILEPATH='tareas.txt'


def get_tareas(filepath=FILEPATH):
    '''Read a text file and returns the list
    of to-do items
     '''
    with open(filepath,'r') as file_local:
        tareas_local=file_local.readlines()
    return tareas_local

      
def write_tareas(tareas_arg,filepath=FILEPATH):
    '''write a to-do items list in the text file'''
    with open(filepath,'w') as file_local:
        file_local.writelines(tareas_arg)