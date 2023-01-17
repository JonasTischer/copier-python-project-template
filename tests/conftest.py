from distutils.dir_util import copy_tree
from os import getenv
from pathlib import Path
from tempfile import TemporaryDirectory
from copier import run_copy
from git import Repo
from pytest import fixture
from dataclasses import dataclass

TEMPLATE_PATH = Path(__file__).parent.parent
@dataclass
class TestAnswers:
    project_name: str = "Test_project"
    
def project_dir(answers: dict):
    with TemporaryDirectory() as tmp_template_dir:
        if not getenv("CI"):
            copy_tree(TEMPLATE_PATH, tmp_template_dir)
            repo = Repo(tmp_template_dir)
            repo.git.add(all=True)
            repo.index.commit("Test template changes")
            src_path = tmp_template_dir
        else:
            src_path = str(TEMPLATE_PATH)

        tmp_dir = TemporaryDirectory()
        run_copy(
            src_path,
            tmp_dir.name,
            answers,
            vcs_ref="HEAD",
            exclude=("venv/", ".venv/"),
            quiet=True,
        )

    return tmp_dir


@fixture(scope="session")
def project_path():
    directory = project_dir(TestAnswers().__dict__)

    yield Path(directory.name)
    directory.cleanup()