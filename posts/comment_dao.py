from json import JSONDecodeError
import json
from exceptions.exceptions import DataSourceError
from posts.comment import Comment


class CommentDAO:

    def __init__(self, path):
        self.path = path

    def _load_data(self) -> list[dict]:
        """Загружаем JSON из файла"""
        try:
            with open(self.path, 'r', encoding='UTF-8') as file:
                data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f'Can not get data from file {self.path}')
        return data

    def _load_comments(self) -> list[Comment]:
        """Возвращает список экземпляров Comment"""
        comments_data = self._load_data()
        list_comments = [Comment(**comments_data) for comments_data in comments_data]
        return list_comments

    def get_comments_by_post_pk(self, post_id: int) -> list[Comment]:
        """Возвращает все комментарии к посту"""
        comments: list[Comment] = self._load_comments()
        comments_match: list[Comment] = [c for c in comments if c.post_id == post_id]
        return comments_match

