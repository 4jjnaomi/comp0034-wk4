def test_get_regions_status_code(client):
    """
    GIVEN a Flask test client
    WHEN a request is made to /regions
    THEN the status code should be 200
    """
    response = client.get("/regions")
    assert response.status_code == 200


def test_get_regions_json(client):
    """
    GIVEN a Flask test client
    AND the database contains data of the regions
    WHEN a request is made to /regions
    THEN the response should contain json
    AND a JSON object for Tonga should be in the json
    """
    response = client.get("/regions")

    assert response.headers["Content-Type"] == "application/json"
    tonga = {'NOC': 'TGA', 'notes': '', 'region': 'Tonga'}
    assert tonga in response.json
