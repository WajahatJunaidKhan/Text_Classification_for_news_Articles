from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/articles/import', methods=['POST'])
def import_articles():
    data = request.get_json()
    return jsonify({"status": "success", "article_id": "unique-article-id"}), 201

@app.route('/api/articles/export', methods=['GET'])
def export_articles():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    categories = request.args.get('categories')
    articles = []
    return jsonify(articles)

@app.route('/api/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    return jsonify({"status": "success", "category_id": "unique-category-id"}), 201

@app.route('/api/categories/<category_id>', methods=['PUT'])
def update_category(category_id):
    data = request.get_json()
    return jsonify({"status": "success"}), 200

@app.route('/api/categories/<category_id>', methods=['DELETE'])
def delete_category(category_id):
    return jsonify({"status": "success"}), 200

@app.route('/api/categories', methods=['GET'])
def list_categories():
    categories = []
    return jsonify(categories)

if __name__ == '__main__':
    app.run(port=5000)
