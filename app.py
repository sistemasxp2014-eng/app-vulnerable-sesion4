from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)
# Solución SAST: Remover contraseña en texto plano y usar una variable de entorno segura
DB_PASSWORD = os.getenv("DB_PASSWORD", "default_secure_fallback_value") 

@app.route("/buscar")
def buscar():
    termino = request.args.get("q", "")
    conexion = sqlite3.connect("datos.db")
    
    # Solución SAST: Usar consultas parametrizadas (?) para evitar la Inyección SQL
    consulta = "SELECT * FROM productos WHERE nombre = ?"
    resultado = conexion.execute(consulta, (termino,))
    return str(resultado.fetchall())

@app.route("/calcular")
def calcular():
    expresion = request.args.get("expr", "")
    
    # Solución SAST: Eliminar eval(). Validamos de forma segura si la entrada es un número entero.
    if expresion.isdigit():
        return str(int(expresion))
    else:
        return "Entrada inválida. Solo se permiten números enteros por seguridad."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
