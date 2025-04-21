import faker
from flask import Flask, jsonify
from faker import Faker
from flask import Flask, jsonify, request
from flask_httpauth import HTTPTokenAuth

app = Flask(__name__)
auth = HTTPTokenAuth(scheme="Bearer")
fake = Faker()

@app.route('/random-user', methods=['GET'])
def get_random_user():
    user = {
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address(),
        "phone": fake.phone_number(),
        "company": fake.company()
    }
    return jsonify(user)

TOKENS = {
    "mysecrettoken123": "authorized_user"
}

@auth.verify_token
def verify_token(token):
    if token in TOKENS:
        return TOKENS[token]
    return None

# Custom unauthorized handler
@auth.error_handler
def unauthorized():
    response = jsonify({"message": "Unauthorized Access", "error": "Invalid or missing token"})
    response.status_code = 401
    return response

@app.route('/protected', methods=['GET'])
@auth.login_required
def protected():
    return jsonify({"message": "Access granted!", "user": auth.current_user()}), 200

@app.route('/public', methods=['GET'])
def public():
    return jsonify({"message": "This is a public endpoint!"}), 200

if __name__ == '__main__':
    app.run(debug=True)