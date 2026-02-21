import tempfile
import unittest
from pathlib import Path

from project_utils import (
    ensure_project_dirs,
    make_resource_name,
    render_template,
    render_template_file,
)


class TestProjectUtils(unittest.TestCase):
    def test_ensure_project_dirs_creates_expected_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp) / "demo"
            created = ensure_project_dirs(base, ["src", "configs/dev", "pipelines"])

            self.assertEqual(len(created), 3)
            for path in created:
                self.assertTrue(path.exists())
                self.assertTrue(path.is_dir())

    def test_make_resource_name_normalizes_and_truncates(self):
        name = make_resource_name(" Sales ", "Daily@Ingest", max_length=12)
        self.assertEqual(name, "sales-daily")

    def test_render_template_replaces_tokens(self):
        content = "project={{PROJECT}}, env={{ENV}}"
        rendered = render_template(content, {"PROJECT": "sales", "ENV": "dev"})
        self.assertEqual(rendered, "project=sales, env=dev")

    def test_render_template_file_writes_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            template = tmp_path / "sample.template"
            output = tmp_path / "out" / "sample.out"

            template.write_text("hello {{NAME}}", encoding="utf-8")
            written = render_template_file(template, output, {"NAME": "world"})

            self.assertEqual(written, output)
            self.assertEqual(output.read_text(encoding="utf-8"), "hello world")


if __name__ == "__main__":
    unittest.main()
