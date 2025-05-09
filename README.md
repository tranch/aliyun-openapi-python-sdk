# Alibaba Cloud Python Software Development Kit

[![PyPI version](https://badge.fury.io/py/aliyun-python-sdk-core.svg)](https://badge.fury.io/py/aliyun-python-sdk-core)
[![Python test](https://github.com/aliyun/aliyun-openapi-python-sdk/actions/workflows/test.yml/badge.svg)](https://github.com/aliyun/aliyun-openapi-python-sdk/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/aliyun/aliyun-openapi-python-sdk/graph/badge.svg?token=qmWxah6dPs)](https://codecov.io/gh/aliyun/aliyun-openapi-python-sdk)
[![python](https://img.shields.io/pypi/pyversions/aliyun-python-sdk-core.svg)](https://img.shields.io/pypi/pyversions/aliyun-python-sdk-core.svg)

[中文文档](./README_zh.md)

The Alibaba Cloud V1.0 SDK will soon enter the Basic Security Maintenance phase and is no longer recommended for use. It is suggested to use the V2.0 SDK instead.

## Troubleshoot

[Troubleshoot](https://api.alibabacloud.com/troubleshoot?source=github_sdk) Provide OpenAPI diagnosis service to help developers locate quickly and provide solutions for developers through `RequestID` or `error message`.

## Online Demo

**[API Developer Portal](https://api.alibabacloud.com)** provides the ability to call the cloud product OpenAPI online, and dynamically generate SDK Example code and quick retrieval interface, which can significantly reduce the difficulty of using the cloud API. **It is highly recommended**.

<a href="https://api.alibabacloud.com" target="api_explorer">
  <img src="https://img.alicdn.com/tfs/TB12GX6zW6qK1RjSZFmXXX0PFXa-744-122.png" width="180" />
</a>

## Important Updates

- Starting from version 2.16.0, the Alibaba Cloud Python SDK core library `aliyun-python-sdk-core` only supports Python 3.7 and above.

## Documentation

- [Requirements](docs/0-Requirement-EN.md)
- [Installation](./docs/1-Installation-EN.md)
- [Client & Credentials](./docs/2-Client-EN.md)
- [Timeout](./docs/3-Timeout-EN.md)
- [Proxy Configurations](./docs/4-Proxy-EN.md)
- [Log](./docs/5-Log-EN.md)
- [Endpoint](./docs/6-Endpoint-EN.md)
- [Https](./docs/7-Https-EN.md)
- [Debug](./docs/8-Debug-EN.md)
- [Exception](./docs/9-Exception-EN.md)

## Prerequisites

- To use Alibaba Cloud Python SDK, you must have an Alibaba Cloud account as well as an AccessKey.

	The AccessKey is required when initializing `AcsClient`. You can create an AccessKey in the Alibaba Cloud console. For more information, see [Create an AccessKey](https://usercenter.console.aliyun.com/?spm=5176.doc52740.2.3.QKZk8w#/manage/ak).

	> **Note:** To increase the security of your account, we recommend that you use the AccessKey of the RAM user to access Alibaba Cloud services.

- To use Alibaba Cloud Python SDK to access the APIs of a product, you must first activate the product on the [Alibaba Cloud console](https://home.console.aliyun.com/?spm=5176.doc52740.2.4.QKZk8w) if required.

- Alibaba Cloud Python SDK requires Python 3.7.x and above.

## Install Python SDK

Alibaba Cloud Python SDK supports Python 3.7.x and above. Run ``python --version`` to check your version of Python.

You can install the Alibaba Cloud Python SDK using the following two methods. Regardless of which method and cloud service are used, the core library `aliyun-python-sdk-core` must be installed.

- **Install with pip**

	Python SDK uses a common package management tool named `pip`. If pip is not installed, see the [pip user guide](https://pip.pypa.io/en/stable/installing/?spm=5176.doc53090.2.7.zHDiNV "pip User Guide") to install pip.

	Run the following command to install the individual libraries of Alibaba Cloud services:

	```bash
	# Install the core library
	pip install aliyun-python-sdk-core
	# Install the ECS management library
	pip install aliyun-python-sdk-ecs
	# Install the RDS management library
	pip install aliyun-python-sdk-rds
	```

## Use Python SDK

1. Import the required modules as follows:

    ```python
    from aliyunsdkcore.client import AcsClient
    from aliyunsdkcore.acs_exception.exceptions import ClientException
    from aliyunsdkcore.acs_exception.exceptions import ServerException
    from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
    from aliyunsdkecs.request.v20140526 import StopInstanceRequest
    ```
2. Initialize the `AcsClient` instance:

    ```python
    client = AcsClient(
        "<access-key-id>",
        "<access-key-secret>",
        "<region-id>"
    )
    ```

	where:

	- `access-key-id` is the Accesskey ID for your account.
	- `access-key-secret` is the AccessKey secret for your account.
	- `region-id` is the ID of the region where the service is called. For a list of region IDs, see [Regions and zones](https://www.alibabacloud.com/help/doc-detail/40654.html).

	> **Note:** The sequence of these parameters cannot be changed.

3. Initialize a request and print response.

	```python
	# Initialize a request and set parameters
	request = DescribeInstancesRequest.DescribeInstancesRequest()
	request.set_PageSize(10)
	# Print response
	response = client.do_action_with_exception(request)
	print response
	```

## Code example

The following example shows how to query a list of ECS instances in a specific region using [DescribeInstances](~~25506~~). Substitute the values for `your-access-key-id`, `your-access-key-secret`, and `your-region-id`.

```python
# -*- coding: utf8 -*-

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest

# Initialize AcsClient instance
client = AcsClient(
  "<your-access-key-id>",
  "<your-access-key-secret>",
  "<your-region-id>"
)

# Initialize a request and set parameters
request = DescribeInstancesRequest.DescribeInstancesRequest()
request.set_PageSize(10)

# Print response
response = client.do_action_with_exception(request)
print response
```

## HTTP DEBUG

To use the function `HTTP DEBUG`, you must set `DEBUG` in your environment variable, the corresponding value
may be `sdk` or `SDK`.

The following example shows what the `HTTP DEBUG` do, which will help you debug your codes.

```plaintext
> GET /databases?RegionId=cn-hangzhou HTTP/1.1
> Host : ads.cn-hangzhou.aliyuncs.com
> User-Agent : AlibabaCloud (Windows 10;AMD64) Python/3.7.1 Core/2.13.1 python-requests/2.18.1
> accept-encoding : *
> Accept : application/json
> Connection : keep-alive
> x-sdk-invoke-type : normal
> x-acs-version : 2019-01-22
> x-acs-region-id : cn-hangzhou
> Date : Thu, 21 Feb 2019 08:00:50 GMT
> x-acs-signature-method : HMAC-SHA1
> x-acs-signature-version : 1.0
> Authorization : acs ...
> x-sdk-client : python/2.0.0

< HTTP/1.1 503 SERVICE_UNAVAILABLE
< Date : Thu, 21 Feb 2019 08:00:50 GMT
< Content-Type : application/json; charset=UTF-8
< Content-Length : 297
< Connection : keep-alive
< Access-Control-Allow-Origin : *
< Access-Control-Allow-Methods : POST, GET, OPTIONS
< Access-Control-Allow-Headers : X-Requested-With, X-Sequence, _aop_secret, _aop_signature
< Access-Control-Max-Age : 172800
< x-acs-request-id : 670F3D09-F8E7-4144-83C3-B56C35DA35ED
< Server : Jetty(7.2.2.v20101205)
```
