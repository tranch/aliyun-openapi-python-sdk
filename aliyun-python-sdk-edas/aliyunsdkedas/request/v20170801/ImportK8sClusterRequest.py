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

class ImportK8sClusterRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'ImportK8sCluster','Edas')
		self.set_uri_pattern('/pop/v5/import_k8s_cluster')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Mode(self): # integer
		return self.get_query_params().get('Mode')

	def set_Mode(self, Mode):  # integer
		self.add_query_param('Mode', Mode)
	def get_EnableAsm(self): # boolean
		return self.get_query_params().get('EnableAsm')

	def set_EnableAsm(self, EnableAsm):  # boolean
		self.add_query_param('EnableAsm', EnableAsm)
	def get_NamespaceId(self): # string
		return self.get_query_params().get('NamespaceId')

	def set_NamespaceId(self, NamespaceId):  # string
		self.add_query_param('NamespaceId', NamespaceId)
	def get_ClusterId(self): # string
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self, ClusterId):  # string
		self.add_query_param('ClusterId', ClusterId)
