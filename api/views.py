import logging
from flask import Blueprint, jsonify
from config import DATA_PATH_POSTS, DATA_PATH_COMMENTS
from posts.comment_dao import CommentDAO
from posts.post import Post
from posts.utils import Utils

bp_api = Blueprint("bp_api", __name__)

post_dao = Utils(DATA_PATH_POSTS)
comment_dao = CommentDAO(DATA_PATH_COMMENTS)

api_logger = logging.getLogger("api_logger")


@bp_api.route("/")
def api_index():
    return "Read the manual"


@bp_api.route("/posts/")
def api_posts_all():
    """Get all posts"""
    all_posts: list[Post] = post_dao.get_all()
    all_posts_as_dicts: list[dict] = [post.as_dict() for post in all_posts]
    api_logger.debug("got all posts")
    return jsonify(all_posts_as_dicts), 200


@bp_api.route("/posts/<int:pk>/")
def api_post_by_pk(pk: int):
    """Get post by pk"""
    post: Post | None = post_dao.get_by_pk(pk)
    return jsonify(post.as_dict()), 200
