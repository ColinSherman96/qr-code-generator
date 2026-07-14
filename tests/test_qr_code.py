from main import is_valid_url, generate_qr_code, create_directory


def test_valid_url():
    assert is_valid_url("https://github.com/ColinSherman96")


def test_invalid_url():
    assert not is_valid_url("this-is-not-a-url")


def test_generate_qr_code(tmp_path):
    output_file = tmp_path / "test_qr.png"

    generate_qr_code(
        "https://github.com/ColinSherman96",
        output_file
    )

    assert output_file.exists()

def test_generate_qr_code_invalid_url(tmp_path):
    output_file = tmp_path / "bad_qr.png"

    generate_qr_code(
        "not-a-url",
        output_file
    )

    assert not output_file.exists()

def test_create_directory(tmp_path):
    new_directory = tmp_path / "qr_codes"

    create_directory(new_directory)

    assert new_directory.exists()
    assert new_directory.is_dir()
