# Example Code generated by Beijing Volcanoengine Technology.
from __future__ import print_function
import volcenginesdkcore
import volcenginesdkclb
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
    api_instance = volcenginesdkclb.CLBApi()
    attach_health_check_log_topic_request = volcenginesdkclb.AttachHealthCheckLogTopicRequest(
        load_balancer_id="clb-bp1b6c719dfa08ex****",
        log_topic_id="74936ae4-bbd6-41de-a0d2-ed156203****",
    )
    
    try:
        resp = api_instance.attach_health_check_log_topic(attach_health_check_log_topic_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
