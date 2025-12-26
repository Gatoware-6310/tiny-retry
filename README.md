# tiny-retry

`tiny-retry` is a tiny package for retrying (synchronous) Python functions when they raise predictable exceptions. It keeps things focused on the common use-case of running a function, catching the error, waiting briefly, and retrying without needing a full decorator or external dependency.

## Installation

```bash
pip install tiny-retry
```

## Usage

```python
from tiny_retry import retry

def foo():
    # Replace this stub with something that can raise the exception(s) you want to retry.
    ...

# This will try foo() 6 times, with a delay of 3.1 seconds between retries, and it will only retry when ConnectionError is raised.
result = retry(foo, tries=6, delay=3.10, exceptions=(ConnectionError,))
```

### Parameters

- `func`: callable to invoke.
- `tries`: how many times to attempt the call (must be >= 1).
- `delay`: seconds to sleep between retries.
- `exceptions`: tuple of exception classes that should trigger another attempt.
- `*args`, `**kwargs`: optional positional and keyword arguments forwarded to `func`.

If all attempts fail, `retry` reraises the last exception so the caller can handle or log it.

## Development

Run the simple smoke test from the repo root:

```bash
python -m pytest
```

## License

Apache 2.0 © Gatoware