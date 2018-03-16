from flask import Flask, request, jsonify
from db import connection
from query_generator import get_user_by_id_query, get_all_user_query, delete_user_by_id_query, insert_user, update_user_by_id

app = Flask(__name__)

@app.route('/api/users/<id>', methods=['GET'])
def get_user_by_id(id):
    with connection.cursor() as cursor:
        rows_count = cursor.execute(get_user_by_id_query(id))
        if rows_count == 0:
            return jsonify('No User with id - ' + id), 404
        else:
            return jsonify(cursor.fetchone()), 200


@app.route('/api/users', methods=['GET'])
def get_users():
        # read request arguments
        name = request.args.get('name')
        sort_by = request.args.get('sort_by')
        limit = request.args.get('limit')
        page = request.args.get('page')

        with connection.cursor() as cursor:

            rows_count = cursor.execute(get_all_user_query(name, sort_by, limit, page))
            if rows_count == 0:
                return jsonify('No Users'), 404
            else:
                return jsonify(cursor.fetchall()), 200


@app.route('/api/users/<id>', methods=['DELETE'])
def delete_user_by_id(id):
        with connection.cursor() as cursor:
            rows_count = cursor.execute(delete_user_by_id_query(id))
            if rows_count == 0:
                return jsonify('No User with id - ' + id), 404
            else:
                return jsonify('User deleted with id - ' + id), 200


@app.route('/api/users', methods=['POST'])
def add_user():
    req_data = request.get_json()

    # add validations for the request and fields, can have separate validator class for validation
    if req_data is None:
        return jsonify('Request is not valid'), 400
    else:
        first_name = ""
        last_name = ""
        company_name = ""
        age = None
        city = ""
        state = ""
        zip = None
        email = ""
        web = ""

        if 'first_name' in req_data:
            first_name = req_data['first_name']

        if 'last_name' in req_data:
            last_name = req_data['last_name']

        if 'company_name' in req_data:
            company_name = req_data['company_name']

        if 'age' in req_data:
            age = req_data['age']

        if 'city' in req_data:
            city = req_data['city']

        if 'state' in req_data:
            state = req_data['state']

        if 'zip' in req_data:
            zip = req_data['zip']

        if 'email' in req_data:
            email = req_data['email']

        if 'web' in req_data:
            web = req_data['web']

        with connection.cursor() as cursor:
            rows_count = cursor.execute(insert_user(first_name, last_name,
                                                    company_name, age, city, state, zip, email, web))
            if rows_count == 0:
                return jsonify('Error occured while saving user'), 404
            else:
                return jsonify('User added successfully'), 201

@app.route('/api/users/<id>', methods=['PUT'])
def update_user(id):
    with connection.cursor() as cursor:

        req_data = request.get_json()
        if req_data is None:
            return jsonify('Request is not valid'), 400
        else:
            rows_count = cursor.execute(get_user_by_id_query(id))
            if rows_count == 0:
                return jsonify('No User with id - ' + id), 404
            else:
                data = cursor.fetchone()
                first_name = data['first_name']
                last_name = data['last_name']
                company_name = data['company_name']
                age = data['age']
                city = data['city']
                state = data['state']
                zip = data['zip']
                email = data['email']
                web = data['web']

                if 'first_name' in req_data:
                    first_name = req_data['first_name']

                if 'last_name' in req_data:
                    last_name = req_data['last_name']

                if 'company_name' in req_data:
                    company_name = req_data['company_name']

                if 'age' in req_data:
                    age = req_data['age']

                if 'city' in req_data:
                    city = req_data['city']

                if 'state' in req_data:
                    state = req_data['state']

                if 'zip' in req_data:
                    zip = req_data['zip']

                if 'email' in req_data:
                    email = req_data['email']

                if 'web' in req_data:
                    web = req_data['web']

                rows_count = cursor.execute(update_user_by_id(id, first_name, last_name, company_name, age,
                                                              city, state, zip, email, web))
                if rows_count == 0:
                      return jsonify('nothing to update for User with id - ' + id), 404
                else:
                     return jsonify('Successfully Updated User with id - ' + id), 200

if __name__ == '__main__':
    app.run(debug=True)