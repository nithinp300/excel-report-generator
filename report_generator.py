import PySimpleGUI as sg
import mysql.connector
import pandas as pd
import os

#gui window
sg.theme('SandyBeach')
layout = [
    [sg.Text("Please Enter SQL")]
]
window = sg.Window("Report Generator")
event, values = window.read()
query = values['textbook']