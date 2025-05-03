from testcontainers.core.container import DockerContainer
import pymongo
import logging
import time

logging.basicConfig(level=logging.INFO)

def test_mongodb_connection():
    logs = ["🔧 Starting MongoDB Test using Testcontainers..."]

    with DockerContainer("mongo:latest") as mongo:
        mongo.with_exposed_ports(27017)
        mongo.with_command("--noauth")  # 💡 Disable authentication
        mongo.start()
        logs.append("🚀 MongoDB container started without authentication.")

        host = mongo.get_container_host_ip()
        port = mongo.get_exposed_port(27017)
        uri = f"mongodb://{host}:{port}/"
        logs.append(f"🌐 Attempting to connect to MongoDB at {uri}")

        time.sleep(2)  # Allow time for container to fully initialize

        try:
            client = pymongo.MongoClient(uri, serverSelectionTimeoutMS=5000)
            db = client.test_db
            collection = db.test_collection

            collection.insert_one({"message": "Hello, Mongo!"})
            doc = collection.find_one({"message": "Hello, Mongo!"})
            if doc:
                logs.append("✅ MongoDB insert and read successful, test passed!")
            else:
                logs.append("⚠️ Document not found in MongoDB.")
        except Exception as e:
            logs.append(f"❌ Error occurred while connecting to MongoDB: {str(e)}")

        logs.append("📦 Container stopped and removed.")

    return "\n".join(logs)

if __name__ == "__main__":
    print(test_mongodb_connection())
