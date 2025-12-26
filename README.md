# tiny-retry v0.2.0

`tiny-retry` is a tiny package for retrying (synchronous) Python functions when they raise exceptions, designed to keep things light and simple.

## Installation

```bash
pip install tiny-retry
```

## Usage

```python
from tiny_retry import retry, retry_infinite

def foo():
    # Replace this stub with something that can raise the exception(s) you want to retry.
    ...

# This will try foo() 6 times, with a delay of 3.1 seconds between retries, and it will only retry when ConnectionError is raised.
result = retry(foo, tries=6, delay=3.10, exceptions=(ConnectionError,))

# This will try foo() infinitely, with a delay of 3.1 seconds between retries, and it will only retry when ConnectionError is raised.
result = retry_infinite(foo, delay=3.10, exceptions=(ConnectionError,))
```

### Parameters

- `func`: function to call.
- `tries`: how many times to attempt the function (must be >= 1).
- `delay`: delay in seconds between retries.
- `exceptions`: a tuple of exceptions that should trigger another attempt.
- `*args`, `**kwargs`: optional positional and keyword arguments to be passed into `func`.

If all attempts fail, `retry` reraises the last exception so the caller can handle or log it.

## Notes
- retry_infinite does *not* take `tries` as a parameter.

## Development

Run the simple tests from the repo root:

```bash
python -m pytest
```

## License

Apache 2.0 © Gatoware





<small><sub>6310</sub></small>