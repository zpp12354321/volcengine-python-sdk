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


class DescribeServerGroupsRequest(object):
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
        'load_balancer_id': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'server_group_ids': 'list[str]',
        'server_group_name': 'str'
    }

    attribute_map = {
        'load_balancer_id': 'LoadBalancerId',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'server_group_ids': 'ServerGroupIds',
        'server_group_name': 'ServerGroupName'
    }

    def __init__(self, load_balancer_id=None, page_number=None, page_size=None, server_group_ids=None, server_group_name=None, _configuration=None):  # noqa: E501
        """DescribeServerGroupsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._load_balancer_id = None
        self._page_number = None
        self._page_size = None
        self._server_group_ids = None
        self._server_group_name = None
        self.discriminator = None

        if load_balancer_id is not None:
            self.load_balancer_id = load_balancer_id
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if server_group_ids is not None:
            self.server_group_ids = server_group_ids
        if server_group_name is not None:
            self.server_group_name = server_group_name

    @property
    def load_balancer_id(self):
        """Gets the load_balancer_id of this DescribeServerGroupsRequest.  # noqa: E501


        :return: The load_balancer_id of this DescribeServerGroupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._load_balancer_id

    @load_balancer_id.setter
    def load_balancer_id(self, load_balancer_id):
        """Sets the load_balancer_id of this DescribeServerGroupsRequest.


        :param load_balancer_id: The load_balancer_id of this DescribeServerGroupsRequest.  # noqa: E501
        :type: str
        """

        self._load_balancer_id = load_balancer_id

    @property
    def page_number(self):
        """Gets the page_number of this DescribeServerGroupsRequest.  # noqa: E501


        :return: The page_number of this DescribeServerGroupsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeServerGroupsRequest.


        :param page_number: The page_number of this DescribeServerGroupsRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeServerGroupsRequest.  # noqa: E501


        :return: The page_size of this DescribeServerGroupsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeServerGroupsRequest.


        :param page_size: The page_size of this DescribeServerGroupsRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def server_group_ids(self):
        """Gets the server_group_ids of this DescribeServerGroupsRequest.  # noqa: E501


        :return: The server_group_ids of this DescribeServerGroupsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._server_group_ids

    @server_group_ids.setter
    def server_group_ids(self, server_group_ids):
        """Sets the server_group_ids of this DescribeServerGroupsRequest.


        :param server_group_ids: The server_group_ids of this DescribeServerGroupsRequest.  # noqa: E501
        :type: list[str]
        """

        self._server_group_ids = server_group_ids

    @property
    def server_group_name(self):
        """Gets the server_group_name of this DescribeServerGroupsRequest.  # noqa: E501


        :return: The server_group_name of this DescribeServerGroupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._server_group_name

    @server_group_name.setter
    def server_group_name(self, server_group_name):
        """Sets the server_group_name of this DescribeServerGroupsRequest.


        :param server_group_name: The server_group_name of this DescribeServerGroupsRequest.  # noqa: E501
        :type: str
        """

        self._server_group_name = server_group_name

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
        if issubclass(DescribeServerGroupsRequest, dict):
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
        if not isinstance(other, DescribeServerGroupsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeServerGroupsRequest):
            return True

        return self.to_dict() != other.to_dict()
