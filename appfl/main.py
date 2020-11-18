from appfl.app import app
import appfl.view
from appfl.app import db
from appfl.posts.blueprint import posts


app.register_blueprint(posts, url_prefix='/blog')


if __name__ == '__main__':
    app.run()