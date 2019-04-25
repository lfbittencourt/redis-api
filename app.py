from flask import Flask, jsonify, request
import redis

app = Flask(__name__)
r = redis.Redis(host='database', port=6379, decode_responses=True)


@app.route('/cart/<int:user_id>', methods=['POST'])
def create_cart(user_id):
    if cart_exists(user_id):
        return create_error_response('Cart exists'), 400

    # We are doing nothing here. Cart will be created when we add a product
    return jsonify([])


@app.route('/cart/<int:user_id>/products', methods=['POST'])
def add_product_to_cart(user_id):
    product_id = request.get_json(force=True).get('product_id')

    if not isinstance(product_id, int) or product_id <= 0:
        return create_error_response('Invalid product id'), 400

    r.sadd(user_id, product_id)

    return jsonify(get_cart(user_id))


@app.route('/cart/<int:user_id>/products/<int:product_id>', methods=['DELETE'])
def delete_product_from_cart(user_id, product_id):
    if not cart_exists(user_id):
        return create_error_response('Cart not found'), 404

    if not r.srem(user_id, product_id):
        return create_error_response('Product not found in cart'), 404

    return jsonify(get_cart(user_id))


@app.route('/cart/<int:user_id>')
def get_cart(user_id):
    if not cart_exists(user_id):
        return create_error_response('Cart not found'), 404

    return jsonify(get_cart(user_id))


@app.route('/cart/<int:user_id>', methods=['DELETE'])
def delete_cart(user_id):
    if not r.delete(user_id):
        return create_error_response('Cart not found'), 404

    return jsonify(True)


def cart_exists(user_id):
    return bool(r.exists(user_id))


def get_cart(user_id):
    return list(int(x) for x in r.smembers(user_id))


def create_error_response(message):
    return jsonify({
        'error': message
    })
