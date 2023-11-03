import os
import subprocess

main_folder = "/home/bosstoner/codeStorage/testfolder"
new_branch_name = "feature/hooksignore4"


def create_new_branch(repo_folder):
    try:
        subprocess.check_call(["git", "checkout", "master"], cwd=repo_folder)
        subprocess.check_call(["git", "checkout", "-b", new_branch_name], cwd=repo_folder)
        print(f"Created branch {new_branch_name} based on 'master' in {repo_folder}")
    except subprocess.CalledProcessError as e:
        print(f"Error creating branch in {repo_folder}: {e}")


def update_gitignore(repo_folder):
    gitignore_path = os.path.join(repo_folder, ".gitignore")
    
    if not os.path.exists(gitignore_path):
        with open(gitignore_path, "w") as gitignore_file:
            gitignore_file.write("hooks.json\n")
        print(f"Created .gitignore and added 'hooks.json' in {repo_folder}")
    else:
        with open(gitignore_path, "a") as gitignore_file:
            gitignore_file.write("\nhooks.json\n")
        print(f"Added 'hooks.json' in {repo_folder}")

    try:
        subprocess.check_call(["git", "add", ".gitignore"], cwd=repo_folder)
        subprocess.check_call(["git", "commit", "-m", "Add hooks.json to .gitignore"], cwd=repo_folder)
        print(f"Committed changes in {repo_folder}")
            
        subprocess.check_call(["git", "push", "origin", new_branch_name], cwd=repo_folder)
        print(f"Pushed changes in {repo_folder}")
    except subprocess.CalledProcessError as e:
        print(f"Error in Git commands for {repo_folder}: {e}")



for subfolder in os.listdir(main_folder):
    subfolder_path = os.path.join(main_folder, subfolder)
    
    if os.path.isdir(subfolder_path) and os.path.exists(os.path.join(subfolder_path, ".git")):
        create_new_branch(subfolder_path)
        update_gitignore(subfolder_path)
