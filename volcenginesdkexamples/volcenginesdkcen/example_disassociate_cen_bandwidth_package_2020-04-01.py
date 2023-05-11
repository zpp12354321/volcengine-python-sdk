# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkcen
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
    api_instance = volcenginesdkcen.CENApi()
    disassociate_cen_bandwidth_package_request = volcenginesdkcen.DisassociateCenBandwidthPackageRequest(
        cen_bandwidth_package_id="cbp-4c2zaavbvh5fx****",
        cen_id="cen-7qthudw0ll6jmc****",
    )

    try:
        resp = api_instance.disassociate_cen_bandwidth_package(disassociate_cen_bandwidth_package_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
