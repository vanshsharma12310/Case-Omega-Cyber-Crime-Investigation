
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence"
OUTPUT = EVIDENCE / "sha256_hashes.txt"

def calculate_sha256(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:
        for block in iter(lambda: f.read(4096), b""):
            sha256.update(block)

    return sha256.hexdigest()

with open(OUTPUT, "w", encoding="utf-8") as report:
    for folder in ["evidence", "malware"]:
        directory = ROOT / folder

        for file_path in sorted(directory.rglob("*")):
            if file_path.is_file() and file_path != OUTPUT:
                digest = calculate_sha256(file_path)
                report.write(f"{digest}  {file_path.relative_to(ROOT)}\n")
                print(file_path.name, digest)

print("SHA-256 hash report generated:", OUTPUT)
