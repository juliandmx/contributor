import os
import subprocess
from datetime import datetime

FILE_PATH = os.path.abspath(__file__)
REPO_PATH = os.path.dirname(FILE_PATH)
FILENAME = "cuntribute_here.txt"

def make_dummy_commit():
    os.chdir(REPO_PATH)

    # Update the dummy file with a timestamp
    with open(FILENAME, "a") as f:
        f.write(f"Update: {datetime.now()}\n")

    # Run git commands to add, commit, and push
    subprocess.run(["git", "add", FILENAME])
    subprocess.run(["git", "commit", "-m", f"Automated commit {datetime.now()}"])
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    make_dummy_commit()
