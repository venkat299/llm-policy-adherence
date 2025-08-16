from core.graph_builder import build_graph


def test_build_graph_creates_edges():
    rules = ["Employers must provide contracts."]
    graph = build_graph(rules)
    assert graph.has_edge("employers", "provide contracts.")
    assert graph["employers"]["provide contracts."]["action"] == "must"
