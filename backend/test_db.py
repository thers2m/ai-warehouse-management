from app.database_connector import db


def test_connection():
    try:
        print("Connecting to Supabase...")

        response = (
            db.table("products")
            .select("id, name, price, stock_quantity")
            .limit(5)
            .execute()
        )

        print("✅ Supabase connection successful!")
        print(f"Products found: {len(response.data)}")

        for product in response.data:
            print(product)

    except Exception as e:
        print(f"❌ Database connection failed: {e}")


if __name__ == "__main__":
    test_connection()