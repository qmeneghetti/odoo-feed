{
    "name": "Custom Product Feed",
    "summary": "Genera un feed XML para Google Shopping y Facebook",
    'category': 'Sales',
    "author": "Quetzal Meneghetti",
    "version": "1.1.2",
    "depends": ["base","website", "product"],
    "data": [
        "views/product_template_views.xml",  
        "views/feed_settings_views.xml",
    ],
    "installable": True,
    "application": True,
}