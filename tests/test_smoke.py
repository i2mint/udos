"""Smoke tests for the ``udos`` package.

``udos`` is currently a placeholder package (the standard it names is still
being designed), so there is no behaviour to test yet. This module exists so
that pytest collects at least one item: wads CI runs ``pytest --doctest-modules``
driven entirely by ``testpaths``, and an empty collection makes pytest exit with
code 5, which fails the build. Keeping a real (if minimal) test here means the
test step stays *enabled*, so the moment ``udos`` grows modules with doctests
they are exercised automatically.
"""


def test_package_imports():
    """The package imports cleanly and carries a module docstring."""
    import udos

    assert udos.__doc__ is not None
