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
import json

class CreateRulesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'AmpTest', '2020-12-30', 'CreateRules','AmpTest')
		self.set_method('POST')

	def get_Home(self): # Struct
		return self.get_query_params().get('Home')

	def set_Home(self, Home):  # Struct
		self.add_query_param("Home", json.dumps(Home))