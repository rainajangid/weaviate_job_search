import os
import weaviate
from dotenv import load_dotenv
load_dotenv()


def connect():
    headers = {
        "X-OpenAI-Api-Key": os.getenv("OPENAI_APIKEY")
    }
    client = weaviate.connect_to_local(headers=headers)
    return client