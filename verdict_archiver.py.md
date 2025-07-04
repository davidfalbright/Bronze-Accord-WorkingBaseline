# verdict_archiver.py

import shutil
from pathlib import Path
from datetime import datetime


class VerdictArchiver:
    """
    Archives verdict log files into timestamped subfolders for long-term storage.
    """

    def __init__(self, source_dir="verdict_logs", archive_base="verdict_archive"):
        self.source_dir = Path(source_dir)
        self.archive_base = Path(archive_base)
        self.archive_base.mkdir(parents=True, exist_ok=True)

    def archive_logs(self) -> str:
        """
        Moves all JSON verdict logs into a new timestamped archive folder.

        Returns:
            The path to the newly created archive folder.
        """
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        archive_dir = self.archive_base / f"archive_{timestamp}"
        archive_dir.mkdir(parents=True, exist_ok=True)

        for file in self.source_dir.glob("*.json"):
            shutil.move(str(file), archive_dir / file.name)

        return str(archive_dir)

    def list_archives(self):
        """
        Lists all archive directories created so far.

        Returns:
            A list of Path objects pointing to archive folders.
        """
        return sorted([p for p in self.archive_base.iterdir() if p.is_dir()])


# Example usage
if __name__ == "__main__":
    archiver = VerdictArchiver()
    archive_path = archiver.archive_logs()
    print(f"Logs archived to: {archive_path}")