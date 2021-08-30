from flask import request
from sqlalchemy import or_

from app.admin.movie.models import Movie
from app.admin.movie.schemas import MovieSchema
from app.services.errors.exceptions import NotFoundError
from app.services.requests.params import custom_parameters


def create_movie(schema=None):
    dict_body = request.get_json()
    item = Movie().create_item(dict_body).save()
    if schema:
        item = MovieSchema().dump(item)
    return item


def get_movie(id, schema=None, columns=None):
    query = Movie.query
    if columns:
        query = query.with_entities(*[getattr(Movie, column) for column in columns])
    item = query.filter(Movie.id == id).first()
    if not item:
        raise NotFoundError()
    if schema:
        item = MovieSchema().dump(item)
    return item


def gets_movie(schema=None, columns=None):
    page, per_page, search = custom_parameters()
    query = Movie.query.filter(Movie.deleted_at.is_(None))
    if columns:
        query = query.with_entities(*[getattr(Movie, column) for column in columns])
    if search:
        query = query.filter(
            or_(Movie.name.like(f'%%{search}%%')))
    items = query.paginate(page, per_page, False)
    items_paginate = items
    if schema:
        items = MovieSchema(many=True).dump(items.items)

    return items, items_paginate


def update_movie(id, schema=None):
    item = get_movie(id)
    dict_body = request.get_json()
    item.update_item(dict_body).update()
    if schema:
        item = MovieSchema().dump(item)
    return item


def delete_movie(id):
    item = get_movie(id)
    item.delete()
    return True