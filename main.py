ALTER TABLE перевалы
ADD COLUMN status VARCHAR(10);

### Задача 2: Создание класса для взаимодействия с базой данных

import psycopg2
import os

class DatabaseHandler:
    def __init__(self):
        self.connection = psycopg2.connect(
            host=os.getenv('FSTR_DB_HOST'),
            port=os.getenv('FSTR_DB_PORT'),
            user=os.getenv('FSTR_DB_LOGIN'),
            password=os.getenv('FSTR_DB_PASS'),
            dbname='your_db_name'
        )
        self.cursor = self.connection.cursor()

    def add_new_pass(self, pass_data):
        sql = "INSERT INTO перевалы (name, description, altitude, status) VALUES (%s, %s, %s, %s)"
        pass_values = (pass_data['name'], pass_data['description'], pass_data['altitude'], 'new')
        self.cursor.execute(sql, pass_values)
        self.connection.commit()
### Задача 3: Создание REST API метода `POST submitData`

from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/submitData', methods=['POST'])
def submit_data():
    try:
        data = request.json
        db_handler = DatabaseHandler()
        db_handler.add_new_pass(data)
        return jsonify({"message": "Pass added successfully"}), 200
    except Exception as e:
        return jsonify({"": str(e)}), 500

if __name__ == '__main__':
    app.run()


