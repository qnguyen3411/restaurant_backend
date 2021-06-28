from uuid import UUID
from utils.schema_helper import serialize, deserialize
from functools import partial
from utils.exceptions import *
from flask import request, Response, abort
from schemas.menu_item import MenuItemSchema
from dto_models.menu_item import MenuItem as MenuItemDTO
from services.menu_item import MenuItemService
from dto_models.menu_item import MenuItem as MenuItemDBO
import logging
logger = logging.getLogger(__name__)

class MenuItemResource:
    @staticmethod
    def post() -> Response:
        try:
            json = request.get_json(force=True) #get from body
            schema = MenuItemSchema()
            validated_json = schema.load(json) #Validated data from frontend
            dto = MenuItemDTO(**validated_json) #transform to DTO OBJECT
            returned_dto = MenuItemService().create(dto)
        except ValueError as e:
            abort(400, {'message': str(e)})
            logger.debug("CategoryResource post 400 {}".format(e))
        # except ObjectAlreadyExists as e:
        #     abort(400, {'message': str(e)})
        #     logger.debug("CategoryResource post 400 {}".format(e))
        except Exception as e:
            abort(500, {'message': str(e)})
            logger.debug("CategoryResource post 500 {}".format(e))

        response_data = schema.dumps(returned_dto)
        return Response(response_data, status=200, headers={}, mimetype="application/json")

    @staticmethod
    def get_by_id(id: UUID) -> Response:
        try:
            returned_dto = MenuItemService().get_by_id(id)
        except ValueError as e:
            abort(400, {'message': str(e)})
        except Exception as e:
            abort(500, {'message': str(e)})
            logger.debug("MenuItemResource get 500 {}".format(e))

            # Dumps to UI format (json)
        schema = MenuItemSchema()
        response_data = schema.dumps(returned_dto)

        return Response(response_data, status=200, headers={}, mimetype="application/json")

    @staticmethod
    def get_all_menu_items() -> Response:
        try:
            returned_dto = MenuItemService().get_all_categories()
        except ValueError as e:
            abort(400, {'message': str(e)})
        except Exception as e:
            abort(500, {'message': str(e)})
            logger.debug("MenuItemResource get 500 {}".format(e))

            # Dumps to UI format (json)
        schema = MenuItemSchema(many=True)
        response_data = schema.dumps(returned_dto)

        return Response(response_data, status=200, headers={}, mimetype="application/json")

    @staticmethod
    def update_category(id: UUID) -> Response:
        try:
            returned_dto = MenuItemService().get_all_categories()
        except ValueError as e:
            abort(400, {'message': str(e)})
        except Exception as e:
            abort(500, {'message': str(e)})
            logger.debug("MenuItemResource get 500 {}".format(e))

            # Dumps to UI format (json)
        schema = MenuItemSchema(many=True)
        response_data = schema.dumps(returned_dto)

        return Response(response_data, status=200, headers={}, mimetype="application/json")

    @staticmethod
    def delete_category(id: UUID) -> Response:

        try:
            returned_dto = MenuItemService().get_all_categories()
        except ValueError as e:
            abort(400, {'message': str(e)})
        except Exception as e:
            abort(500, {'message': str(e)})
            logger.debug("MenuItemResource get 500 {}".format(e))

            # Dumps to UI format (json)
        schema = MenuItemSchema(many=True)
        response_data = schema.dumps(returned_dto)

        return Response(response_data, status=200, headers={}, mimetype="application/json")