from testcontainers.core.container import DockerContainer

def run_demo():
    output_lines = []
    with DockerContainer("alpine:3.17") as container:
        container.with_command("echo 'Hello from Testcontainers'")
        logs = container.get_logs()
        output_lines.append(logs.decode())

    return "\n".join(output_lines)

if __name__ == "__main__":
    print(run_demo())
