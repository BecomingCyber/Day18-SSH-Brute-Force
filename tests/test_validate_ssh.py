import unittest
from pathlib import Path


class TestSSHEvidenceValidation(unittest.TestCase):

    def test_required_files_exist(self):
        files = [
            "README.md",
            "findings.md",
            "commands_used.md"
        ]

        for file in files:
            self.assertTrue(Path(file).exists())


    def test_ssh_findings_documented(self):
        text = ""

        for file in ["README.md", "findings.md"]:
            if Path(file).exists():
                text += Path(file).read_text().lower()

        self.assertIn("ssh", text)
        self.assertIn("brute", text)


    def test_missing_file_rejected(self):
        self.assertFalse(
            Path("missing_evidence.png").exists()
        )


if __name__ == "__main__":
    unittest.main()
