# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkdirectconnect
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
    api_instance = volcenginesdkdirectconnect.DIRECTCONNECTApi()
    create_direct_connect_gateway_request = volcenginesdkdirectconnect.CreateDirectConnectGatewayRequest(
        description="test",
        direct_connect_gateway_name="test",
    )

    try:
        resp = api_instance.create_direct_connect_gateway(create_direct_connect_gateway_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
