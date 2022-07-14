import pytest
from posts.post import Post
from posts.utils import Utils


def check_fields(post):
    fields = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]

    for field in fields:
        assert hasattr(post, field), f"No field {field}"


class TestUtils:

    @pytest.fixture
    def post_utils(self):
        post_utils_instance = Utils("data_mock.json")
        return post_utils_instance

    def test_get_all_types(self, post_utils):
        posts = post_utils.get_all()
        assert type(posts) == list, "Incorrect type"

        post = post_utils.get_all()[0]
        assert type(post) == Post, "Incorrect type"

    def test_get_all_fields(self, post_utils):
        post = post_utils.get_all()[0]
        check_fields(post)

    def test_get_all_correct_ids(self, post_utils):
        posts = post_utils.get_all()
        correct_pks = {1, 2, 3}
        pks = set([post.pk for post in posts])
        assert pks == correct_pks, "Didn't match id"

    def test_get_by_pk_types(self, post_utils):
        post = post_utils.get_by_pk(1)
        assert type(post) == Post, "Incorrect type"

    def test_get_by_pk_fields(self, post_utils):
        post = post_utils.get_by_pk(1)
        check_fields(post)

    def test_get_by_pk_none(self, post_utils):
        post = post_utils.get_by_pk(9991)
        assert post is None, "Should be None"

    @pytest.mark.parametrize("pk", [1, 2, 3])
    def test_get_by_pk_correct_id(self, post_utils, pk):
        post = post_utils.get_by_pk(pk)
        assert post.pk == pk, "Incorrect PK"





