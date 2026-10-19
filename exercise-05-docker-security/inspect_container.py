
import docker

client = docker.from_env()
container_name = "docker-security-test"

try:
    container = client.containers.get(container_name)
    container.reload()

    print("Container:", container.name)
    print("Status:", container.status)
    print("Image:", container.image.tags)
    print("Configured user:", container.attrs["Config"].get("User"))
    print(
        "AppArmor profile:",
        container.attrs.get("AppArmorProfile") or "Not reported by Docker"
    )

    print("\nContainer ports:")
    print(container.attrs["NetworkSettings"].get("Ports"))

except docker.errors.NotFound:
    print(f"Container '{container_name}' was not found.")
except docker.errors.DockerException as exc:
    print("Docker SDK error:", exc)
