import unittest
from pathlib import Path


class TestSplunkEvidenceValidation(unittest.TestCase):

    def test_required_files_exist(self):
        required_files = [
            "README.md",
            "findings.md",
            "commands_used.md",
            "notes/conclusion.md",
            "images/q1-most-brute-user.png",
            "images/q2-thor-ip.png",
            "images/q3-thor-fail-count.png"
        ]

        for file in required_files:
            self.assertTrue(
                Path(file).exists(),
                f"Missing required evidence file: {file}"
            )


    def test_splunk_findings_documented(self):
        content = ""

        for file in ["README.md", "findings.md"]:
            if Path(file).exists():
                content += Path(file).read_text().lower()

        keywords = [
            "splunk",
            "ssh",
            "failed",
            "authentication",
            "brute",
            "ip"
        ]

        for keyword in keywords:
            self.assertIn(
                keyword,
                content,
                f"Missing investigation keyword: {keyword}"
            )


    def test_images_directory_exists(self):
        self.assertTrue(
            Path("images").exists(),
            "Images evidence directory missing"
        )


if __name__ == "__main__":
    unittest.main()
