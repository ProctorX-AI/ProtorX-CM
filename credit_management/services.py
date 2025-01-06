from ..utils import get_db_handle
from django.conf import settings

# Get MongoDB handle
db_handle, mongo_client = get_db_handle(
    db_name=settings.MONGO_DB['NAME'],
    host=settings.MONGO_DB['HOST'],
    port=settings.MONGO_DB['PORT'],
    username=settings.MONGO_DB['USERNAME'],
    password=settings.MONGO_DB['PASSWORD'],
)

# Access specific collections (e.g., `credits`)
credits_collection = db_handle['credits']