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
    delete_snat_entry_request = volcenginesdknatgateway.DeleteSnatEntryRequest(
        snat_entry_id="snat-2fedi096gdiww59gp680****",
    )

    try:
        resp = api_instance.delete_snat_entry(delete_snat_entry_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
