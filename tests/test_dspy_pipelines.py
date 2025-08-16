from core.dspy_pipelines import extract_rules


def test_extract_rules():
    text = (
        "Employers must provide a contract. "
        "Overtime may not exceed two hours. "
        "Snacks are available."
    )
    rules = extract_rules(text)
    assert rules == [
        "Employers must provide a contract.",
        "Overtime may not exceed two hours.",
    ]
