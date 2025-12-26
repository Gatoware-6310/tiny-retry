from tiny_retry import retry

def print_hello():
    print('Hello, world!')

if __name__ == "__main__":
    retry(print_hello)