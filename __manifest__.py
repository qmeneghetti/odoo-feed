{
    "name": "Custom Product Feed",
    "summary": "Genera un feed XML para Google Shopping y Facebook",
    'category': 'Sales',
    "author": "Quetzal Meneghetti",
    "version": "1.1.6",
    "depends": ["base","website", "product"],
    "data": [
        "views/product_template_views.xml",  
        "views/feed_menu.xml",
        "views/feed_views.xml", 
    ],
    "installable": True,
    "application": True,
}