import os

config = {
    "PORT": 8000,
    "HOST": "0.0.0.0",
    "workers": 4,
    "PROD": os.getenv("PROD", None),
    "ALLOWED_HOSTS": ["*"],
    "POSTGRES_SQL_URL": f"postgresql://{os.getenv('POSTGRES_USER', 'admin')}:{os.getenv('POSTGRES_PASSWORD', 'admin123')}@{os.getenv('POSTGRES_HOST', 'database')}:{os.getenv('POSTGRES_PORT', '5432')}/{os.getenv('POSTGRES_DB', 'hospital_management')}",
    "REDIS_HOST": os.getenv("REDIS_HOST", "redis"),
    "REDIS_PORT": os.getenv("REDIS_PORT", '6379'),
}