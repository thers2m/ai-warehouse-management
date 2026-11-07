from app.extensions import db
from app.models import Product


def list_products():
    return db.session.execute(db.select(Product).order_by(Product.id)).scalars().all()
