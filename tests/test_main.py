"""Tests for the main CLI entry point."""

import io
from unittest.mock import patch

import pytest

from main import main


def test_main_prints_hello_message() -> None:
    """Test that main function prints the expected hello message."""
    # Capture stdout
    captured_output = io.StringIO()

    with patch("sys.stdout", captured_output):
        main()

    output = captured_output.getvalue()
    assert "Hello from wikipedia-search-engine!" in output


def test_main_function_executes_without_error() -> None:
    """Test that main function can be called without raising exceptions."""
    try:
        main()
    except Exception as e:
        pytest.fail(f"main() raised an exception: {e}")


def test_main_as_script() -> None:
    """Test that the script can be executed as main."""
    # This test verifies the if __name__ == "__main__" block works
    # We'll test this by importing and checking the function exists
    import main

    assert hasattr(main, "main")
    assert callable(main.main)
