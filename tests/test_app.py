
def test_app_is_create(app):
    assert app.name == 'delivery.app'

def test_config_debug_is_false(config):
    assert config["DEBUG"] is False

def test_request_returns_404(client):
    assert client.get("/url_que_nao_existe").status_code == 404