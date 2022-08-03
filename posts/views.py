from flask import Blueprint, render_template, abort, request
from posts.comment import Comment
from posts.comment_dao import CommentDAO
from posts.post import Post
from posts.utils import Utils
from config import DATA_PATH_POSTS, DATA_PATH_COMMENTS

posts = Blueprint("posts", __name__, template_folder="templates")


post_dao = Utils(DATA_PATH_POSTS)
comment_dao = CommentDAO(DATA_PATH_COMMENTS)


@posts.route("/")
def page_posts_index():
    all_posts = post_dao.get_all()
    return render_template("index.html", posts=all_posts)


@posts.route("/posts/<int:pk>")
def page_posts_single(pk: int):
    post: Post | None = post_dao.get_by_pk(pk)
    comments: list[Comment] = comment_dao.get_comments_by_post_pk(pk)
    if post is None:
        abort(404)
    return render_template("post.html", post=post, comments=comments)


@posts.route("/users/<user_name>")
def page_post_by_user(user_name):
    posts_: list[Post] = post_dao.get_by_poster(user_name)
    return render_template("user-feed.html", user_name=user_name, posts=posts_)


@posts.route("/search/")
def page_post_search():
    query: str = request.args.get("s", "")
    if query == "":
        posts_ = []
    else:
        posts_ = post_dao.search_by_word(query)
    return render_template("search.html", posts=posts_, query=query)



