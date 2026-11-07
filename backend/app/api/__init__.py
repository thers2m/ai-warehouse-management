from .health_routes import bp as health_bp
from .product_routes import bp as product_bp
from .order_routes import bp as order_bp
from .inventory_routes import bp as inventory_bp
from .agent_routes import bp as agent_bp


def register_blueprints(app):
    for bp in [health_bp, product_bp, order_bp, inventory_bp, agent_bp]:
        app.register_blueprint(bp)
