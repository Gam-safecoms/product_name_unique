# -*- coding: utf-8 -*-

# from odoo import models, fields, api

import logging
from odoo import api,_
from odoo.exceptions import ValidationError
from odoo import models

_logger = logging.getLogger(__name__)

class ProductProduct(models.Model):
	_inherit = 'product.product'


	@api.model_create_multi
	def create(self,vals_list):
		_logger.info("in product name unique module .......")
		products = super(ProductProduct, self.with_context(create_product_product=True)).create(vals_list)
		matching_products = self.env['product.product'].search([('name','=',products.name)])
		if len(matching_products)>1:
			raise ValidationError(_('Product name must be unique!'))