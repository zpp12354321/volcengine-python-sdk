# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkvpc
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
    api_instance = volcenginesdkvpc.VPCApi()
    delete_security_group_request = volcenginesdkvpc.DeleteSecurityGroupRequest(
        security_group_id="sg-bp1fg655nh68xyz9****",
    )
    
    try:
        resp = api_instance.delete_security_group(delete_security_group_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
