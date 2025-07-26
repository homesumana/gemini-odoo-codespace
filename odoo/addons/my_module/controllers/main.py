from odoo import http
from odoo.http import request, Response
import json

class MyModuleController(http.Controller):
    @http.route('/api/my_module', type='http', auth='public', methods=['GET'], csrf=False)
    def get_all_data(self, **kw):
        records = request.env['my_module.my_module'].search([])
        data = []
        for record in records:
            data.append({
                'id': record.id,
                'name': record.name,
                'description': record.description,
            })
        return Response(json.dumps(data), content_type='application/json', status=200)

    @http.route('/api/my_module/<int:record_id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_data(self, record_id, **kw):
        record = request.env['my_module.my_module'].browse(record_id).exists()
        if not record:
            return Response(json.dumps({'error': 'Record not found'}), content_type='application/json', status=404)
        
        data = {
            'id': record.id,
            'name': record.name,
            'description': record.description,
        }
        return Response(json.dumps(data), content_type='application/json', status=200)

    @http.route('/api/my_module', type='http', auth='public', methods=['POST'], csrf=False)
    def post_data(self, **kw):
        try:
            data = json.loads(request.httprequest.data)
        except json.JSONDecodeError:
            return Response(json.dumps({'error': 'Invalid JSON'}), content_type='application/json', status=400)
        
        try:
            new_record = request.env['my_module.my_module'].create(data)
            return Response(json.dumps({'status': 'success', 'id': new_record.id}), content_type='application/json', status=201)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json', status=400)