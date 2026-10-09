import subprocess
import sys


def test_file_upload_import_emits_no_deprecation_warning():
    result = subprocess.run(
        [
            sys.executable,
            "-W",
            "error::DeprecationWarning",
            "-c",
            "import roe.models.file",
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
