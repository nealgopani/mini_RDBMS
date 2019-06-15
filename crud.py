from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api, reqparse
import psycopg2
import json


app = Flask(__name__)
api = Api(app)

conn = psycopg2.connect('postgres://postgres:******@localhost:5432/dvdrental')

@app.route('/')
def home():
    return render_template('test.html')


class Actor(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('actor_id', type = int)
        self.parser.add_argument('first_name', type = str)
        self.parser.add_argument('last_name', type = str)
        self.parser.add_argument('last_update')

    def get(self):
        cur = conn.cursor()
        actor_id = self.parser.parse_args()['actor_id']
        
        if actor_id:
            cur.execute(f'SELECT * FROM actor WHERE actor_id = {actor_id} ORDER BY actor_id')
            return jsonify(cur.fetchall())
        
        cur.execute('SELECT * FROM actor ORDER BY actor_id')
        table = cur.fetchall()
        return jsonify(table)


    def post(self):
        cur = conn.cursor()
        json_data = request.get_json()
        if json_data:
            actor_id, first_name, last_name, last_update = json_data['actor_id'], json_data['first_name'], json_data['last_name'], json_data['last_update']
        else:
            actor_id, first_name, last_name, last_update = [self.parser.parse_args()[k] for k in self.parser.parse_args()]
        sql = f'INSERT INTO actor (actor_id, first_name, last_name, last_update) VALUES {actor_id, first_name, last_name, last_update}'
        cur.execute(sql)
        conn.commit()
        return jsonify(self.parser.parse_args())


    def put(self):
        cur = conn.cursor()
        json_data = request.get_json()
        if json_data:
            actor_id, first_name, last_name, last_update = [json_data[k] for k in json_data]
        else:
            actor_id, first_name, last_name, last_update = [self.parser.parse_args()[k] for k in self.parser.parse_args()]
        sql = f"UPDATE actor SET first_name='{first_name}',last_name='{last_name}',last_update='{last_update}' WHERE actor_id = {actor_id}"
        cur.execute(sql)
        conn.commit()
        return jsonify(self.parser.parse_args())

    def delete(self):
        cur = conn.cursor()
        json_data = request.get_json()
        if json_data:
            actor_id = json_data['actor_id']
        else:
            actor_id, first_name, last_name, last_update = [self.parser.parse_args()[k] for k in self.parser.parse_args()]
        sql = f"DELETE FROM actor WHERE actor_id = {actor_id}"
        cur.execute(sql)
        conn.commit()
        return jsonify({actor_id: 'deleted'})


api.add_resource(Actor,'/actor')

if __name__ == '__main__':
    app.run(debug=True)