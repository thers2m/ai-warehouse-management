from flask import Blueprint, jsonify
# from app.repositories.product_repository import list_products
from app.schemas.product_schema import serialize_product

bp = Blueprint("products", __name__, url_prefix="/api/products")


@bp.get("")
def get_products():
    return jsonify(data=[])
