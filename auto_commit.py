import os
import datetime

# Path to your repo
repo_path = r"C:\Users\richu\my-first-repo"

# Change working directory
os.chdir(repo_path)

# Update a dummy file to make git see a change
dummy_file = "dummy.txt"
with open(dummy_file, "a") as f:
    f.write(f"Update: {datetime.datetime.now()}\n")

# Commit message with timestamp
message = f"Auto commit {datetime.datetime.now()}"

# Run git commands
os.system("git add .")
os.system(f'git commit -m "{message}"')
os.system("git push origin main")
