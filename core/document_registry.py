import sqlite3
from pathlib import Path
from models.document_file_type import DocumentFileType

class DocumentRegistry:

    def __init__(self, db_path: str | Path):
        self.db_path = Path(db_path)
        self._initialize_database()

    def _connect(self):
        return sqlite3.connect(self.db_path)

    def _initialize_database(self):
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        with self._connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS documents (
                    doc_id TEXT PRIMARY KEY,
                    file_name TEXT NOT NULL,
                    file_path TEXT NOT NULL,
                    file_type TEXT NOT NULL,
                    UNIQUE(file_name, file_path)
                )
                """
            )
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS document_sequences (
                    sequence_name TEXT PRIMARY KEY,
                    current_value INTEGER NOT NULL
                )
                """
            )
            connection.execute(
                """
                INSERT OR IGNORE INTO document_sequences (
                    sequence_name,
                    current_value
                )
                VALUES ('document', -1)
                """
            )
            connection.commit()

    def get_or_create(
        self,
        file_name: str,
        file_path: str | Path,
        file_type: DocumentFileType,
    ) -> str:
        file_path = str(file_path)
        with self._connect() as connection:
            existing = connection.execute(
                """
                SELECT doc_id
                FROM documents
                WHERE file_name = ? AND file_path = ?
                """,
                (file_name, file_path),
            ).fetchone()
            if existing is not None:
                return existing[0]
            cursor = connection.execute(
                """
                UPDATE document_sequences
                SET current_value = current_value + 1
                WHERE sequence_name = 'document'
                """
            )
            if cursor.rowcount != 1:
                raise RuntimeError(
                    "Document sequence could not be updated."
                )
            current_value = connection.execute(
                """
                SELECT current_value
                FROM document_sequences
                WHERE sequence_name = 'document'
                """
            ).fetchone()[0]
            if current_value > 999999:
                raise ValueError(
                    "Document ID limit reached. "
                    "Maximum supported document ID is doc_999999."
                )
            doc_id = f"doc_{current_value:06d}"
            connection.execute(
                """
                INSERT INTO documents (
                    doc_id,
                    file_name,
                    file_path,
                    file_type
                )
                VALUES (?, ?, ?, ?)
                """,
                (
                    doc_id,
                    file_name,
                    file_path,
                    file_type.value,
                ),
            )
            connection.commit()
            return doc_id