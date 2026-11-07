from app.extensions import db


class Product(db.Model):
    __tablename__ = "products"
    __table_args__ = {"schema": "public"}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Numeric(15, 2), nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime)
