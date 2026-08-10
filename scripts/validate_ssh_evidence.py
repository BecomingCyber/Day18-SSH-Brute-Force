from pathlib import Path

print("SSH Brute Force Evidence Validation")
print("=" * 40)

required_files = [
    "README.md",
    "findings.md",
    "commands_used.md",
    "images/q1-most-brute-user.png",
    "images/q2-thor-ip.png",
    "images/q3-thor-fail-count.png"
]

for file in required_files:
    if Path(file).exists():
        print(f"[PASS] Evidence exists: {file}")
    else:
        print(f"[FAIL] Missing evidence: {file}")


required_keywords = [
    "ssh",
    "failed",
    "authentication",
    "brute",
    "blocked"
]

content = ""

for file in ["README.md", "findings.md"]:
    if Path(file).exists():
        content += Path(file).read_text().lower()


for keyword in required_keywords:
    if keyword in content:
        print(f"[PASS] Investigation contains: {keyword}")
    else:
        print(f"[FAIL] Missing investigation detail: {keyword}")

print("\n[PASS] SSH evidence validation completed.")
