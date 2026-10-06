"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import bitwhisper


def test_version_is_set() -> None:
    assert bitwhisper.__version__
