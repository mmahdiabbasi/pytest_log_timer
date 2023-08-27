import pytest
import datetime 

def pytest_addoption(parser):
    parser.addoption(
        '--logfile',
        action = 'store',
        default = 'logfile.txt',
        help = 'name of log file'
    )

@pytest.hookimpl(hookwrapper=True)
def pytest_sessionstart(session):
    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    log = "starting test at: " + dt_string
    write_outout(log)    
    yield

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_setup(item):
    global log
    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    log = f"function {item.name} tested at: " + dt_string
    write_outout(log)
    yield

@pytest.hookimpl
def pytest_report_teststatus(report):
    if report.when == "call":
        if report.outcome == "failed":
            log = "test failed"
        elif report.outcome == "passed":
            log = "test passed"
        write_outout(log)
    yield

@pytest.hookimpl(hookwrapper=True)
def pytest_sessionfinish(session):
    file_name = session.config.getoption("--format")
    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    log.append("all tests are finished at : " + dt_string)

def write_outout(log):
    with open("test_results.txt", mode="w") as file:
        file.write(log)
        file.write('\n')