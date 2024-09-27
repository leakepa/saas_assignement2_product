from flask import Flask, jsonify, request

app = Flask(__name__)


products = {
    1: {"name": "Apple", "price": 0.5, "quantity": 100},
    2: {"name": "Banana", "price": 0.3, "quantity": 150},
    3: {"name": "Carrot", "price": 0.2, "quantity": 200},
}


@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)


@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if product:
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404


@app.route('/products', methods=['POST'])
def add_product():
    new_product = request.get_json()
    product_id = len(products) + 1  
    products[product_id] = {
        "name": new_product.get("name"),
        "price": new_product.get("price"),
        "quantity": new_product.get("quantity")
    }
    return jsonify({"message": "Product added", "product_id": product_id}), 201

if __name__ == '__main__':
    app.run(debug=True)