import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import items

blp = Blueprint("Items", __name__, description="Operations on stores")


@blp.route("/item/<string:item_id>")
class Store(MethodView):
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Store not found.")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": f"Store with id {item_id} has been deleted"}
        except KeyError:
            abort(404, message="Store not found.")

    def put(self, item_id):
        item_data = request.get_json()
        if "price" not in item_data or "name" not in item_data:
            abort(400, message="Bad request. Ensure 'price' and 'name' are included in the JSON payload")
        try:
            item = items[item_id]
            item["name"] = item_data["name"]
            item["price"] = item_data["price"]
            # below line performs the same as the above lines - new dict merge update operator
            # item |= item_data
            return item
        except KeyError:
            abort(404, message="Item not found.")
