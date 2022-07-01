# coding: utf-8

"""
    clb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeListenerHealthRequest(object):
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
        'listener_id': 'str',
        'only_un_healthy': 'str',
        'page_number': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'listener_id': 'ListenerId',
        'only_un_healthy': 'OnlyUnHealthy',
        'page_number': 'PageNumber',
        'page_size': 'PageSize'
    }

    def __init__(self, listener_id=None, only_un_healthy=None, page_number=None, page_size=None, _configuration=None):  # noqa: E501
        """DescribeListenerHealthRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._listener_id = None
        self._only_un_healthy = None
        self._page_number = None
        self._page_size = None
        self.discriminator = None

        self.listener_id = listener_id
        if only_un_healthy is not None:
            self.only_un_healthy = only_un_healthy
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size

    @property
    def listener_id(self):
        """Gets the listener_id of this DescribeListenerHealthRequest.  # noqa: E501


        :return: The listener_id of this DescribeListenerHealthRequest.  # noqa: E501
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this DescribeListenerHealthRequest.


        :param listener_id: The listener_id of this DescribeListenerHealthRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and listener_id is None:
            raise ValueError("Invalid value for `listener_id`, must not be `None`")  # noqa: E501

        self._listener_id = listener_id

    @property
    def only_un_healthy(self):
        """Gets the only_un_healthy of this DescribeListenerHealthRequest.  # noqa: E501


        :return: The only_un_healthy of this DescribeListenerHealthRequest.  # noqa: E501
        :rtype: str
        """
        return self._only_un_healthy

    @only_un_healthy.setter
    def only_un_healthy(self, only_un_healthy):
        """Sets the only_un_healthy of this DescribeListenerHealthRequest.


        :param only_un_healthy: The only_un_healthy of this DescribeListenerHealthRequest.  # noqa: E501
        :type: str
        """

        self._only_un_healthy = only_un_healthy

    @property
    def page_number(self):
        """Gets the page_number of this DescribeListenerHealthRequest.  # noqa: E501


        :return: The page_number of this DescribeListenerHealthRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeListenerHealthRequest.


        :param page_number: The page_number of this DescribeListenerHealthRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeListenerHealthRequest.  # noqa: E501


        :return: The page_size of this DescribeListenerHealthRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeListenerHealthRequest.


        :param page_size: The page_size of this DescribeListenerHealthRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

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
        if issubclass(DescribeListenerHealthRequest, dict):
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
        if not isinstance(other, DescribeListenerHealthRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeListenerHealthRequest):
            return True

        return self.to_dict() != other.to_dict()
