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

from aliyunsdkcore.request import RpcRequest
from aliyunsdkarms.endpoint import endpoint_data

class InstallAddonRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ARMS', '2019-08-08', 'InstallAddon','arms')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AddonVersion(self): # String
		return self.get_query_params().get('AddonVersion')

	def set_AddonVersion(self, AddonVersion):  # String
		self.add_query_param('AddonVersion', AddonVersion)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_AliyunLang(self): # String
		return self.get_query_params().get('AliyunLang')

	def set_AliyunLang(self, AliyunLang):  # String
		self.add_query_param('AliyunLang', AliyunLang)
	def get_Values(self): # String
		return self.get_query_params().get('Values')

	def set_Values(self, Values):  # String
		self.add_query_param('Values', Values)
	def get_ReleaseName(self): # String
		return self.get_query_params().get('ReleaseName')

	def set_ReleaseName(self, ReleaseName):  # String
		self.add_query_param('ReleaseName', ReleaseName)
	def get_EnvironmentId(self): # String
		return self.get_query_params().get('EnvironmentId')

	def set_EnvironmentId(self, EnvironmentId):  # String
		self.add_query_param('EnvironmentId', EnvironmentId)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
