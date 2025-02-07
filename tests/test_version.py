"""Test version information."""

from metagent import __version__


def test_version():
    """Test version is a string."""
    assert isinstance(__version__, str)
    assert __version__ == "0.1.0"
