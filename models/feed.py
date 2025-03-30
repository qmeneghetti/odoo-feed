from odoo import models, fields

class FeedSettings(models.Model):
    _name = 'feed.settings'
    _description = 'Configuración del Feed de Productos'

    name = fields.Char(string='Nombre', required=True)
    shipping_cost = fields.Float(string="Costo de Envío", default=0.0)
    currency = fields.Many2one('res.currency', string='Moneda')
    default_category = fields.Char(string="Categoría Predeterminada de Producto")