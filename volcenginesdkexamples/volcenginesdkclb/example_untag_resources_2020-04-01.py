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
    untag_resources_request = volcenginesdkclb.UntagResourcesRequest(
        resource_ids=["clb-273sdsdsxxxxxp8u2j****", "clb-2fe6fszjgeznk5oxruv0u****"],
        resource_type="CLB",
        tag_keys=["k1", "k2"],
    )

    try:
        resp = api_instance.untag_resources(untag_resources_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)