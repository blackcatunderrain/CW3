from flask import Blueprint, render_template
from posts.utils import Utils
from config import DATA_PATH_POSTS

posts = Blueprint("posts", __name__, template_folder="templates")


post_dao = Utils(DATA_PATH_POSTS)


@posts.route("/")
def page_posts_index():
    all_posts = post_dao.get_all()
    return render_template("index.html", posts=all_posts)
