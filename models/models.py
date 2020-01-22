# -*- coding: utf-8 -*-

# from odoo import models, fields, api
from odoo import api,_
from odoo.exceptions import ValidationError
from odoo import models


class ProductProduct(models.Model):
	_inherit = 'product.product'


	@api.model_create_multi
	def create(self,vals_list):
		products = super(ProductProduct, self.with_context(create_product_product=True)).create(vals_list)
		matching_products = self.env['product.product'].search([('name','=',products.name)])
		if len(matching_products)>1:
			raise ValidationError(_('Product name must be unique!'))

class ProductTemplate(models.Model):
	_inherit = 'product.template'

	def write(self,vals):
		res = super(ProductTemplate, self).write(vals)
		matching_products = self.env['product.product'].search([('name','=',vals['name'])])
		print(matching_products)
		if len(matching_products) > 1:
			raise ValidationError(_('Product name must be unique!'))


