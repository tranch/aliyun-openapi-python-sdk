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
from aliyunsdkfnf.endpoint import endpoint_data

class ReportTaskFailedRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'fnf', '2019-03-15', 'ReportTaskFailed','fnf')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Cause(self): # String
		return self.get_body_params().get('Cause')

	def set_Cause(self, Cause):  # String
		self.add_body_params('Cause', Cause)
	def get_Error(self): # String
		return self.get_body_params().get('Error')

	def set_Error(self, Error):  # String
		self.add_body_params('Error', Error)
	def get_RequestId(self): # String
		return self.get_query_params().get('RequestId')

	def set_RequestId(self, RequestId):  # String
		self.add_query_param('RequestId', RequestId)
	def get_TaskToken(self): # String
		return self.get_query_params().get('TaskToken')

	def set_TaskToken(self, TaskToken):  # String
		self.add_query_param('TaskToken', TaskToken)
