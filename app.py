from flask import Flask, jsonify, request
app = Flask(__name__)
database = {}


@app.route('/cart/<int:user_id>', methods=['POST'])
def create_cart(user_id):
    if cart_exists(user_id):
        return create_error_response('Cart exists'), 400

    cart = []
    database[user_id] = cart

    return jsonify(cart)


@app.route('/cart/<int:user_id>/products', methods=['POST'])
def add_product_to_cart(user_id):
    if not cart_exists(user_id):
        return create_error_response('Cart not found'), 404

    product_id = request.get_json(force=True).get('product_id')

    if not isinstance(product_id, int) or product_id <= 0:
        return create_error_response('Invalid product id'), 400

    if not product_exists_in_cart(user_id, product_id):
        database[user_id].append(product_id)

    return jsonify(database[user_id])


@app.route('/cart/<int:user_id>/products/<int:product_id>', methods=['DELETE'])
def delete_product_from_cart(user_id, product_id):
    if not cart_exists(user_id):
        return create_error_response('Cart not found'), 404

    try:
        database[user_id].remove(product_id)
    except ValueError:
        return create_error_response('Product not found in cart'), 404

    return jsonify(database[user_id])


@app.route('/cart/<int:user_id>')
def get_cart(user_id):
    if not cart_exists(user_id):
        return create_error_response('Cart not found'), 404

    return jsonify(database[user_id])


@app.route('/cart/<int:user_id>', methods=['DELETE'])
def delete_cart(user_id):
    try:
        del database[user_id]
    except KeyError:
        return create_error_response('Cart not found'), 404

    return jsonify(True)


def cart_exists(user_id):
    return database.get(user_id) is not None


def product_exists_in_cart(user_id, product_id):
    return cart_exists(user_id) and product_id in database[user_id]


def create_error_response(message):
    return jsonify({
        'error': message
    })
