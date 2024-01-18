from sqlalchemy import inspect
from sqlalchemy.orm.properties import ColumnProperty

from . import db
from .budget_enum import budget_enum

# common columns and methods across multiple data models can be added via a Mixin class:
# https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/mixins.html

# see examples of Mixins in current and past Blueprint projects:
# https://github.com/uwblueprint/dancefest-web/blob/master/db/models.py#L10-L70
# https://github.com/uwblueprint/plasta/blob/master/backend/app/models/mixins.py#L10-L95

class Reviewer(db.Model):
    # define the restaurants table

    __tablename__ = 'reviewers'


    restaurant_id = db.Column(db.Integer, ForeignKey('restaurants.id'), nullable=False)

    # id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    review = db.Column(db.String(250))

    budget = db.Column(budget_enum)
    description = db.Column(db.String(250))
    rating = db.Column(db.Integer)

    # must define how to convert to a dict so that Restaurant can eventually be serialized into JSON
    # this would be a good method to include in a base Mixin
    def to_dict(self, include_relationships=False):
        cls = type(self)
        # mapper allows us to grab the columns of a Model // uses 
        mapper = inspect(cls)
        formatted = {}
        for column in mapper.attrs:
            field = column.key
            attr = getattr(self, field)
            # if it's a regular column, extract the value
            if isinstance(column, ColumnProperty):
                formatted[field] = attr
            # otherwise, it's a relationship field
            # (currently not applicable, but may be useful for restaurant groups)
            elif include_relationships:
                # recursively format the relationship
                # don't format the relationship's relationships
                formatted[field] = [obj.to_dict() for obj in attr]
        return formatted

