from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)

class StockMove(models.Model):
    _inherit = 'stock.move'

    initial_available_quantity = fields.Float(string='Available', compute='_compute_quantities', store=True)
    initial_remaining_quantity = fields.Float(string='Remaining', compute='_compute_quantities', store=True)
    current_available_quantity = fields.Float(string='Current Available Quantity', compute='_compute_quantities')
    current_remaining_quantity = fields.Float(string='Current Remaining Quantity', compute='_compute_quantities')

    @api.depends('product_id', 'product_uom_qty', 'location_id', 'picking_type_id.code', 'picking_id', 'state')
    def _compute_quantities(self):
        for move in self:
            if move.picking_type_id.code == 'internal' and move.product_id:
                available = move.product_id.with_context(location=move.location_id.id).qty_available

                # Calculate initial quantities only if they haven't been set
                if not move.initial_available_quantity:
                    move.initial_available_quantity = available
                    move.initial_remaining_quantity = max(0, available - move.product_uom_qty)

                # Calculate current quantities
                current_picking_moves = move.picking_id.move_ids.filtered(
                    lambda m: m.product_id == move.product_id and m.id and m.id != move.id
                )
                current_allocated = sum(current_picking_moves.mapped('product_uom_qty'))

                move.current_available_quantity = max(0, available - current_allocated)
                move.current_remaining_quantity = max(0, move.current_available_quantity - move.product_uom_qty)
            else:
                move.initial_available_quantity = 0
                move.initial_remaining_quantity = 0
                move.current_available_quantity = 0
                move.current_remaining_quantity = 0

            _logger.info(f"Computing quantities for move {move.id or 'New'}: "
                         f"Available: {available if 'available' in locals() else 'N/A'}, "
                         f"Initial Available: {move.initial_available_quantity}, "
                         f"Initial Remaining: {move.initial_remaining_quantity}, "
                         f"Current Available: {move.current_available_quantity}, "
                         f"Current Remaining: {move.current_remaining_quantity}")

    def write(self, vals):
        res = super(StockMove, self).write(vals)
        if any(field in vals for field in ['product_id', 'product_uom_qty', 'location_id', 'picking_id']):
            self._compute_quantities()
        return res

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.onchange('move_ids', 'move_ids.product_id', 'move_ids.product_uom_qty')
    def _onchange_move_ids(self):
        for move in self.move_ids:
            move._compute_quantities()