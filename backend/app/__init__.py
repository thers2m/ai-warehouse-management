import os
from flask import Flask
from app.database_connector import db  # Giả sử bạn dùng Flask-SQLAlchemy hoặc extension connector riêng
from app.api.order_routes import order_bp
# from app.api.product_routes import product_bp
# from app.api.inventory_routes import inventory_bp
# from app.api.agent_routes import agent_bp
# from app.api.health_routes import health_bp
def test_connection():
    try:
        print("Connecting to Supabase...")

        response = (
            db.table("products")
            .select("id, name, price, stock_quantity")
            .limit(5)
            .execute()
        )

        if response.data is not None:
            print("✅ Supabase connection successful!")
        # print(f"Products found: {len(response.data)}")

        # for product in response.data:
        #     print(product)

    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        
def create_app(config_name=None):
    # Khởi tạo Flask app
    app = Flask(__name__)
    
    # Load cấu hình từ file config.py hoặc biến môi trường
    app.config.from_object('app.config.Config')
    test_connection()  # Kiểm tra kết nối cơ sở dữ liệu khi khởi tạo ứng dụng
    # db
    

    # 1. Khởi tạo Extensions (DB, Migrate, Cors, v.v.)
    # Ví dụ nếu dùng Flask-SQLAlchemy: db.init_app(app)
    
    # 2. Đăng ký các Blueprints (API Routes)
    # app.register_blueprint(health_bp, url_prefix='/api/health')
    # app.register_blueprint(product_bp, url_prefix='/api/products')
    app.register_blueprint(order_bp, url_prefix='/api/orders')
    # app.register_blueprint(inventory_bp, url_prefix='/api/inventory')
    # app.register_blueprint(agent_bp, url_prefix='/api/agent')

    @app.route('/')
    def index():
        return {"message": "AI Sales & Inventory Backend is running successfully!"}

    return app