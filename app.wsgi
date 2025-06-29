import sys
import os

# Agrega la ruta del proyecto
sys.path.insert(0, os.path.dirname(__file__))

# Establece la variable de entorno para Flask
os.environ['FLASK_APP'] = 'app.py'

# Importa tu aplicación Flask
from app import app as application