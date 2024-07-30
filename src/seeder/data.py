# from src.orm.article import ArticleOrm
# from src.orm.user import UserOrm
from time import time
from bcrypt import hashpw, gensalt
from uuid import uuid4

data = [
  {
    'target_class': 'src.orm.article:ArticleOrm',
    'data': [
      {
        'id': uuid4(),
        'title': 'Menelusuri Jejak Kepramukaan: Sejarah, Nilai, dan Peranannya Kini',
        'cover_url': 'https://akcdn.detik.net.id/community/media/visual/2023/08/10/ilustrasi-pramuka-1_169.jpeg?w=700&q=90',
        'description': 'Menelusuri Jejak Kepramukaan: Sejarah, Nilai, dan Peranannya Kini',
        'article_url': 'https://pramuka.or.id/gerakan-pramuka/',
        'created_at' : time(),
        'updated_at': None,
      },
      {
        'id': uuid4(),
        'title': 'Membangun Karakter Melalui Kepramukaan: Peran Pendidikan Non-formal',
        'cover_url': 'https://mtsn1kotamalang.sch.id/wp-content/uploads/2015/04/pramuka11.jpg',
        'description': 'Membangun Karakter Melalui Kepramukaan: Peran Pendidikan Non-formal',
        'article_url': 'https://id.wikipedia.org/wiki/Gerakan_Pramuka_Indonesia',
        'created_at' : time(),
        'updated_at': None,
      },
      {
        'id': uuid4(),
        'title': '5 Langkah Menuju Kegiatan Kepramukaan yang Menginspirasi',
        'cover_url': 'https://cdn1-production-images-kly.akamaized.net/tzcdvSZ9J8Dk0hSB6ZT9cqvD9bE=/1280x720/smart/filters:quality(75):strip_icc():format(webp)/kly-media-production/medias/2332408/original/088424600_1534416186-Napak-Tilas-Kemerdekaan-RI-di-Tugu-Proklamasi6.jpg',
        'description': '5 Langkah Menuju Kegiatan Kepramukaan yang Menginspirasi',
        'article_url': 'https://polbangtanmalang.ac.id/courses/learn-php-programming-from-scratch/',
        'created_at' : time(),
        'updated_at': None,
      },
    ],
  },
  {
    'target_class': 'src.orm.user:UserOrm',
    'data': [
      {
        'username': 'isnandar.1471@gmail.com',
        'email': 'isnandar.1471@gmail.com',
        'password': hashpw("12345678".encode(), gensalt()).decode(),
      },
      {
        'username': 'user1@fake.mail',
        'email': 'user1@fake.mail',
        'password': hashpw('12345678'.encode(), gensalt()).decode(),
      },
      {
        'username': 'user2@fake.mail',
        'email': 'user2@fake.mail',
        'password': hashpw('12345678'.encode(), gensalt()).decode(),
      }
    ],
  },
]