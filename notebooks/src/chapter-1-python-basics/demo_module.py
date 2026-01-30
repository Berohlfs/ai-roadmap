"""
Demo module for the modules/imports notebook.
Use: import demo_module / from demo_module import ...
"""

PI = 3.14159

def greet(name: str) -> str:
    """Return a greeting string."""
    return f"Hello, {name}!"

def area_of_circle(radius: float) -> float:
    """Compute area using this module's PI."""
    return PI * radius ** 2

def main():
    """Run when this file is executed as a script."""
    print("Running demo_module as __main__")
    print(greet("World"))
    print(f"Area of circle r=2: {area_of_circle(2):.2f}")

if __name__ == "__main__":
    main()
