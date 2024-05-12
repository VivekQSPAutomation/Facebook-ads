import logging
import os
from datetime import date

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Initialize the logging module
logging.basicConfig(
    filename=f"{os.getcwd()}/test_log.txt",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
)


@pytest.fixture(scope="session")
def ses_init(request):
    chrome_options = Options()
    prefs = f"{os.getcwd()}/Influ_downloads"
    exc_env = request.config.getoption("--exc")
    env = request.config.getoption("--env")
    os.environ["Env"] = env
    print(os.environ.get("Env"))
    if exc_env:
        chrome_options.add_argument(f"{exc_env}")
        chrome_options.add_argument("--window-size=1400,1080")
    chrome_options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": prefs,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
        },
    )
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1380, 900)
    navigator_properties = driver.execute_script(
        """
        return {
            userAgent: navigator.userAgent,
            appVersion: navigator.appVersion,
            platform: navigator.platform,
            language: navigator.language,
            languages: navigator.languages,
            product: navigator.product,
            productSub: navigator.productSub,
            vendor: navigator.vendor,
            vendorSub: navigator.vendorSub
        };
    """
    )

    # Print the extracted properties
    print("Navigator Properties:", navigator_properties)
    yield driver
    driver.quit()


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
                error_logs = [log for log in browser_logs if log["level"] == "SEVERE"]

                # Attach filtered browser console log
                allure.attach(
                    str(error_logs),
                    name=f"{item.name}_error_logs.txt",
                    attachment_type=allure.attachment_type.TEXT,
                )
            except Exception as e:
                print(f"Failed to capture screenshot and console log: {e}")


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
            f"{date.today()} - '{test_name}' finished with outcome: {report.outcome}"
        )
        logging.log(log_level, log_message)
