from project import extract_ip, count_attempts, sort_attempts, count_targeted_users

def test_extract_ip():
    assert extract_ip("Failed password for root from 10.0.0.7 port 22 ssh2") == "10.0.0.7"
    assert extract_ip("Failed password for root from port 22 ssh2") is None

def test_count_attempts():
    lines = [
        "Failed password for root from 10.0.0.7 port 22 ssh2",
        "Failed password for root from 10.0.0.7 port 22 ssh2",
        "Accepted password for kaldrosh from 192.168.1.50 port 22 ssh2",
    ]
    lines_second = []
    assert count_attempts(lines) == {"10.0.0.7": 2}
    assert count_attempts(lines_second) == {}

def test_sort_attempts():
    assert sort_attempts({"a": 1, "b": 3}) == [("b", 3), ("a", 1)]
    assert sort_attempts({}) == []

def test_count_targeted_users():
    lines = [
            "Failed password for root from 10.0.0.7 port 22 ssh2",
            "Failed password for root from 10.0.0.7 port 22 ssh2",
            "Accepted password for kaldrosh from 192.168.1.50 port 22 ssh2",
        ]
    lines_second = []
    lines_third = [
            "Failed password for root from 10.0.0.7 port 22 ssh2",
            "Failed password for root from 10.0.0.7 port 22 ssh2",
            "Accepted password for kaldrosh from 192.168.1.50 port 22 ssh2",
            "Failed password for invalid user admin from 172.16.5.9 port 22 ssh2",
        ]
    assert count_targeted_users(lines) == {"root": 2}
    assert count_targeted_users(lines_second) == {}
    assert count_targeted_users(lines_third) == {"root": 2, "admin": 1}
