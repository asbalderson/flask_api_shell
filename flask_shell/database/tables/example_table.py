"""The answer table."""
from .. import DB


class Example(DB.Model):

    __tablename__ = 'example'
    primary_key = DB.Column(DB.Integer, nullable=False, primary_key=True)
    integer = DB.Column(DB.Integer, nullable=False)
    string = DB.Column(DB.Text, nullable=False)
    boolean = DB.Column(DB.Boolean, nullable=False, default=False)
    date = DB.Column(DB.DateTime)
    #other = DB.Column(DB.Integer, ForeignKey("other.id")
