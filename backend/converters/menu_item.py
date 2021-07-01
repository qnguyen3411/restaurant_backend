from dbo_models.menu_item import MenuItem as MenuItemDBO
from dto_models.menu_item import MenuItem as MenuItemDTO

def menu_item_dbo_to_dto(dbo: MenuItemDBO) -> MenuItemDTO:
    dto = MenuItemDTO(
        category_id=dbo.category_id,
        id=dbo.id,
        name=dbo.name, 
        description=dbo.description,
        price=dbo.price, size=dbo.size,
        image_url=dbo.image_url,
        active=dbo.active,
        is_taxable=dbo.is_taxable,
        tax_rate=dbo.tax_rate
    ) # Only take DTO attribute that has init=True
    dto.updated_time = dbo.updated_time
    dto.created_time = dbo.created_time
    return dto

def menu_item_dto_to_dbo(dto: MenuItemDTO) -> MenuItemDBO:
    dbo = MenuItemDBO(
        category_id=dto.category_id,
        name=dto.name,
        description=dto.description,
        price=dto.price,
        image_url=dto.image_url,
        active=dto.active,
        is_taxable=dto.is_taxable,
        size=dto.size,
        tax_rate=dto.tax_rate,
        id=dto.id
    )
    dbo.updated_time = dto.updated_time
    dbo.created_time = dto.created_time
    return dbo