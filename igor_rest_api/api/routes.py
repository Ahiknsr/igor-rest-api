#!/usr/bin/env python2

from .auth.views import LoginAPI

from .ipmi.views import (
    MachineChassisAPI, MachineChassisPowerAPI,
    MachineSensorsAPI, MachineSensorAPI,
    MachineLanAPI, MachineLanChannelAPI,
    MachineLanAlertAPI, MachineLanChannelAlertAPI,
    MachineChassisPolicyAPI, MachineSelAPI, MachineSelTimeAPI,
    MachineSelRecordsAPI,
)
from .machines.views import MachineAPI, MachinesAPI
from .machines.views.permissions import (
    UserMachineAPI, UserMachinesAPI,
    MachineUserAPI, MachineUsersAPI,
)
from .auth.views import UserAPI, UsersAPI
from .views import RootAPI
from .testing_api.views import (
        Testing_views , Testing_views_data ,
        Create_outlet_grouping , Add_admin_outlet
)

resources = [
            (RootAPI, '/', 'root'),
            (LoginAPI, '/login', 'login'),
            (UsersAPI, '/users', 'users'),
            (UserAPI, '/users/<string:username>', 'user'),
            (MachinesAPI, '/machines', 'machines'),
            (MachineAPI, '/machines/<string:hostname>', 'machine'),
            (UserMachinesAPI, '/users/<string:username>/machines',
                'user_machines'),
            (UserMachineAPI,
                '/users/<string:username>/machines/<string:hostname>',
                'user_machine'),
            (MachineUsersAPI, '/machines/<string:hostname>/users',
                'machine_users'),
            (MachineUserAPI,
                '/machines/<string:hostname>/users/<string:username>',
                'machine_user'),
            (MachineChassisAPI,
                '/machines/<string:hostname>/chassis',
                'machine_chassis'),
            (MachineChassisPolicyAPI,
                '/machines/<string:hostname>/chassis/policy',
                'machine_chassis_policy'),
            (MachineChassisPowerAPI,
                '/machines/<string:hostname>/chassis/power',
                'machine_chassis_power'),
            (MachineSensorsAPI,
                '/machines/<string:hostname>/sensors',
                'machine_sensors'),
            (MachineSensorAPI,
                '/machines/<string:hostname>/sensors/<string:sensor>',
                'machine_sensor'),
            (MachineLanAPI,
                '/machines/<string:hostname>/lan',
                'machine_lan'),
            (MachineLanChannelAPI,
                '/machines/<string:hostname>/lan/<int:channel>',
                'machine_lan_channel'),
            (MachineLanAlertAPI,
                '/machines/<string:hostname>/lan/alert',
                'machine_lan_alert'),
            (MachineLanChannelAlertAPI,
                '/machines/<string:hostname>/lan/<int:channel>/alert',
                'machine_lan_channel_alert'),
            (MachineSelAPI,
                '/machines/<string:hostname>/sel',
                'machine_sel'),
            (MachineSelTimeAPI,
                '/machines/<string:hostname>/sel/time',
                'machine_sel_time'),
            (MachineSelRecordsAPI,
                '/machines/<string:hostname>/sel/records',
                'machine_sel_records'),
            (Testing_views,'/testing_api/<string:testdata>','test'),
            (Testing_views_data,'/testing_api','testdata'),
            (Create_outlet_grouping,'/testing_api/create_outlet_grouping','outlet_grouping_create'),
            (Add_admin_outlet , '/testing_api/add_admin_outlet','outlet_grouping_add_admin')
            ]

def setup(api):
    for resourceClass, url, endpoint in resources:
        api.add_resource(resourceClass, url, endpoint=endpoint)
