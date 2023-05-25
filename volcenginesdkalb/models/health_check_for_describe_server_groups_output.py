# coding: utf-8

"""
    alb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class HealthCheckForDescribeServerGroupsOutput(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'domain': 'str',
        'enabled': 'str',
        'healthy_threshold': 'int',
        'http_code': 'str',
        'interval': 'int',
        'method': 'str',
        'protocol': 'str',
        'timeout': 'int',
        'uri': 'str',
        'unhealthy_threshold': 'int'
    }

    attribute_map = {
        'domain': 'Domain',
        'enabled': 'Enabled',
        'healthy_threshold': 'HealthyThreshold',
        'http_code': 'HttpCode',
        'interval': 'Interval',
        'method': 'Method',
        'protocol': 'Protocol',
        'timeout': 'Timeout',
        'uri': 'URI',
        'unhealthy_threshold': 'UnhealthyThreshold'
    }

    def __init__(self, domain=None, enabled=None, healthy_threshold=None, http_code=None, interval=None, method=None, protocol=None, timeout=None, uri=None, unhealthy_threshold=None, _configuration=None):  # noqa: E501
        """HealthCheckForDescribeServerGroupsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._domain = None
        self._enabled = None
        self._healthy_threshold = None
        self._http_code = None
        self._interval = None
        self._method = None
        self._protocol = None
        self._timeout = None
        self._uri = None
        self._unhealthy_threshold = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if enabled is not None:
            self.enabled = enabled
        if healthy_threshold is not None:
            self.healthy_threshold = healthy_threshold
        if http_code is not None:
            self.http_code = http_code
        if interval is not None:
            self.interval = interval
        if method is not None:
            self.method = method
        if protocol is not None:
            self.protocol = protocol
        if timeout is not None:
            self.timeout = timeout
        if uri is not None:
            self.uri = uri
        if unhealthy_threshold is not None:
            self.unhealthy_threshold = unhealthy_threshold

    @property
    def domain(self):
        """Gets the domain of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501


        :return: The domain of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this HealthCheckForDescribeServerGroupsOutput.


        :param domain: The domain of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def enabled(self):
        """Gets the enabled of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501


        :return: The enabled of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this HealthCheckForDescribeServerGroupsOutput.


        :param enabled: The enabled of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501
        :type: str
        """

        self._enabled = enabled

    @property
    def healthy_threshold(self):
        """Gets the healthy_threshold of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501


        :return: The healthy_threshold of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._healthy_threshold

    @healthy_threshold.setter
    def healthy_threshold(self, healthy_threshold):
        """Sets the healthy_threshold of this HealthCheckForDescribeServerGroupsOutput.


        :param healthy_threshold: The healthy_threshold of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501
        :type: int
        """

        self._healthy_threshold = healthy_threshold

    @property
    def http_code(self):
        """Gets the http_code of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501


        :return: The http_code of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._http_code

    @http_code.setter
    def http_code(self, http_code):
        """Sets the http_code of this HealthCheckForDescribeServerGroupsOutput.


        :param http_code: The http_code of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501
        :type: str
        """

        self._http_code = http_code

    @property
    def interval(self):
        """Gets the interval of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501


        :return: The interval of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this HealthCheckForDescribeServerGroupsOutput.


        :param interval: The interval of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501
        :type: int
        """

        self._interval = interval

    @property
    def method(self):
        """Gets the method of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501


        :return: The method of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this HealthCheckForDescribeServerGroupsOutput.


        :param method: The method of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501
        :type: str
        """

        self._method = method

    @property
    def protocol(self):
        """Gets the protocol of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501


        :return: The protocol of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this HealthCheckForDescribeServerGroupsOutput.


        :param protocol: The protocol of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def timeout(self):
        """Gets the timeout of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501


        :return: The timeout of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this HealthCheckForDescribeServerGroupsOutput.


        :param timeout: The timeout of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def uri(self):
        """Gets the uri of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501


        :return: The uri of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this HealthCheckForDescribeServerGroupsOutput.


        :param uri: The uri of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def unhealthy_threshold(self):
        """Gets the unhealthy_threshold of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501


        :return: The unhealthy_threshold of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._unhealthy_threshold

    @unhealthy_threshold.setter
    def unhealthy_threshold(self, unhealthy_threshold):
        """Sets the unhealthy_threshold of this HealthCheckForDescribeServerGroupsOutput.


        :param unhealthy_threshold: The unhealthy_threshold of this HealthCheckForDescribeServerGroupsOutput.  # noqa: E501
        :type: int
        """

        self._unhealthy_threshold = unhealthy_threshold

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(HealthCheckForDescribeServerGroupsOutput, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HealthCheckForDescribeServerGroupsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HealthCheckForDescribeServerGroupsOutput):
            return True

        return self.to_dict() != other.to_dict()