# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkecs
from pprint import pprint
from volcenginesdkcore.rest import ApiException

if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.ak = "Your AK"
    configuration.sk = "Your SK"
    configuration.region = "cn-beijing"
    # set default configuration
    volcenginesdkcore.Configuration.set_default(configuration)

    # use global default configuration
    api_instance = volcenginesdkecs.ECSApi()
    modify_subscription_event_types_request = volcenginesdkecs.ModifySubscriptionEventTypesRequest(
        event_types=["SystemFailure.Stop:Succeeded", "SystemFailure.Stop:Succeeded"],
        subscription_id="s-6js1al1y9665lp******",
    )
    
    try:
        resp = api_instance.modify_subscription_event_types(modify_subscription_event_types_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
