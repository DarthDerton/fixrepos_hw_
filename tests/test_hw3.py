import pytest
from hw3 import universal_file_counter


@pytest.fixture
def test_dir(tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.write_text("HellonWorldn")
    file2 = tmp_path / "file2.txt"
    file2.write_text("Thisnisnantestn")
    return tmp_path


@pytest.mark.parametrize("file_extension, tokenizer, expected_count", [
    ("txt", None, 6),
    ("txt", str.split, 7),
    ("md", None, 0),
    ("md", str.split, 0),
])
def test_universal_file_counter(test_dir, file_extension, tokenizer, expected_count):
    assert universal_file_counter(test_dir, file_extension, tokenizer) == expected_count