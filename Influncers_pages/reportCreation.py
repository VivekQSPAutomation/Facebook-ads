import subprocess


class ReportCreation:
    def run_allure_generate(self, report_dir, output_dir):
        allure_command = ["allure", "generate", report_dir, "-o", output_dir, "--clean"]
        print(allure_command)
        try:
            subprocess.run(allure_command, check=True)
            print("Allure report generated successfully!")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while generating the Allure report: {e}")

    def run_refresh_script(self, script_path):
        try:
            # Replace "python" with the appropriate Python executable if needed
            subprocess.run([f"python", f"{script_path}"], check=True)
            print("Subprocess completed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while running the subprocess: {e}")
