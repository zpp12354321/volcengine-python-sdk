# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkecs
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
    api_instance = volcenginesdkecs.ECSApi()
    delete_deployment_set_request = volcenginesdkecs.DeleteDeploymentSetRequest(
        deployment_set_id="dps-yc1o9aahks5m57nk****",
    )

    try:
        resp = api_instance.delete_deployment_set(delete_deployment_set_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
