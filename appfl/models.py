from datetime import datetime
import re

from appfl.app import db


def slugify(s):
    pattern = r'[^\w+]'.encode('utf8')
    return re.sub(pattern, '-', s)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    # def __repr__(self):
    #     return f"<Post id: {}, title: {}>.format(self.id, self.title)"

    def __repr__(self):
        return str('<Post id: {}, title: {}>'.format(self.id, self.title))
