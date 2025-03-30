{
    "name": "Custom Product Feed",
    "summary": "Genera un feed XML para Google Shopping y Facebook",
    'category': 'Sales',
    "author": "Quetzal Meneghetti",
    "version": "1.1.12",
    "depends": ["base","website", "product"],
    "data": [
        "security/ir.model.access.csv",
        "data/feed_data.xml",
        "views/product_template_views.xml",  
        "views/feed_views.xml",
        "views/feed_menu.xml",
    ],
    "installable": True,
    "application": True,
}