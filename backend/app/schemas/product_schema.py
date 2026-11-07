def serialize_product(product):
    return {
        "id": product.id,
        "name": product.name,
        "price": str(product.price),
        "stock_quantity": product.stock_quantity,
        "status": product.status,
    }
