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

class QuerySlsLogStoreListRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'QuerySlsLogStoreList','Edas')
		self.set_uri_pattern('/pop/v5/k8s/sls/query_sls_log_store_list')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AppId(self): # string
		return self.get_query_params().get('AppId')

	def set_AppId(self, AppId):  # string
		self.add_query_param('AppId', AppId)
	def get_PageSize(self): # integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # integer
		self.add_query_param('PageSize', PageSize)
	def get_CurrentPage(self): # integer
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self, CurrentPage):  # integer
		self.add_query_param('CurrentPage', CurrentPage)
	def get_Type(self): # string
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # string
		self.add_query_param('Type', Type)
