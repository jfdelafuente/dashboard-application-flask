from flask import request, render_template, flash, redirect, url_for
from flask_login import current_user, login_required, login_user, logout_user
from app.accounts.forms import LoginForm, RegisterForm, PasswordForm
from app.accounts import accounts_bp
from app.util import verify_pass
from app.accounts.models import User
from app.extensions import db
from app.extensions import login_manager
# from app.accounts.controllers import list_all_accounts_controller, create_account_controller, retrieve_account_controller, update_account_controller, delete_account_controller

# @accounts_bp.route("/accounts", methods=['GET', 'POST'])
# def list_create_accounts():
#     if request.method == 'GET': return list_all_accounts_controller()
#     if request.method == 'POST': return create_account_controller()
#     else: return 'Method is Not Allowed'

# @accounts_bp.route("/accounts/<account_id>", methods=['GET', 'PUT', 'DELETE'])
# def retrieve_update_destroy_account(account_id):
#     if request.method == 'GET': return retrieve_account_controller(account_id)
#     if request.method == 'PUT': return update_account_controller(account_id)
#     if request.method == 'DELETE': return delete_account_controller(account_id)
#     else: return 'Method is Not Allowed'
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()

 
@accounts_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("You are already logged in.", "info")
        return redirect(url_for("home.home"))
    form = LoginForm(request.form)
    if form.validate_on_submit():
        
        user = User.query.filter_by(username=form.username.data).first()
        if user and verify_pass(form.password.data, user.password):
            login_user(user, remember=form.remember.data)
            print("Logged in successfully.")
            return redirect(url_for("home.home"))
        else:
            flash("Invalid username and/or password.", "danger")
            return render_template(
                "accounts/login.html", form=form, msg="Wrong user or password"
            )
    return render_template("accounts/login.html", form=form)


@accounts_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        flash("You are already registered.", "info")
        return redirect(url_for("home.home"))
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            password=form.password.data,
            email=form.email.data,
            is_admin=False,
        )
        db.session.add(user)
        db.session.commit()

        # Delete user from session
        logout_user()

        return render_template(
            "accounts/register.html",
            msg="Account created successfully.",
            success=True,
            form=form,
        )
    return render_template("accounts/register.html", form=form)


@accounts_bp.route("/password", methods=["GET", "POST"])
def password():
    form = PasswordForm()
    if form.validate_on_submit():
        return render_template(
            "accounts/recuperar.html",
            msg=f"Se ha enviado un correo a {form.email.data} para recuperar password.",
        )
    return render_template("accounts/password.html", form=form)

@accounts_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You were logged out.", "success")
    return redirect(url_for("accounts.login"))