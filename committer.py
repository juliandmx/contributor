import os
import subprocess
from datetime import datetime

#pic without last column so there aren't 2 empty columns in a row
picture = [
    [0]*28,
    [0,1,0,0,1,0,1,0,0,0,1,1,0,0,0,1,1,0,0,1,1,1,0,0,1,1,1,1],
    [0,1,0,1,1,1,1,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,0],
    [0,1,0,1,1,1,1,1,0,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,1,1,1,0],
    [0,1,0,0,1,1,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,0],
    [0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,1,1,0,0,1,1,1,0,0,1,1,1,1],
    [0]*28
]

FILE_PATH = os.path.abspath(__file__)
REPO_PATH = os.path.dirname(FILE_PATH)
FILENAME = "contribute_here.txt"
start_date = datetime(2025, 7, 20)

def commit_day():
    today = datetime.now()
    # y = 0: monday, y = 6: sunday
    y = today.weekday()
    # shift for github contribution
    y = (y+1)%7

    diff = today - start_date
    x = (diff.days // 7) % 28

    if picture[y][x] == 1:
        print(f"x: {x}, y: {y}, color: 🟩")
        return True
    print(f"x: {x}, y: {y}, color: ⬛")
    return False

def make_dummy_commit():
    if (commit_day()):

        os.chdir(REPO_PATH)

        subprocess.run(['git', 'config', 'user.email', 'julian@dammdesign.de'], check=True)
        subprocess.run(['git', 'config', 'user.name', 'juliandmx'], check=True)


        #Commit 5 times
        for i in range(5):
            # Update the dummy file with a timestamp
            with open(FILENAME, "a") as f:
                f.write(f"Update: {datetime.now()}\n")

            # Run git commands to add, commit, and push
            subprocess.run(["git", "add", FILENAME], check=True)
            subprocess.run(["git", "commit", "-m", f"Automated commit {datetime.now()}"], check=True)
            subprocess.run(["git", "push"], check=True)

if __name__ == "__main__":
    make_dummy_commit()

    #test image
    color_map = {
        0: "⬛",
        1: "🟩"
    }
    for row in picture:
        print("".join(color_map[p] for p in row))
