import docker

client = docker.from_env()

container = client.containers.run(
    "nginx", 
    detach=True,
    ports={"80/tcp": ("0.0.0.0", 8080)}
)

print(f"Container ID: {container.id}")