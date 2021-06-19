from dto_models.category import Category as CategoryDTO
from dbo_models.category import Category as CategoryDBO
from services._base import BaseService
from converters.category import category_dbo_to_dto, category_dto_to_dbo
from utils.exceptions import *
from uuid import UUID
from typing import List
import logging

logger = logging.getLogger(__name__)


class CategoryService(BaseService):
    def __init__(self) -> None:
        super().__init__()

    def _is_category_id_exist(self, id: UUID) -> CategoryDBO:
        return self.session.query(CategoryDBO).filter_by(id=id).first()

    def _is_category_name_exist(self, name: str) -> bool:
        return self.session.query(CategoryDBO).filter_by(name=name).first()

    def create(self, dto: CategoryDTO) -> CategoryDTO:
        dbo = category_dto_to_dbo(dto)
        if self._is_category_name_exist(dto.name):
            raise ObjectAlreadyExists("Category '{}' already exist".format(dbo.name))

        self.session.add(dbo)
        self.session.commit()
        return category_dbo_to_dto(dbo)

    def get_by_id(self, category_id: UUID) -> CategoryDTO:
        dbo = self.session.query(CategoryDBO).filter_by(id=category_id).first()
        if not dbo:
            raise ObjectNotFound("Category id '{}' not found".format(category_id))

        return category_dbo_to_dto(dbo)

    def get_all_categories(self):
        dbo_list = self.session.query(CategoryDBO).all()
        if not dbo_list:
            raise ObjectNotFound("Categories fetch failed")

        return [category_dbo_to_dto(dbo) for dbo in dbo_list]

    def update_category(self, dto: CategoryDTO) -> CategoryDTO:
        dbo = self.session.query(CategoryDBO).filter_by(id=dto.id).first()
        if not dbo:
            raise ObjectNotFound("Category id '{}' not found".format(category_id))
        dbo.name = dto.name
        dbo.index = dto.index
        self.session.commit()
        return category_dbo_to_dto(dbo)
        
    def delete_category(self, category_id: UUID) -> CategoryDTO:
        #find category by id
        dbo = self.session.query(CategoryDBO).filter_by(id=category_id).first()
        if not dbo:
            raise ObjectNotFound("Category id '{}' not found".format(category_id))
        #delete the category
        self.session.delete(dbo)
        #save the database
        self.session.commit()
        #return the deleted category
        return category_dbo_to_dto(dbo)
