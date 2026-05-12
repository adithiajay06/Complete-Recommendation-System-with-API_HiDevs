import logging
import uuid

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("recommendation-system")


def generate_trace_id():
    return str(uuid.uuid4())