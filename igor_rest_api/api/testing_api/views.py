from flask.ext.restful import Resource
from flask import request , jsonify

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

    def post(self):
        json = request.json
        print json.keys()
        print json['username']
        return jsonify(json)

"""

Send post request to create outlet grouping
curl -H "Content-Type: application/json" -X POST -d '{"sid":"xyz","pduid":"xyz","outletid":[23,24]}' http://localhost:5000/testing_api/create_outlet_grouping

Send get request to view all the created groupings
curl  http://localhost:5000/testing_api/create_outlet_grouping

"""

Grouping_storage = {}

class Create_outlet_grouping(Resource):
    def get(self):
        return jsonify(Grouping_storage)

    def post(self):
        json = request.json
        try :
            temp_list = []
            print json['sid']
            if Grouping_storage.has_key(json['sid']):
                return { 'Failure ' : 'serverid already exists' }
            else :
                print json['pduid']
                temp_list.append(json['pduid'])
                print json['outletid']
                temp_list.append(json['outletid'])
                Grouping_storage[json['sid']] = temp_list
                del temp_list
                return { 'Sucess ' : json['sid'] }
        except:
            return { 'Failure ' : 'please send vaild data' }

"""

Send post request to add admin
curl -H "Content-Type: application/json" -X POST -d '{"sid":"xy","user":"8aa","pass":56}' http://localhost:5000/testing_api/add_admin_outlet

Send get request to view all admins
curl http://localhost:5000/testing_api/add_admin_outlet

"""

Admin_details_storage = {}

class Add_admin_outlet(Resource):
    def get(self):
        return Admin_details_storage

    def post(self):
        json = request.json
        try:
            print json['sid']
            print json['user']
            print json['pass']
            temp_list = []
            temp_list.append(json['user'])
            temp_list.append(json['pass'])
            if Admin_details_storage.has_key(json['sid']):
                Admin_details_storage[json['sid']].append(temp_list)
            else:
                Admin_details_storage[json['sid']] = [temp_list]
            return { 'Sucess ' : json['user'] }
        except:
            return { 'Failure ' : 'send vaild data' }
