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

class UpdateK8sApplicationBaseInfoRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'UpdateK8sApplicationBaseInfo','Edas')
		self.set_uri_pattern('/pop/v5/oam/update_app_basic_info')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Owner(self): # string
		return self.get_query_params().get('Owner')

	def set_Owner(self, Owner):  # string
		self.add_query_param('Owner', Owner)
	def get_AppId(self): # string
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # string
		self.add_query_param('AppId', AppId)
	def get_PhoneNumber(self): # string
		return self.get_query_params().get('PhoneNumber')

	def set_PhoneNumber(self, PhoneNumber):  # string
		self.add_query_param('PhoneNumber', PhoneNumber)
	def get_Description(self): # string
		return self.get_query_params().get('Description')

	def set_Description(self, Description):  # string
		self.add_query_param('Description', Description)
	def get_Email(self): # string
		return self.get_query_params().get('Email')

	def set_Email(self, Email):  # string
		self.add_query_param('Email', Email)
