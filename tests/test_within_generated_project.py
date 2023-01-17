import logging
from os import environ
from subprocess import PIPE, Popen

logging.basicConfig(level=logging.INFO)

def test_runs_tests_within_generated_project(project_path):
    logging.info("Running tests within generated project...")
    with Popen(
        ["pytest"],
        cwd=project_path,
        stdout=PIPE,
        bufsize=1,
        universal_newlines=True,
    ) as pytest_run:
        for i in pytest_run.stdout:
            print(i, end="")

    assert pytest_run.returncode == 0
