from flask import Blueprint, render_template, jsonify, request, flash, redirect
import re

base_blueprint = Blueprint('base', __name__, template_folder='templates')

VALID_EMAIL = '^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$'
VALID_LETTERS = '^[0-9a-zA-ZА-ЯЁа-яё,\.!\:\?\-]+$'


def is_valid_mail(email):
    if re.match(VALID_EMAIL, email):
        return True
    return False


def is_valid_name(name):
    if len(name) > 30 or not re.match(VALID_LETTERS, name):
        return False
    return True


def is_valid_interest(interst):
    if len(interst) > 254 or not re.match(VALID_LETTERS, interst):
        return False
    return True


@base_blueprint.route('/')
def get_main_page():
    return render_template('general.html')


@base_blueprint.route('/load', methods=['GET', 'POST'])
def add_data():
    interest = request.form['interest']
    name = request.form['name']
    email = request.form['email']
    if not is_valid_name(name):
        flash("Имя должно быть текстовое и короче 30 символов")
        return redirect('/')
    if not is_valid_interest(interest):
        flash("Интересы могут содержать только письменные символы и быть короче 255 символов")
        return redirect('/')
    if not is_valid_mail(email):
        flash("Некорректный email. Используйте формат exmaple@example.zyx")
        return redirect('/')
    return jsonify("OK")

