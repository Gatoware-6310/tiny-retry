import pytest
from tiny_retry import retry


def test_retry_succeeds_after_failures():
    state = {"n": 0}

    def flaky():
        state["n"] += 1
        if state["n"] < 3:
            raise ValueError("fail")
        return "ok"

    result = retry(flaky, tries=5, delay=0.0, exceptions=(ValueError,))
    assert result == "ok"
    assert state["n"] == 3  # it should stop retrying once it succeeds


def test_retry_raises_after_all_tries():
    state = {"n": 0}

    def always_fails():
        state["n"] += 1
        raise RuntimeError("nope")

    with pytest.raises(RuntimeError):
        retry(always_fails, tries=4, delay=0.0, exceptions=(RuntimeError,))

    assert state["n"] == 4  # should try exactly `tries` times


def test_retry_does_not_catch_unlisted_exception():
    state = {"n": 0}

    def raises_type_error():
        state["n"] += 1
        raise TypeError("wrong type")

    # We only retry ValueError, so TypeError should immediately escape
    with pytest.raises(TypeError):
        retry(raises_type_error, tries=5, delay=0.0, exceptions=(ValueError,))

    assert state["n"] == 1  # no retries happened


def test_retry_passes_args_and_kwargs():
    def add(a, b, scale=1):
        return (a + b) * scale

    assert retry(add, 2, 3, scale=10, tries=2) == 50


def test_retry_rejects_invalid_tries():
    with pytest.raises(ValueError):
        retry(lambda: 123, tries=0)
