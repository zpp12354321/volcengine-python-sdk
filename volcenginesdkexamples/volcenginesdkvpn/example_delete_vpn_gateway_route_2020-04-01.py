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
    delete_vpn_gateway_route_request = volcenginesdkvpn.DeleteVpnGatewayRouteRequest(
        vpn_gateway_route_id="vgr-7qthudw0ll6jmc****",
    )

    try:
        resp = api_instance.delete_vpn_gateway_route(delete_vpn_gateway_route_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)