from app import app


def test_hello_route():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200
    assert b"welcome to website deployed using a CI/CD pipeline." in response.data


def test_health_route():
    tester = app.test_client()
    response = tester.get("/health")
    assert response.status_code == 200
    assert b"OK" in response.data


def test_not_found_route():
    tester = app.test_client()
    response = tester.get("/nonexistent")
    assert response.status_code == 404


def test_method_not_allowed():
    tester = app.test_client()
    response = tester.post("/health")
    assert response.status_code == 405


def test_home_content_type():
    tester = app.test_client()
    response = tester.get("/")
    assert response.content_type == "text/html; charset=utf-8"
