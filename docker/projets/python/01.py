import docker

client = docker.from_env()
output = client.containers.run("hello-world")
print(output.decode())