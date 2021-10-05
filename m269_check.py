
def check(case: str, actual: object, expected: object, context: object) -> None:
    """Write a message if actual and expected are different."""
    if actual != expected:
        print(case, 'FAILED for', context, ':', actual, 'instead of', expected)
