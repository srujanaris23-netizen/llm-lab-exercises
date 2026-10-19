# Exercise 5: Docker Security and AppArmor

## 1. Objective
To demonstrate Docker container security through non-root execution, filesystem restrictions, Linux capability reduction, and prevention of privilege escalation. AppArmor support is being investigated separately.

## 2. Environment and Technology Stack
- Operating System: Windows 11
- Container platform: Docker Desktop
- Container engine: Docker Engine
- Linux environment: WSL2 with Ubuntu 24.04
- Application: Python Flask
- Container image: docker-security-app:1.0
- Automated tests: Python Docker SDK

## 3. Methodology
1. Created a Flask application with home, health, and security-test endpoints.
2. Built a Docker image using a Dockerfile.
3. Configured the application to run as the non-root user appuser.
4. Started the application in a standard container.
5. Created a hardened container with a read-only root filesystem.
6. Dropped all Linux capabilities and enabled no-new-privileges.
7. Mounted /tmp as temporary writable storage.
8. Tested application availability and filesystem restrictions.
9. Automated eight security checks using Python.

## 4. Security Controls
- Non-root execution: reduces the privileges available to the application.
- Read-only root filesystem: prevents modifications to the container's main filesystem.
- Temporary filesystem: allows temporary writes to /tmp.
- Capability dropping: removes Linux capabilities from the container.
- No-new-privileges: prevents processes from gaining additional privileges through execution.
- Health endpoint: verifies that the application remains available.

## 5. Test Cases and Results

| Test | Expected Result | Observed Result |
|---|---|---|
| Container running | Running | PASS |
| Non-root user | appuser | PASS |
| Read-only filesystem | Enabled | PASS |
| Linux capabilities | ALL dropped | PASS |
| No-new-privileges | Enabled | PASS |
| Health endpoint | HTTP 200, healthy | PASS |
| Write to /app | Denied | PASS |
| Write to /tmp | Allowed | PASS |

Automated test summary: 8/8 passed.

## 6. Test Evidence
- The /health endpoint returned status healthy.
- The / endpoint returned the Docker Security Exercise message.
- A write attempt to /app failed with a read-only filesystem error.
- A write attempt to /tmp succeeded.
- Docker inspection confirmed ReadonlyRootfs=true.
- Docker inspection confirmed CapDrop=["ALL"].
- Docker inspection confirmed no-new-privileges=true.

## 7. AppArmor Status and Limitation
The WSL Ubuntu environment reported AppArmor parameter N and stated that the AppArmor filesystem was not mounted. Therefore, custom AppArmor profile enforcement has not been demonstrated or verified in this environment. The Docker tests above demonstrate other container security controls and must not be presented as proof of AppArmor enforcement.

## 8. Conclusion
The exercise successfully demonstrated multiple Docker hardening controls while keeping the Flask application operational. The automated test script passed all eight checks. A separate Linux environment with active AppArmor support is still required to complete and verify the custom AppArmor profile portion.
