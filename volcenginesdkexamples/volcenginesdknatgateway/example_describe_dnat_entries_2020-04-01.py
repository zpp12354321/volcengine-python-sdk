# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdknatgateway
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
    api_instance = volcenginesdknatgateway.NATGATEWAYApi()
    describe_dnat_entries_request = volcenginesdknatgateway.DescribeDnatEntriesRequest(
        dnat_entry_ids=["dnat-342abc3bc3****"],
        nat_gateway_id="ngw-2feq5xhimd88w59gp686****",
    )

    try:
        resp = api_instance.describe_dnat_entries(describe_dnat_entries_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)