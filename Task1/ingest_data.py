import os
import pandas as pd
from sqlalchemy import create_engine

# الاتصال بقاعدة البيانات PostgreSQL التي أنشأناها على Docker
engine = create_engine('postgresql://postgres:postgres@localhost:5432/olist_db')

# مسار المجلد الحالي (حيث توجد ملفات الـ CSV)
folder_path = '.'

# استعراض كل الملفات في المجلد ورفع ملفات الـ CSV فقط
for file in os.listdir(folder_path):
    if file.endswith('.csv'):
        file_path = os.path.join(folder_path, file)
        table_name = file.replace('.csv', '')  # اسم الجدول سيكون نفس اسم ملف الـ CSV بدون اللاحقة
        
        print(f"Reading {file} and loading into table '{table_name}'...")
        
        # قراءة الملف باستخدام pandas (على دفعات إذا كان كبيراً لضمان السرعة)
        df = pd.read_csv(file_path)
        
        # إدخال البيانات إلى قاعدة البيانات PostgreSQL
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        
        print(f"Table '{table_name}' loaded successfully!\n")

print("All datasets have been successfully ingested into PostgreSQL!")