import os
import random
import string
import subprocess
from datetime import date

from github import Github

from Config.config import TestData


class GitRepo:
    repository_path = f"{os.getcwd()}/allure-report"

    def git_process_command(self, command):
        try:
            subprocess.run(command, shell=True, check=True, cwd=self.repository_path)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while running command: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def push_to_git_repository(self):
        characters = string.ascii_letters + string.digits
        random_string = "".join(random.choice(characters) for _ in range(5))
        count = 1
        os.environ["Report_name"] = f"New_{random_string}"
        commands = [
            "git init",
            f"git branch New_{random_string}",
            f"git checkout New_{random_string}",
            "git add .",
            f'git commit -m "New_{date.today()}"',
            f"git remote add origin https://{TestData.Gittoken}@github.com/VivekQSPAutomation/QSP-Automation.git",
            f"git push -u origin New_{random_string}",
        ]
        while True:
            if count == 2:
                for _ in commands[1:]:
                    self.git_process_command(_)
                print("Code pushed successfully to the remote repository.")
                break
            else:
                for cmd in commands:
                    self.git_process_command(cmd)
                # self.get_remote_branches()

            count = count + 1

    def get_remote_branches(self):
        access_token = TestData.Gittoken
        g = Github(access_token)

        repo_name = "VivekQSPAutomation/QSP-Automation"
        repo = g.get_repo(repo_name)

        # Fetch all remote branches
        remote_branches = [branch.name for branch in repo.get_branches()]
        for _ in remote_branches:
            if "main" in _:
                pass
            else:
                self.git_process_command(f"git push origin --delete {_}")
