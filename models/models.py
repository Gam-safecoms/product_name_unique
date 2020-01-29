# -*- coding: utf-8 -*-

# from odoo import models, fields, api
from odoo import api,_
from odoo.exceptions import ValidationError
from odoo import models
import logging

_logger = logging.getLogger(__name__)

class ProductProduct(models.Model):
	_inherit = 'product.product'


	@api.model_create_multi
	def create(self,vals_list):
		products = super(ProductProduct, self.with_context(create_product_product=True)).create(vals_list)
		matching_products = self.env['product.product'].search([('name','=',products.name)])
		if len(matching_products)>1:
			raise ValidationError(_('Product name must be unique!'))
		self.clear_caches()
		return products

class ProductTemplate(models.Model):
	_inherit = 'product.template'

	def write(self,vals):
		res = super(ProductTemplate, self).write(vals)
		if "name" in vals :			
			matching_products = self.env['product.product'].search([('name','=',vals['name'])])
			print(matching_products)
			if len(matching_products) > 1:
				raise ValidationError(_('Product name must be unique!'))
		if 'attribute_line_ids' in vals or vals.get('active'):
			self._create_variant_ids()
		if 'active' in vals and not vals.get('active'):
			self.with_context(active_test=False).mapped('product_variant_ids').write({'active':vals.get('active')})
		if 'image_1920' in vals:
			self.env['product.product'].invalidate_cache(fnames=[
					'image_1920',
					'image_1024',
					'image_512',
					'image_256',
					'image_128',
					'can_image_1024_be_zoomed',
				])
		return res
					

