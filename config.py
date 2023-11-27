from flask_sqlalchemy import SQLAlchemy
import os
import pymysql

pymysql.install_as_MySQLdb()
db = SQLAlchemy()

#Environment Variable 
mysql_user = os.environ.get('MYSQL_USER', 'root')
mysql_root_password = os.environ.get('MYSQL_ROOT_PASSWORD', 'password123')


class Drug(db.Model):

    id = db.Column(db.String(36), primary_key=True)
    diseases = db.Column(db.JSON)
    description = db.Column(db.String(1024))
    name = db.Column(db.String(255))
    released = db.Column(db.String(10))  # Assuming 'YYYY/MM/DD' format

    def __init__(self, id, diseases, description, name, released):
        self.id = id
        self.diseases = diseases
        self.description = description
        self.name = name
        self.released = released

    def __repr__(self):
        return f'<Drug {self.name}>'
    
    def __str__(self):
        return f"Drug: {self.name}\nID: {self.id}\nDiseases: {self.diseases}\nDescription: {self.description}\nReleased: {self.released}"