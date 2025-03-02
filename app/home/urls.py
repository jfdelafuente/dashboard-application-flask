from flask import request, render_template
from flask_login import login_required

from app.home import home_bp


@home_bp.route("/")
@login_required
def home():
    return render_template(
        "home/index.html"
    )