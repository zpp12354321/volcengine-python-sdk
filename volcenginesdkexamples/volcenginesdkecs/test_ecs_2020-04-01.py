from __future__ import print_function
import volcenginesdkcore
import volcenginesdkecs
from pprint import pprint
from volcenginesdkcore.rest import ApiException


if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.host = "xx-xx-xx.xx.org"
    configuration.ak = "xx"
    configuration.sk = "xx=="
    configuration.region = "xx-xx-xx"

    try:
        # create an instance of the API class
        api_instance = volcenginesdkecs.ECSApi(volcenginesdkcore.ApiClient(configuration))
        resp = api_instance.describe_instances(
            volcenginesdkecs.DescribeInstancesRequest(instance_ids=["i-ybmq2b6xiil8u206g9yv"]))

        pprint(resp)
    except ApiException as e:
        print("Exception when call ECSApi:DescribeInstances: %s\n" % e)
