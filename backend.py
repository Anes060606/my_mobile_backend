import datetime
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/news.all.get')
def get_news_all_articles():
  # بيانات الأخبار مدمجة مباشرة لتجنب أي أخطاء في مسار الملفات على السحابة
  data = [
      {
          'id': 1,
          'title': (
              'Universities Adopt AI-Powered Learning Platforms for'
              ' Personalized Education'
          ),
          'image_url': 'https://images.unsplash.com/photo-1501504905252-473c47e087f8',
          'description': (
              'Major universities across the country are implementing'
              ' artificial intelligence systems to create personalized'
              ' learning experiences for students.'
          ),
          'category_id': 3,
      },
      {
          'id': 2,
          'title': (
              'Study Reveals Benefits of Bilingual Education in Early Childhood'
          ),
          'image_url': 'https://images.unsplash.com/photo-1503676260728-1c00da094a0b',
          'description': (
              'New research shows that children enrolled in bilingual'
              ' education programs demonstrate enhanced cognitive flexibility.'
          ),
          'category_id': 3,
      },
      {
          'id': 3,
          'title': (
              'Government Announces $2 Billion Investment in STEM Education'
          ),
          'image_url': 'https://images.unsplash.com/photo-1532094349884-543bc11b234d',
          'description': (
              'The Department of Education unveiled a comprehensive funding'
              ' package aimed at improving science and technology programs.'
          ),
          'category_id': 3,
      },
  ]
  return jsonify(data)


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
  app.run()
