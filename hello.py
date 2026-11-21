"""A tiny test script pushed by Hark."""


def greet(name: str = "world") -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet())
