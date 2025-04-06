from flask import Flask, render_template, redirect
import sqlite3
from pprint import pprint


conexion = sqlite3.connect('web2.sqlite3')
conexion.row_factory = sqlite3.Row #modo diccionario
cursor = conexion.cursor()


# aplicación
app = Flask(__name__)
