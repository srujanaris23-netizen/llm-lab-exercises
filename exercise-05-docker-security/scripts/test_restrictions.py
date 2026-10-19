import docker

client = docker.from_env()
container = client.containers.get("docker-security-test")

checks = [
    (
        "Read application file",
        ["python", "-c", "print(open('/app/app.py').readline().strip())"]
    ),
    (
        "Write to /etc",
        [
            "python", "-c",
            "open('/etc/apparmor_exercise_test', 'w').write('test')"
        ]
    ),
    (
        "Write to /root",
        [
            "python", "-c",
            "open('/root/apparmor_exercise_test', 'w').write('test')"
        ]
    ),
]

for description, command in checks:
    print(f"\nTest: {description}")

    result = container.exec_run(command, demux=True)
    stdout, stderr = result.output

    print("Exit code:", result.exit_code)

    if stdout:
        print("Output:", stdout.decode(errors="replace").strip())

    if stderr:
        print("Error:", stderr.decode(errors="replace").strip())

    print(
        "Result:",
        "Succeeded" if result.exit_code == 0 else "Failed or denied"
    )
