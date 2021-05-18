from flask import Flask
from flask import jsonify


app = Flask(__name__)

@app.route("/", methods=['GET'])
def tree():
    return jsonify(myFavouriteTree='pine-tree')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')