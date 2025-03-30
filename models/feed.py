from odoo import models, fields, api

class FeedSettings(models.Model):
    _name = 'feed.settings'
    _description = 'Configuración del Feed de Productos'
    
    name = fields.Char(string='Nombre', default="Configuración Global")
    shipping_cost = fields.Float(string="Costo de Envío", default=0.0)
    currency = fields.Many2one('res.currency', string='Moneda')
    default_category = fields.Char(string="Categoría Predeterminada de Producto")
    
    @api.model
    def get_config(self):
        """Obtiene la configuración única o la crea si no existe"""
        config = self.search([], limit=1)
        if not config:
            config = self.create({
                'name': 'Configuración Global',
                'shipping_cost': 5.0,
                'default_category': 'General'
            })
        return config
    
    # Override para que siempre abra el primer registro
    @api.model
    def get_empty_list_help(self, help):
        config = self.search([], limit=1)
        if not config:
            config = self.create({
                'name': 'Configuración Global',
                'shipping_cost': 5.0,
                'default_category': 'General'
            })
        return super(FeedSettings, self).get_empty_list_help(help)