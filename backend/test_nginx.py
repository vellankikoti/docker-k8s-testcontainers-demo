from testcontainers.core.container import DockerContainer
import requests
import logging
import time

logging.basicConfig(level=logging.INFO)

def test_nginx_status():
    logs = ["🔧 Starting NGINX Test using Testcontainers..."]

    with DockerContainer("nginx:alpine") as nginx:
        nginx.with_exposed_ports(80)
        nginx.start()
        logs.append("🚀 NGINX container started.")

        host = nginx.get_container_host_ip()
        port = nginx.get_exposed_port(80)
        url = f"http://{host}:{port}"
        logs.append(f"🌐 Attempting to reach NGINX at {url}")

        time.sleep(2)  # Let container fully initialize

        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                logs.append("✅ NGINX responded with 200 OK")
            else:
                logs.append(f"⚠️ NGINX returned unexpected status: {response.status_code}")
        except Exception as e:
            logs.append(f"❌ Error occurred while connecting to NGINX: {str(e)}")

        logs.append("📦 Container stopped and removed.")

    return "\n".join(logs)

if __name__ == "__main__":
    print(test_nginx_status())
