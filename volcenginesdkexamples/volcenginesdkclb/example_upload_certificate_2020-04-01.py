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
    upload_certificate_request = volcenginesdkclb.UploadCertificateRequest(
        certificate_name="mycert1",
        private_key="***",
        public_key="***",
    )
    
    try:
        resp = api_instance.upload_certificate(upload_certificate_request)
        pprint(resp)
    except ApiException as e:
        print("Exception when calling api: %s\n" % e)
