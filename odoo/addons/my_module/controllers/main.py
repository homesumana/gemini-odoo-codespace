from odoo import http
from odoo.http import request, Response
import json

class MyModuleController(http.Controller):
    @http.route('/api/my_module', type='http', auth='public', methods=['GET'], csrf=False)
    def get_data(self, **kw):
        data = {'message': 'Hello, world!'}
        return Response(json.dumps(data), content_type='application/json', status=200)
