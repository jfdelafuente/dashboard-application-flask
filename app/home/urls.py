from datetime import datetime
from flask import render_template, request
from flask_login import login_required
from app.home.controllers import (
    get_metricas,
    get_metricas_proveedor,
    get_distinct_providers,
    get_distinct_apps,
    get_metricas_aplicacion,
    get_all_apps,
    get_metricas_aplicacion_proveedor,
    get_stats,
    get_stats_proveedor,
    get_stats_aplicacion,
    get_dailys,
    get_dailys_proveedor,
    get_dailys_details_aplicacion
)

from app.home import home_bp


@home_bp.route("/")
@login_required
def home():
    return render_template("home/index.html", date=datetime.now())


@home_bp.route("/metricas")
@login_required
def metricas():
    # metricas = Metrica.query.all()
    return render_template("home/metricas/metricas.html", scores=get_metricas())


@home_bp.route("/metricas/proveedores", methods=("GET", "POST"))
@login_required
def proveedores():
    apps = get_distinct_providers()
    if request.method == "POST":
        project = request.form["project_name"]
        return render_template(
            "home/metricas/proveedores.html",
            apps=apps,
            scores=get_metricas_proveedor(project),
            proveedor=project,
            success=True,
        )
    else:
        return render_template("home/metricas/proveedores.html", apps=apps)


@home_bp.route("/metricas/aplicacion", methods=("GET", "POST"))
@login_required
def historico():
    apps = get_distinct_apps()
    if request.method == "POST":
        project = request.form["project_name"]
        # print(f'Proyect name {project}')
        return render_template(
            "home/metricas/historico.html",
            apps=apps,
            scores=get_metricas_aplicacion(project),
            project=project,
            success=True,
        )
    else:
        return render_template("home/metricas/historico.html", apps=apps)

@home_bp.route("/kpis")
@login_required
def kpis():
    return render_template("home/kpis/kpis.html", scores=get_all_apps())



@home_bp.route("/kpis/proveedores", methods=("GET", "POST"))
@login_required
def kpis_proveedores():
    apps = get_distinct_providers()
    if request.method == "POST":
        project = request.form["project_name"]
        return render_template(
            "home/kpis/kpis_proveedores.html",
            apps=apps,
            scores = get_metricas_aplicacion_proveedor(project),
            proveedor=project,
            success=True
        )
    else:
        return render_template("home/kpis/kpis_proveedores.html", apps=apps)


@home_bp.route("/kpis/aplicacion", methods=("GET", "POST"))
@login_required
def kpis_historico():
    apps = get_distinct_apps()
    if request.method == "POST":
        project = request.form["project_name"]
        return render_template(
            "home/kpis/kpis_historico.html",
            apps=apps,
            scores=get_metricas_aplicacion(project),
            date=datetime.now(),
            proveedor=project,
            success=True
        )
    else:
        return render_template("home/kpis/kpis_historico.html", apps=apps)



@home_bp.route("/stats")
@login_required
def stats():
    return render_template("home/stats/stats.html", scores=get_stats())


@home_bp.route("/stats/proveedores", methods=("GET", "POST"))
@login_required
def stats_proveedores():
    apps = get_distinct_providers()
    if request.method == "POST":
        project = request.form["project_name"]
        return render_template(
            "home/stats/stats_proveedores.html",
            apps=apps,
            scores = get_stats_proveedor(project),
            proveedor=project,
            success=True
        )
    else:
        return render_template("home/stats/stats_proveedores.html", apps=apps)


@home_bp.route("/stats/aplicacion", methods=("GET", "POST"))
@login_required
def stats_historico():
    apps = get_distinct_apps()
    if request.method == "POST":
        project = request.form["project_name"]
        return render_template(
            "home/stats/stats_historico.html",
            apps=apps,
            scores=get_stats_aplicacion(project),
            proveedor=project,
            success=True
        )
    else:
        return render_template("home/stats/stats_historico.html", apps=apps)
    

@home_bp.route("/dailys")
def dailys():
    return render_template("home/dailys/dailys.html", 
                            scores=get_dailys())


@home_bp.route("/dailys/proveedores", methods=("GET", "POST"))
def dailys_proveedores():
    apps = get_distinct_providers()
    if request.method == "POST":
        project = request.form["project_name"]
        print(project)
        return render_template(
            "home/dailys/dailys_proveedores_chart.html",
            apps=apps,
            date=datetime.now(),
            scores = get_dailys_proveedor(project),
            project=project,
            success=True
        )
    else:
        return render_template("home/dailys/dailys_proveedores.html", apps=apps)


@home_bp.route("/dailys/aplicacion", methods=("GET", "POST"))
def dailys_historico():
    apps = get_distinct_apps()
    if request.method == "POST":
        project = request.form["project_name"]
        return render_template(
            "home/dailys/dailys_historico_chart.html",
            apps=apps,
            scores=get_dailys_details_aplicacion(project),
            project=project,
            date=datetime.now(),
            success=True
        )
    else:
        return render_template("home/dailys/dailys_historico.html", apps=apps)
