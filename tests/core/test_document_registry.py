import re
from models.document_file_type import DocumentFileType
from core.document_registry import DocumentRegistry
import sqlite3

def test_register_new_document_returns_document_id(tmp_path):
    db_path = tmp_path / "document_registry.db"
    registry = DocumentRegistry(db_path)
    doc_id = registry.get_or_create(
        file_name="report.pdf",
        file_path="E:/documents",
        file_type=DocumentFileType.PDF,
    )
    assert doc_id == "doc_000000"

def test_document_id_has_required_format(tmp_path):
    db_path = tmp_path / "document_registry.db"
    registry = DocumentRegistry(db_path)
    doc_id = registry.get_or_create(
        file_name="report.pdf",
        file_path="E:/documents",
        file_type=DocumentFileType.PDF,
    )
    assert re.fullmatch(r"doc_\d{6}", doc_id)

def test_same_file_returns_same_document_id(tmp_path):
    db_path = tmp_path / "document_registry.db"
    registry = DocumentRegistry(db_path)
    first_id = registry.get_or_create(
        file_name="report.pdf",
        file_path="E:/documents",
        file_type=DocumentFileType.PDF,
    )
    second_id = registry.get_or_create(
        file_name="report.pdf",
        file_path="E:/documents",
        file_type=DocumentFileType.PDF,
    )
    assert first_id == "doc_000000"
    assert second_id == "doc_000000"

def test_different_files_receive_different_document_ids(tmp_path):
    db_path = tmp_path / "document_registry.db"
    registry = DocumentRegistry(db_path)
    first_id = registry.get_or_create(
        file_name="report.pdf",
        file_path="E:/documents",
        file_type=DocumentFileType.PDF,
    )
    second_id = registry.get_or_create(
        file_name="manual.pdf",
        file_path="E:/documents",
        file_type=DocumentFileType.PDF,
    )
    assert first_id == "doc_000000"
    assert second_id == "doc_000001"

def test_same_filename_in_different_paths_is_different_document(tmp_path):
    db_path = tmp_path / "document_registry.db"
    registry = DocumentRegistry(db_path)
    first_id = registry.get_or_create(
        file_name="report.pdf",
        file_path="E:/documents",
        file_type=DocumentFileType.PDF,
    )
    second_id = registry.get_or_create(
        file_name="report.pdf",
        file_path="E:/archive",
        file_type=DocumentFileType.PDF,
    )
    assert first_id == "doc_000000"
    assert second_id == "doc_000001"

def test_document_ids_are_generated_sequentially(tmp_path):
    db_path = tmp_path / "document_registry.db"
    registry = DocumentRegistry(db_path)
    ids = [
        registry.get_or_create(
            file_name=f"document_{index}.pdf",
            file_path="E:/documents",
            file_type=DocumentFileType.PDF,
        )
        for index in range(3)
    ]
    assert ids == [
        "doc_000000",
        "doc_000001",
        "doc_000002",
    ]

def test_file_type_does_not_change_document_identity(tmp_path):
    db_path = tmp_path / "document_registry.db"
    registry = DocumentRegistry(db_path)
    first_id = registry.get_or_create(
        file_name="report.pdf",
        file_path="E:/documents",
        file_type=DocumentFileType.PDF,
    )
    second_id = registry.get_or_create(
        file_name="report.pdf",
        file_path="E:/documents",
        file_type=DocumentFileType.PDF,
    )
    assert first_id == "doc_000000"
    assert second_id == "doc_000000"

def test_registry_creates_database_file(tmp_path):
    db_path = tmp_path / "document_registry.db"
    registry = DocumentRegistry(db_path)
    registry.get_or_create(
        file_name="report.pdf",
        file_path="E:/documents",
        file_type=DocumentFileType.PDF,
    )
    assert db_path.exists()

def test_registry_reuses_existing_database(tmp_path):
    db_path = tmp_path / "document_registry.db"
    first_registry = DocumentRegistry(db_path)
    first_id = first_registry.get_or_create(
        file_name="report.pdf",
        file_path="E:/documents",
        file_type=DocumentFileType.PDF,
    )
    second_registry = DocumentRegistry(db_path)
    second_id = second_registry.get_or_create(
        file_name="report.pdf",
        file_path="E:/documents",
        file_type=DocumentFileType.PDF,
    )
    assert first_id == "doc_000000"
    assert second_id == "doc_000000"

def test_document_record_is_stored_in_database(tmp_path):
    db_path = tmp_path / "document_registry.db"
    registry = DocumentRegistry(db_path)
    doc_id = registry.get_or_create(
        file_name="report.pdf",
        file_path="E:/documents",
        file_type=DocumentFileType.PDF,
    )
    with sqlite3.connect(db_path) as connection:
        row = connection.execute(
            """
            SELECT doc_id, file_name, file_path, file_type
            FROM documents
            WHERE doc_id = ?
            """,
            (doc_id,),
        ).fetchone()
    assert row == (
        "doc_000000",
        "report.pdf",
        "E:/documents",
        "pdf",
    )