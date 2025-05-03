from testcontainers.core.container import DockerContainer
import redis
import logging
import time

logging.basicConfig(level=logging.INFO)

def test_redis_connection():
    logs = ["🔧 Starting Redis Test using Testcontainers..."]

    with DockerContainer("redis:alpine") as redis_container:
        redis_container.with_exposed_ports(6379)
        redis_container.start()
        logs.append("🚀 Redis container started.")

        host = redis_container.get_container_host_ip()
        port = redis_container.get_exposed_port(6379)
        url = f"redis://{host}:{port}"
        logs.append(f"🌐 Attempting to connect to Redis at {url}")

        time.sleep(2)  # Let Redis fully initialize

        try:
            r = redis.StrictRedis(host=host, port=port, db=0)
            r.set("test_key", "test_value")
            value = r.get("test_key")
            if value == b'test_value':
                logs.append("✅ Redis is working fine, test passed!")
            else:
                logs.append("⚠️ Redis returned unexpected value.")
        except Exception as e:
            logs.append(f"❌ Error occurred while connecting to Redis: {str(e)}")

        logs.append("📦 Container stopped and removed.")

    return "\n".join(logs)

if __name__ == "__main__":
    print(test_redis_connection())
