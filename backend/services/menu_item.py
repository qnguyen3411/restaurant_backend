from dto_models.menu_item import MenuItem as MenuItemDTO
from dbo_models.menu_item import MenuItem as MenuItemDBO
from services._base import BaseService
from converters.menu_item import menu_item_dbo_to_dto, menu_item_dto_to_dbo
from utils.exceptions import *
from uuid import UUID
from typing import List
import logging

logger = logging.getLogger(__name__)

class MenuItemService(BaseService):
    def __init__(self) -> None:
        super().__init__()

    def _is_recipe_id_exist(self, id: UUID) -> bool:
        return self.session.query(MenuItemDBO).filter_by(id=id).first()

    def _is_recipe_name_exist(self, name: str) -> bool:
        return self.session.query(MenuItemDBO).filter_by(name=name).first()

    def get_all_menu_items(self) -> List[MenuItemDTO]:
        base_query = self.session.query(MenuItemDBO)

        # sort by creation_time
        dbos = base_query.order_by( MenuItemDBO.created_time)

        dtos = [menu_item_dbo_to_dto(dbo) for dbo in dbos]
        return dtos

    def get_by_id(self, recipe_id: UUID) -> MenuItemDTO:
        dbo = self._is_recipe_id_exist(recipe_id)
        if not dbo:
            raise ObjectNotFound("Recipe id '{}' not found".format(recipe_id))

        return menu_item_dbo_to_dto(dbo)

    def create(self, dto: MenuItemDTO) -> MenuItemDTO:
        dbo = menu_item_dto_to_dbo(dto)
        if self._is_recipe_name_exist(dto.name):
            raise ObjectAlreadyExists("Recipe '{}' already exist".format(dbo.name))

        self.session.add(dbo)
        self.session.commit()
        return menu_item_dto_to_dbo(dbo)
