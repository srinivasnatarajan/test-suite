import pytest

from test_suite.src.modules.api.login import Login

@pytest.mark.api
class Test_Request_Res:

    @pytest.mark.parametrize('description', ['[ INTERNAL API ] Create product api call as admin'])
    def test_internal_api_product_create_as_admin(self, description: str) -> None:
        response = Login.get_users(2)
        assert response['status_code'] == 200
        data = response['response_body']
        assert data['page'] == 2
        assert 'data' in data