from flask import Flask, jsonify, render_template
from flask_cors import CORS
from helpers.retrieve_v3_semver import resolve_version
from helpers.query_package import fetch_data


app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template("index.html"), 200


@app.route('/api/query/<package_name>/json')
def handle_query(package_name):
    return jsonify(fetch_data(package_name)), 200


@app.route('/api/version/<package_name>/<v_type>/json')
def handle_version(package_name, v_type):
    answer, code = resolve_version(package_name.lower(), v_type.lower())
    if code == '404':
        return render_template("glitch.html"), 404
    else:
        return jsonify(answer), 200


@app.errorhandler(404)
def page_not_found(error):
    return render_template("glitch.html"), 404


if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5001, debug=True)
