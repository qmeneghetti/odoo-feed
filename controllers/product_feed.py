import logging

_logger = logging.getLogger(__name__)

class ProductFeedController(http.Controller):

    @http.route('/feed/products.xml', type='http', auth='public', website=True)
    def product_feed(self):
        # Crear estructura XML
        root = ET.Element("products")

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
            
            # Agregar el campo google_category al XML
            if product.google_category:
                _logger.info(f"Google Category for product {product.id}: {product.google_category}")
                ET.SubElement(product_el, "google_category").text = product.google_category
            else:
                _logger.info(f"Google Category is empty for product {product.id}")
                ET.SubElement(product_el, "google_category").text = "Default Category"  # Puedes poner una categoría predeterminada si no tiene asignada ninguna

        # Convertir a XML
        xml_data = ET.tostring(root, encoding="utf-8")

        # Devolver la respuesta con el XML
        return request.make_response(xml_data, headers=[('Content-Type', 'application/xml')])