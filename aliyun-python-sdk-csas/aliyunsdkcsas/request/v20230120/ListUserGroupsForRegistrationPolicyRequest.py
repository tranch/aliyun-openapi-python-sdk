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

class ListUserGroupsForRegistrationPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'csas', '2023-01-20', 'ListUserGroupsForRegistrationPolicy')
		self.set_method('GET')

	def get_PolicyIds(self): # Array
		return self.get_query_params().get('PolicyIds')

	def set_PolicyIds(self, PolicyIds):  # Array
		for index1, value1 in enumerate(PolicyIds):
			self.add_query_param('PolicyIds.' + str(index1 + 1), value1)
