"""Checks the documentation site in ``docs/`` builds and lists every vocabulary."""

from pathlib import Path

import pytest
from build_vocabularies import source_files
from sphinx.cmd.build import build_main

DOCS = Path(__file__).resolve().parent.parent / "docs"
SOURCES = source_files()


@pytest.fixture(scope="module")
def site(tmp_path_factory):
    output = tmp_path_factory.mktemp("site")
    status = build_main(["-W", "-q", "-b", "dirhtml", str(DOCS), str(output)])
    return status, output


class TestSite:
    def test_builds_without_warnings(self, site):
        status, output = site
        assert status == 0

    @pytest.mark.parametrize("source", SOURCES, ids=[path.stem for path in SOURCES])
    def test_front_page_links_to_the_vocabulary(self, site, source):
        status, output = site
        front_page = (output / "index.html").read_text(encoding="utf-8")
        assert f'href="{source.stem}/"' in front_page
