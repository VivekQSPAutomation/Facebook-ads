def pytest_addoption(parser):
    parser.addoption(
        "--exc", action="store", default=False, help="Specify environment value"
    )
    parser.addoption(
        "--env", action="store", default="Stage", help="Specify environment value"
    )
