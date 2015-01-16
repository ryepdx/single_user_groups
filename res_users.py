# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 NovaPoint Group LLC (<http://www.novapointgroup.com>)
#    Copyright (C) 2004-2010 OpenERP SA (<http://www.openerp.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

from openerp.osv import fields, osv

class res_users(osv.osv):
    _inherit = "res.users"

    def create(self, cr, uid, vals, context=None):
        user_id = super(res_users, self).create(cr, uid, vals, context)
        category_ids = self.pool.get("ir.module.category").search(cr, uid, [('name', '=', 'Single User')])

        if category_ids:
            self.pool.get("res.groups").create(cr, uid,
                {
                    'category_id': category_ids[0],
                    'name': vals.get('login', ''),
                    'users': [(4, user_id)]
                }, context=context
            )

        return user_id

res_users()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: