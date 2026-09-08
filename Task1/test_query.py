import pandas as pd
from sqlalchemy import create_engine

# الاتصال بقاعدة البيانات
engine = create_engine('postgresql://postgres:postgres@localhost:5432/olist_db')

# تجربة استعلام بسيط مع Join بين جدول الطلبات والعملاء
query = """
SELECT o.order_id, o.customer_id, c.customer_city, o.order_status 
FROM olist_orders_dataset o
JOIN olist_customers_dataset c ON o.customer_id = c.customer_id
LIMIT 5;
"""

df = pd.read_sql(query, engine)
print("--- Query Result (Join Success) ---")
print(df)