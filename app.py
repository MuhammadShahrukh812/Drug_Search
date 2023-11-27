from flask import Flask, request, jsonify, send_from_directory
from config import db, Drug, mysql_user, mysql_root_password
from utils import load_json_data
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password123@mysql/flaskappdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def init_db():
    with app.app_context():
        try:
            # Check if there is any data in the Drug table
            if not db.session.query(Drug.query.exists()).scalar():
                db.create_all()
                print("Database tables created.")
                load_json_data()
            else:
                print("Database already contains data, skipping initialization.")
        except Exception as e:
            # Handle the exception (table doesn't exist), create the table, and load data
            db.create_all()
            print("Database tables created.")
            load_json_data()


@app.cli.command("init_db")

@app.route('/')
def serve_index():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'index.html')

@app.route('/search', methods=['GET'])
def search_drugs():
    search_string = request.args.get('q', '')

    # Perform a case-insensitive search on the 'name' column
    results = Drug.query.filter(Drug.name.ilike(f"%{search_string}%")).all()

    # Convert the results to a list of dictionaries
    drugs = [{"id": drug.id, "name": drug.name, "description": drug.description, "released": drug.released} for drug in results]

    return jsonify(drugs)

if __name__ == '__main__':
    init_db()
    flask_host = os.environ.get('FLASK_HOST', '0.0.0.0')
    app.run(debug=True, host=flask_host)
