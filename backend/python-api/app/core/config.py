import os

class Settings:
    PROJECT_NAME = "TaskFlow API"
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    AWS_SQS_URL = os.getenv("AWS_SQS_URL", "<sqs-url>")

settings = Settings()