# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkclb
from pprint import pprint
from volcenginesdkcore.rest import ApiException

if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.ak = "AK"
    configuration.sk = "SK"
    configuration.region = "cn-beijing"
    # set default configuration
    volcenginesdkcore.Configuration.set_default(configuration)

    # use global default configuration
    api_instance = volcenginesdkclb.CLBApi()
    delete_load_balancer_request = volcenginesdkclb.DeleteLoadBalancerRequest(
        load_balancer_id="clb-bp1b6c719dfa08ex****",
    )

    try:
        resp = api_instance.delete_load_balancer(delete_load_balancer_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
