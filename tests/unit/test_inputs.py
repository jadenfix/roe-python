from roe.models.file import FileUpload
from roe.utils.inputs import build_execution_multipart


def test_file_upload_path_is_read_not_left_open(tmp_path):
    path = tmp_path / "invoice.pdf"
    path.write_bytes(b"%PDF-1.4")

    _, files = build_execution_multipart({"document": FileUpload(path=str(path))})

    assert files["document"] == ("invoice.pdf", b"%PDF-1.4", "application/pdf")
