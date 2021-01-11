from app.src.file_paths import base_solutions_path
from app.src.files import get_all_files_in_path


def test_index_get(client):
    # GIVEN
    expected_number_of_files = 12
    expected_extension_of_files = ".png"

    # WHEN
    rv = client.get("/")
    solution_files = get_all_files_in_path(base_solutions_path)

    # THEN
    assert "200" in rv.status
    assert "OK" in rv.status
    assert len(solution_files) == expected_number_of_files

    for file in solution_files:
        file.endswith(expected_extension_of_files)
