#!/usr/bin/env python

import base64
from . import IgorApiTestCase
from flask import url_for
from endpoints import * 

class LoginTestCase(IgorApiTestCase):

    def test_root(self):
        self.assert_200(self.client.get(url_for('root')),
                        message='root must be accessible without login')

    def test_login(self):

        self.assert_401(self.client.get(url_for('login')),
                        message='login should fail without credentials')

        self.assert_401(self.client.get(url_for('login'),
                        headers=[('Authorization', 'Basic '
                                                  + base64.b64encode('toor:root'))]),
                        message='login should fail with incorrect username')

        self.assert_401(self.client.get(url_for('login'),
                        headers=[('Authorization', 'Basic '
                                                  + base64.b64encode('root:toor'))]),
                        message='login should fail with incorrect password')

        self.assert_401(self.client.get(url_for('login'),
                        headers=[('Authorization', 'Basic '
                                                  + base64.b64encode('toor:toor'))]),
                        message='login should fail with incorrect username and password')
        
        self.assert_200(self.client.get(url_for('login'),
                        headers=[('Authorization', 'Basic '
                                                  + base64.b64encode('root:root'))]),
                        message='login should pass with correct username and password')

    def test_unauthenticated_endpoints(self):
        for endpoint in all_endpoints:

            endpoint_url = url_for(endpoint,
                                   username='username',
                                   hostname='hostname',
                                   channel=0)

            self.assert_401(self.client.get(endpoint_url),
                            message=endpoint_url +
                            ' should be inaccessible without login')