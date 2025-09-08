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
