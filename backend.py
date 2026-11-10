import datetime
import json
import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/news.all.get')
def get_news_all_articles():
  try:
    basedir = os.path.abspath(os.path.dirname(__file__))
    json_path = os.path.join(basedir, 'news_data.json')
    with open(json_path, 'r', encoding='utf-8') as file:
      data = json.load(file)
    return jsonify(data)
  except Exception as e:
    return jsonify({'error': str(e)}), 500


@app.route('/news.categories.get')
def get_news_categories():
  time_now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  data = {
      'title': 'List of Categories',
      'time': time_now_str,
      'categories': [
          {'id': 1, 'name': 'Sports'},
          {'id': 2, 'name': 'Politics'},
          {'id': 3, 'name': 'Education'},
      ],
  }
  return jsonify(data)


@app.route('/')
def index():
  return 'Welcome ENSIA Students from Flask!'


if __name__ == '__main__':
  app.run(port=8080)
