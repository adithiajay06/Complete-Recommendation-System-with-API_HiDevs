import time

metrics_store = {
    "total_requests": 0,
    "avg_response_time_ms": 0
}


class MetricsCollector:

    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        elapsed = (time.time() - self.start_time) * 1000

        metrics_store["total_requests"] += 1

        total = metrics_store["total_requests"]
        current_avg = metrics_store["avg_response_time_ms"]

        metrics_store["avg_response_time_ms"] = (
            current_avg * (total - 1) + elapsed
        ) / total

        return elapsed