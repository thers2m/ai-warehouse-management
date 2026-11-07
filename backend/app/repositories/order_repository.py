from app.extensions import db
from app.models import Invoice


def list_orders(status=None):
    query = db.select(Invoice).order_by(Invoice.id.desc())
    if status:
        query = query.where(Invoice.status == status)
    return db.session.execute(query).scalars().all()
