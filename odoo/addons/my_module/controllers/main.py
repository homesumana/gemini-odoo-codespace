from odoo import http
from odoo.http import request, Response
import json

class MyModuleController(http.Controller):
    @http.route('/api/my_module', type='http', auth='public', methods=['GET'], csrf=False)
    def get_data(self, **kw):
        data = {'message': 'Hello, world!'}
        return Response(json.dumps(data), content_type='application/json', status=200)

    @http.route('/api/my_module', type='http', auth='public', methods=['POST'], csrf=False)
    def post_data(self, **kw):
        try:
            data = json.loads(request.httprequest.data)
        except json.JSONDecodeError:
            return Response(json.dumps({'error': 'Invalid JSON'}), content_type='application/json', status=400)
        
        return Response(json.dumps({'status': 'success', 'data_received': data}), content_type='application/json', status=200)
