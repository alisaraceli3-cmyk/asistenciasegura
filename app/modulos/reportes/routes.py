# app/modulos/reportes/routes.py  —  Equipo E2: Reportes
# Este archivo es de E2. Solo E5 lo modifica.
from flask import Blueprint, render_template
 
from app.comun.auth import rol_requerido
 
bp = Blueprint("reportes", __name__,
               template_folder="templates", static_folder="static",
               static_url_path="/static/reportes")
 
 
@bp.route("/")
@rol_requerido("Administrador", "Orientadora")
def index():
    return render_template("reportes/index.html")