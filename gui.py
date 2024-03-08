import functions
import PySimpleGUI as gu

label =gu.Text("Type the to-do")
input_box=gu.InputText(tooltip="Enter the To-do")
add_button = gu.Button("ADD")

window =gu.Window('To-Do App',layout=[[label],[input_box,add_button]])
window.read()
window.close()