# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkvpn
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
    api_instance = volcenginesdkvpn.VPNApi()
    describe_vpn_gateway_attributes_request = volcenginesdkvpn.DescribeVpnGatewayAttributesRequest(
        vpn_gateway_id="vgw-12bfa2du7fojk17q7y1rk****",
    )

    try:
        resp = api_instance.describe_vpn_gateway_attributes(describe_vpn_gateway_attributes_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
