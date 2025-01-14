# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RoaRequest
from aliyunsdkedas.endpoint import endpoint_data

class UpdateSwimmingLaneGroupRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'UpdateSwimmingLaneGroup','Edas')
		self.set_uri_pattern('/pop/v5/trafficmgnt/swimming_lane_groups')
		self.set_method('PUT')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AppIds(self): # string
		return self.get_query_params().get('AppIds')

	def set_AppIds(self, AppIds):  # string
		self.add_query_param('AppIds', AppIds)
	def get_GroupId(self): # integer
		return self.get_query_params().get('GroupId')

	def set_GroupId(self, GroupId):  # integer
		self.add_query_param('GroupId', GroupId)
	def get_Name(self): # string
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # string
		self.add_query_param('Name', Name)
	def get_EntryApp(self): # string
		return self.get_query_params().get('EntryApp')

	def set_EntryApp(self, EntryApp):  # string
		self.add_query_param('EntryApp', EntryApp)
