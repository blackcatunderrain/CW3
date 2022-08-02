from flask import Blueprint, render_template, abort
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
