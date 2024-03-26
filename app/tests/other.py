test_openapi_scheme = {'openapi': '3.1.0', 'info': {'title': 'FastAPI', 'version': '0.1.0'}, 'paths': {
    '/api/v1/deposit/': {'post': {'tags': ['deposit'], 'summary': 'Calculate Deposit',
                                  'operationId': 'calculate_deposit_api_v1_deposit__post', 'requestBody': {
            'content': {'application/json': {'schema': {'$ref': '#/components/schemas/EntryVector'}}},
            'required': True}, 'responses': {'200': {'description': 'Successful Response', 'content': {
            'application/json': {'schema': {'additionalProperties': {'type': 'number'}, 'type': 'object',
                                            'title': 'Response Calculate Deposit Api V1 Deposit  Post'}}}},
                                             '400': {'description': 'Validation Error', 'content': {
                                                 'application/json': {
                                                     'schema': {'$ref': '#/components/schemas/ErrorResponse'}}}}}}}},
                       'components': {'schemas': {'EntryVector': {'properties': {
                           'date': {'type': 'string', 'format': 'date', 'title': 'Date', 'examples': ['31.01.2021']},
                           'periods': {'type': 'integer', 'exclusiveMaximum': 61.0, 'exclusiveMinimum': 0.0,
                                       'title': 'Periods', 'examples': [3]},
                           'amount': {'type': 'integer', 'exclusiveMaximum': 3000001.0, 'exclusiveMinimum': 9999.0,
                                      'title': 'Amount', 'examples': [10000]},
                           'rate': {'type': 'integer', 'exclusiveMaximum': 9.0, 'exclusiveMinimum': 0.0,
                                    'title': 'Rate', 'examples': [6]}}, 'type': 'object',
                                                                  'required': ['date', 'periods', 'amount', 'rate'],
                                                                  'title': 'EntryVector'}, 'Error': {
                           'properties': {'message': {'type': 'string', 'title': 'Message'},
                                          'type': {'type': 'string', 'title': 'Type'}}, 'type': 'object',
                           'required': ['message', 'type'], 'title': 'Error'}, 'ErrorResponse': {'properties': {
                           'detail': {'items': {'$ref': '#/components/schemas/Error'}, 'type': 'array',
                                      'title': 'Detail'}}, 'type': 'object', 'required': ['detail'],
                                                                                                 'title': 'ErrorResponse'},
                                                  'HTTPValidationError': {'properties': {'detail': {
                                                      'items': {'$ref': '#/components/schemas/ValidationError'},
                                                      'type': 'array', 'title': 'Detail'}}, 'type': 'object',
                                                                          'title': 'HTTPValidationError'},
                                                  'ValidationError': {'properties': {'loc': {
                                                      'items': {'anyOf': [{'type': 'string'}, {'type': 'integer'}]},
                                                      'type': 'array', 'title': 'Location'}, 'msg': {'type': 'string',
                                                                                                     'title': 'Message'},
                                                                                     'type': {'type': 'string',
                                                                                              'title': 'Error Type'}},
                                                                      'type': 'object',
                                                                      'required': ['loc', 'msg', 'type'],
                                                                      'title': 'ValidationError'}}}}
