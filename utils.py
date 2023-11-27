import json
from config import db, Drug
def load_json_data():    # For Loading Json data to database.

        with open('dataset.json', 'r') as file:
                data = json.load(file)

        for drug_data in data.get('drugs', []):
                drug = Drug(
                        id=drug_data['id'],
                        diseases=drug_data['diseases'],
                        description=drug_data['description'],
                        name=drug_data['name'],
                        released=drug_data['released'].replace('-', '/')
        )
                db.session.add(drug)
        db.session.commit()
