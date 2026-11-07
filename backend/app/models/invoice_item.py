from app.extensions import db


class InvoiceItem(db.Model):
    __tablename__ = "invoice_items"
    __table_args__ = {"schema": "public"}

    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey("public.invoices.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("public.products.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Numeric(15, 2), nullable=False)

    invoice = db.relationship("Invoice", back_populates="items")
    product = db.relationship("Product")
