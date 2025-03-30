from odoo import http
from odoo.http import request
import xml.etree.ElementTree as ET
from datetime import datetime

class ProductFeedController(http.Controller):

    @http.route('/feed/products.xml', type='http', auth='public', website=True)
    def product_feed(self):
        # Crear estructura XML
        root = ET.Element("products")

        # Obtener los datos globales de configuración del feed
        feed_settings = request.env['feed.settings'].sudo().get_config()
        shipping_cost = feed_settings.shipping_cost if feed_settings else 5.0  # Valor predeterminado si no hay configuraciones
        default_category = feed_settings.default_category if feed_settings else "Default Categoryx"

        # Obtener productos activos
        products = request.env['product.template'].sudo().search([('sale_ok', '=', True), ('website_published', '=', True)])

        for product in products:
            product_el = ET.SubElement(root, "product")
            
            # Agregar los campos existentes
            ET.SubElement(product_el, "id").text = str(product.id)
            ET.SubElement(product_el, "name").text = product.name
            ET.SubElement(product_el, "description").text = product.description_sale or product.name
            ET.SubElement(product_el, "price").text = str(product.list_price)
            ET.SubElement(product_el, "currency").text = product.currency_id.name
            ET.SubElement(product_el, "url").text = request.httprequest.host_url + "shop/product/" + str(product.id)
            ET.SubElement(product_el, "image").text = product.image_1920 and request.httprequest.host_url + "web/image/product.template/" + str(product.id) + "/image_1920"
            ET.SubElement(product_el, "shipping").text = f"US: {shipping_cost}"  # Usar el costo de envío configurado
            ET.SubElement(product_el, "google_product_category").text = product.google_category if product.google_category else default_category

        # Convertir a XML
        xml_data = ET.tostring(root, encoding="utf-8")

        # Devolver la respuesta con el XML
        return request.make_response(xml_data, headers=[('Content-Type', 'application/xml')])