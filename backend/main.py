from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import logging
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)

@app.post("/action")
async def run_action(request: Request):
    data = await request.json()
    action = data.get("action")
    deployment = data.get("deployment")

    if not deployment and action in ["deploy", "delete", "test"]:
        return {"response": "❗ Please specify a valid deployment name."}

    try:
        if action == "deploy":
            output = subprocess.check_output(
                ["kubectl", "apply", "-f", f"{deployment}-pod.yaml"],
                text=True
            )
            return {"response": f"🚀 {deployment.capitalize()} Pod Deployed!\n{output}"}

        elif action == "delete":
            output = subprocess.check_output(
                ["kubectl", "delete", "pod", f"demo-{deployment}", "--ignore-not-found"],
                text=True
            )
            return {"response": f"🗑️ {deployment.capitalize()} Pod Deleted!\n{output}"}

        elif action == "status":
            output = subprocess.check_output(["kubectl", "get", "pods", "-o", "wide"], text=True)
            return {"response": f"📊 Current Pods:\n{output}"}

        elif action == "test":
            test_file = f"test_{deployment}.py"
            if not os.path.exists(test_file):
                return {"response": f"❗ Test file {test_file} not found."}

            output = subprocess.check_output(["python", test_file], text=True)
            return {"response": f"🧪 Test Output for {deployment.capitalize()}:\n{output}"}

        else:
            return {"response": "❓ Unknown action."}

    except subprocess.CalledProcessError as e:
        logging.error(f"Error occurred: {str(e)}")
        return {"response": f"❌ Error occurred:\n{e.output if hasattr(e, 'output') else str(e)}"}
