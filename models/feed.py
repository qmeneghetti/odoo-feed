from odoo import models, fields, api

class FeedSettings(models.Model):
    _name = 'feed.settings'
    _description = 'Configuración del Feed de Productos'
    
    # Esto asegura que solo haya un registro
    _rec_name = 'id'
    
    name = fields.Char(string='Nombre', default="Configuración Global")
    shipping_cost = fields.Float(string="Costo de Envío", default=0.0)
    currency = fields.Many2one('res.currency', string='Moneda')
    default_category = fields.Char(string="Categoría Predeterminada de Producto")
    
    @api.model
    def get_config(self):
        """Obtiene la configuración única o la crea si no existe"""
        config = self.search([], limit=1)
        if not config:
            config = self.create({'name': 'Configuración Global'})
        return config