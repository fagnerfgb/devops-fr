import docker

client = docker.from_env()

container_id = "d52ebbd73bcd93fa667f2626136f0d065a53d4d08e7b023a5b49b25583841405"

container = client.containers.get(container_id)

container.remove(force=True)

print(f"Container {container_id} removido com sucesso.")