from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://Mohan-2004:Mohan-2004@cluster0.wx48bvi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

try:
    client.admin.command('ping')
    print("[OK] Connected to MongoDB successfully!")
except Exception as e:
    print(f"[ERROR] MongoDB connection failed: {e}")

db = client["catering_db"]

collection = db["caterers"]