import docker
import urllib.request
import json

client = docker.from_env()
container_name = "docker-security-hardened"
passed = 0
total = 0

def check(name, condition, details=""):
    global passed, total
    total += 1
    result = "PASS" if condition else "FAIL"
    print(f"[{result}] {name}")
    if details:
        print(f"       {details}")
    if condition:
        passed += 1

container = client.containers.get(container_name)
container.reload()
attrs = container.attrs
config = attrs["HostConfig"]

check("Container is running", container.status == "running",
      f"Status: {container.status}")

check("Runs as non-root user",
      attrs["Config"].get("User") == "appuser",
      f"User: {attrs['Config'].get('User')}")

check("Read-only root filesystem",
      config.get("ReadonlyRootfs") is True)

check("All Linux capabilities dropped",
      "ALL" in (config.get("CapDrop") or []))

security_options = config.get("SecurityOpt") or []
check("No-new-privileges enabled",
      "no-new-privileges=true" in security_options)

try:
    with urllib.request.urlopen(
        "http://localhost:5006/health", timeout=5
    ) as response:
        body = json.loads(response.read().decode())
        check("Health endpoint responds",
              response.status == 200 and body.get("status") == "healthy")
except Exception as exc:
    check("Health endpoint responds", False, str(exc))

result = container.exec_run([
    "python", "-c",
    "open('/app/security-write-test.txt','w').write('test')"
])
check("Write to /app is blocked", result.exit_code != 0)

result = container.exec_run([
    "python", "-c",
    "open('/tmp/security-write-test.txt','w').write('test')"
])
check("Write to /tmp is allowed", result.exit_code == 0)

print(f"\nSecurity test summary: {passed}/{total} passed")
if passed != total:
    raise SystemExit(1)
