import os
import subprocess


class Storage:
    @staticmethod
    def get_files(bucket):
        if not bucket.startswith("gs://"):
            bucket = "gs://" + bucket
        res = subprocess.run(
            ["gsutil", "ls", "-r", bucket],
            check=True,
            stdout=subprocess.PIPE,
            universal_newlines=True,
        )
        try:
            res = [r for r in res.stdout.split("\n") if r and r[-1] != ":"]
        except (IndexError, Exception):
            res = []
        return res

    @staticmethod
    def copy_files(files):
        for source, destination in files:
            p = subprocess.Popen(
                ["gsutil", "cp", source, destination],
            )
        p.communicate()

    @staticmethod
    def sync_folder(source, destination):
        r = subprocess.run(
            ["gsutil", "-m", "rsync", "-r", source, destination],
            check=True,
            stdout=subprocess.PIPE,
            universal_newlines=True,
        )
        return r.stdout


if __name__ == "__main__":
    file = Storage()
    file.sync_folder(os.getcwd(), "gs://qspautomation-files/Ads-Script/")
