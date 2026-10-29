"""Checks the documentation site builds and lists every vocabulary."""

import subprocess
from pathlib import Path

import pytest
from build_vocabularies import source_files

ROOT = Path(__file__).resolve().parent.parent
SOURCES = source_files()


@pytest.fixture(scope="module")
def site(tmp_path_factory):
    output = tmp_path_factory.mktemp("site")
    build = subprocess.run(
        ["sphinx-skos", "build", "-W", "-o", str(output)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    return build, output


class TestSite:
    def test_builds_without_warnings(self, site):
        build, output = site
        assert build.returncode == 0, build.stderr

    @pytest.mark.parametrize("source", SOURCES, ids=[path.stem for path in SOURCES])
    def test_vocabularies_page_links_to_the_vocabulary(self, site, source):
        build, output = site
        index = (output / "vocabularies" / "index.html").read_text(encoding="utf-8")
        assert f'href="{source.stem}/"' in index
