# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkvpc
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
    api_instance = volcenginesdkvpc.VPCApi()
    detach_network_interface_request = volcenginesdkvpc.DetachNetworkInterfaceRequest(
        instance_id="i-wijfn35c****",
        network_interface_id="eni-bp1fgn8xyz9****",
    )

    try:
        resp = api_instance.detach_network_interface(detach_network_interface_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
