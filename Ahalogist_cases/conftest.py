import logging
import os
from datetime import date, datetime

import allure
import pytest
from selenium import webdriver

logging.basicConfig(
    filename=f"{os.getcwd()}/test_log.txt",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
)


@pytest.fixture(scope="session")
def ses_init(request):
    global driver
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": f"{os.getcwd()}/Downloads"}
    options.add_experimental_option("prefs", prefs)
    exc_env = request.config.getoption("--exc")
    env = request.config.getoption("--env")
    os.environ['Env'] = env
    if exc_env:
        options.add_argument(f"{exc_env}")
        options.add_argument('--window-size=1400,1080')

    # options.add_argument("--start-maximized")
    # options.add_argument("--window-size=1400,1080")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1380, 900)
    # print(f"New window size after maximizing: {new_size}")

    yield driver
    driver.quit()





def pytest_runtest_makereport(item, call):
    if call.when == "call":
        ses_init = item.funcargs.get("ses_init")
        if ses_init:
            screenshot_name = f"{item.name}_{str(date.today())}.png"
            screenshot_path = os.path.join("screenshots", screenshot_name)

            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")

            # Capture a screenshot using Selenium and save it
            ses_init.save_screenshot(screenshot_path)




@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    ses_init = item.funcargs.get("ses_init")
    if ses_init:
        if rep.when == "call":
            try:
                allure.attach(
                    ses_init.get_screenshot_as_png(),
                    name=f"{item.name}_{str(date.today())}.png",
                    attachment_type=allure.attachment_type.PNG,
                )

                browser_logs = ses_init.get_log("browser")
                error_logs = [log for log in browser_logs if log['level'] == 'SEVERE']

                # Attach filtered browser console log
                allure.attach(
                    str(error_logs),
                    name=f"{item.name}_error_logs.txt",
                    attachment_type=allure.attachment_type.TEXT,
                )
            except Exception as e:
                print(f"Failed to capture screenshot, console log, and network request URLs: {e}")


def pytest_runtest_logreport(report):
    if report.when == "call":
        # This code will run after each test case
        test_name = report.nodeid
        # Log messages with different logging levels
        if report.outcome == "passed":
            log_level = logging.INFO
        elif report.outcome == "failed":
            log_level = logging.ERROR
        else:
            log_level = logging.WARNING

        log_message = (
            f"{datetime.now()} - '{test_name}' finished with outcome: {report.outcome}"
        )
        logging.log(log_level, log_message)
