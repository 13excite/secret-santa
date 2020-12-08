from flask import Blueprint, render_template, jsonify


base_blueprint = Blueprint('base', __name__, template_folder='templates')


@base_blueprint.route('/')
def get_main_page():
    return render_template('general.html')

