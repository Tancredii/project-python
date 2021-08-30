from app import ma

class MovieSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "author", "release_date")
        ordered = True