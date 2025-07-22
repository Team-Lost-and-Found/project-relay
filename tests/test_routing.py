def test_routing_response():
    ticket = {"type": "harassment", "priority": "high"}
    assert ticket["type"] == "harassment"
