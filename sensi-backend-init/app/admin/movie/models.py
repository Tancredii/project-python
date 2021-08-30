from app import db
from app.services.sqlalchemy.models import BaseModel


class Movie(BaseModel, db.Model):
    __tablename__ = "movie"
    name = db.Column(db.String(256), nullable=False)
    author = db.Column(db.String(256), nullable=False)
    release_date = db.Column(db.Date())

    def create_item(self, item_dict):
        self.name = item_dict["name"]
        self.author = item_dict["author"]
        self.release_date = item_dict.get("release_date", self.release_date)
        return self

    def update_item(self, item_dict):
        self.name = item_dict.get("name", self.name)
        self.author = item_dict.get("author", self.author)
        self.release_date = item_dict.get("release_date", self.release_date)
        return self
