import pytest

from .models import User
from flasksaml2idp.views import IdPHandlerViewMixin
from flasksaml2idp.processors import BaseProcessor


class CustomProcessor(BaseProcessor):
    pass


class TestIdPHandlerViewMixin:
    def test_get_identity_provides_extra_config(self, app):
        IdPHandlerViewMixin()

    def test_get_processor_errors_if_processor_cannot_be_loaded(self):
        sp_config = {
            'processor': 'this.does.not.exist'
        }

        with pytest.raises(Exception):
            IdPHandlerViewMixin().get_processor('entity_id', sp_config)

    def test_get_processor_defaults_to_base_processor(self, app):
        sp_config = {
        }

        assert isinstance(IdPHandlerViewMixin().get_processor('entity_id', sp_config), BaseProcessor)

    def test_get_processor_loads_custom_processor(self, app):
        sp_config = {
            'processor': 'tests.test_views.CustomProcessor'
        }

        assert isinstance(IdPHandlerViewMixin().get_processor('entity_id', sp_config), CustomProcessor)


class TestIdpInitiatedFlow:
    pass


class TestMetadata:
    pass


class LoginFlow:
    def test_requires_authentication(self):
        """test redriect to settings.LOGIN_VIEW"""
        pass
