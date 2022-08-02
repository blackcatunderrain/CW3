import json
from json import JSONDecodeError
from posts.post import Post
from exceptions.exceptions import DataSourceError


class Utils:

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

    def _load_posts(self) -> list[Post]:
        """Возвращает список экземпляров Post"""
        data = self._load_data()
        list_posts = [Post(**data) for data in data]
        return list_posts

    def get_all(self) -> list[dict]:
        """Возвращает все посты"""
        return self._load_posts()

    def get_by_pk(self, pk: int):
        """Возвращает пост по PK"""
        if type(pk) != int:
            raise TypeError("pk must be an int")

        for post in self._load_posts():
            if post.pk == pk:
                return post

    def search_by_word(self, word: str) -> list[Post]:
        """Ищет посты по word"""
        result = []
        for post in self._load_posts():
            if word.lower() in post.content.lower():
                result.append(post)
        return result

    def get_by_poster(self, poster_name: str) -> list[Post]:
        result = []
        for post in self._load_posts():
            if poster_name.lower() in post.poster_name.lower():
                result.append(post)
        return result

