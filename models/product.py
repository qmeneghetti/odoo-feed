from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = "product.template"

    # Puedes agregar más campos personalizados para el feed
    google_category = fields.Char("Categoría Google Shopping")