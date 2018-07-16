"""Routes for modifying the Answer table."""

from flask import jsonify, request, make_response, Blueprint

from . import get_payload

from ..helpers.bphandler import BPHandler
from ..database.utils import add_value, table2dict
from ..database.tables.example_table import Example
from ..errors.notfound import NotFound


EXAMPLE_BP = Blueprint('example', __name__)
BPHandler.add_blueprint(EXAMPLE_BP)


@EXAMPLE_BP.route('/example/<int:example_id>', methods=['GET'])
def get_example(example_id):
    """Add a single answer to the database."""
    example = Example.query.filter_by(primary_key=example_id).first()
    if not example:
        raise NotFound('could not find value from example table')
    return make_response(jsonify(table2dict(example)), 200)


@EXAMPLE_BP.route('/example', methods=['POST'])
def post_example():
    payload = get_payload(request)

    #should do value checking here
    new = Example(**payload)
    add_value(new)

    return make_response(jsonify(table2dict(new)), 201)
