from app.extensions import db


class Invoice(db.Model):
    __tablename__ = "invoices"
    __table_args__ = {"schema": "public"}

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("public.users.id"), nullable=False)
    total_amount = db.Column(db.Numeric(15, 2), nullable=False)
    status = db.Column(db.String(30), nullable=False)
    note = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    customer = db.relationship("User")
    items = db.relationship("InvoiceItem", back_populates="invoice", lazy="selectin")
