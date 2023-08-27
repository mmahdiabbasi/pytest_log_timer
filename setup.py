from setuptools import setup

setup(
    name="pytest-log-timer",
    version="1.1",
    description="plugin to record test execution time",
    author="mohamad mahdi Abbasi",
    packages=["pytest_log_timer"],
    install_requires=["pytest"],
    entry_points={"pytest11": ["timer_plugin = logtimer.timer_plugin"]},
)