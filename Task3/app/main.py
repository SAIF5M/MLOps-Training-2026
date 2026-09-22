from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.predict import make_prediction
from src.config_loader import load_config

app = FastAPI(
    title="MLOps Late Delivery Inference API",
    description="API for predicting order delivery status (late or on time)",
    version="1.0.0"
)

class OrderInput(BaseModel):
    order_id: str
    customer_id: str
    order_purchase_timestamp: str
    product_category: str
    freight_value: float
    price: float

@app.get("/")
def health_check():
    """مسار للتحقق من أن الخدمة تعمل بشكل سليم (Health Check)"""
    return {"status": "healthy", "service": "MLOps Inference API"}

@app.get("/model/info")
def model_info():
    """مسار لعرض معلومات وإصدار الموديل الحالي"""
    config = load_config()
    return {
        "model_name": config["model"]["name"],
        "version": config["model"]["version"]
    }

@app.post("/predict")
def predict_order(order: OrderInput):
    """مسار التوقع لطلب واحد جديد"""
    try:
        input_data = order.dict()
        result = make_prediction(input_data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))