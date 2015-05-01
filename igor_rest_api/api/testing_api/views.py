from flask.ext.restful import Resource
from flask import request

"""
    
Send a put request
curl http://localhost:5000/testing_api/testdata1  -d "data=this is a test put data" -X PUT

send a get request to get the data stored using put request
curl http://localhost:5000/testing_api/testdata1

"""

testdata_storage = {}

class Testing_views(Resource):
    def get(self, testdata):
        return {testdata: testdata_storage[testdata]}

    def put(self, testdata):
        testdata_storage[testdata] = request.form['data']
        return {testdata: testdata_storage[testdata]}

"""

Send a Get request to view all the data
curl http://localhost:5000/testing_api

"""
class Testing_views_data(Resource):
    def get(self):
        return testdata_storage
