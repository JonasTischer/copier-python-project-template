import pytest

    
def test_within_generated_project(project_path):
    assert pytest.main([project_path, "-vs"]) == 0
