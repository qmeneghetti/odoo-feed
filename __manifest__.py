{
    "name": "Custom Product Feed",
    "summary": "Genera un feed XML para Google Shopping y Facebook",
    'category': 'Sales',
    "author": "Quetzal Meneghetti",
    "version": "1.1.11",
    "depends": ["base","website", "product"],
    "data": [
        "security/ir.model.access.csv",  # Añadir esta línea
        "views/product_template_views.xml",  
        "views/feed_views.xml",  # Cambia el orden: primero views, luego menu
        "views/feed_menu.xml",
    ],
    "installable": True,
    "application": True,
}