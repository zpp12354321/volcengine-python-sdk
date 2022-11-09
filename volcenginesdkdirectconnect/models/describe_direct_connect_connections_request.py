# coding: utf-8

"""
    directconnect

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeDirectConnectConnectionsRequest(object):
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
        'access_point': 'str',
        'connection_type': 'str',
        'direct_connect_connection_ids': 'list[str]',
        'direct_connect_connection_name': 'str',
        'line_operator': 'str',
        'operator': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'peer_location': 'str',
        'tag_filters': 'list[TagFilterForDescribeDirectConnectConnectionsInput]'
    }

    attribute_map = {
        'access_point': 'AccessPoint',
        'connection_type': 'ConnectionType',
        'direct_connect_connection_ids': 'DirectConnectConnectionIds',
        'direct_connect_connection_name': 'DirectConnectConnectionName',
        'line_operator': 'LineOperator',
        'operator': 'Operator',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'peer_location': 'PeerLocation',
        'tag_filters': 'TagFilters'
    }

    def __init__(self, access_point=None, connection_type=None, direct_connect_connection_ids=None, direct_connect_connection_name=None, line_operator=None, operator=None, page_number=None, page_size=None, peer_location=None, tag_filters=None, _configuration=None):  # noqa: E501
        """DescribeDirectConnectConnectionsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_point = None
        self._connection_type = None
        self._direct_connect_connection_ids = None
        self._direct_connect_connection_name = None
        self._line_operator = None
        self._operator = None
        self._page_number = None
        self._page_size = None
        self._peer_location = None
        self._tag_filters = None
        self.discriminator = None

        if access_point is not None:
            self.access_point = access_point
        if connection_type is not None:
            self.connection_type = connection_type
        if direct_connect_connection_ids is not None:
            self.direct_connect_connection_ids = direct_connect_connection_ids
        if direct_connect_connection_name is not None:
            self.direct_connect_connection_name = direct_connect_connection_name
        if line_operator is not None:
            self.line_operator = line_operator
        if operator is not None:
            self.operator = operator
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if peer_location is not None:
            self.peer_location = peer_location
        if tag_filters is not None:
            self.tag_filters = tag_filters

    @property
    def access_point(self):
        """Gets the access_point of this DescribeDirectConnectConnectionsRequest.  # noqa: E501


        :return: The access_point of this DescribeDirectConnectConnectionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._access_point

    @access_point.setter
    def access_point(self, access_point):
        """Sets the access_point of this DescribeDirectConnectConnectionsRequest.


        :param access_point: The access_point of this DescribeDirectConnectConnectionsRequest.  # noqa: E501
        :type: str
        """

        self._access_point = access_point

    @property
    def connection_type(self):
        """Gets the connection_type of this DescribeDirectConnectConnectionsRequest.  # noqa: E501


        :return: The connection_type of this DescribeDirectConnectConnectionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """Sets the connection_type of this DescribeDirectConnectConnectionsRequest.


        :param connection_type: The connection_type of this DescribeDirectConnectConnectionsRequest.  # noqa: E501
        :type: str
        """

        self._connection_type = connection_type

    @property
    def direct_connect_connection_ids(self):
        """Gets the direct_connect_connection_ids of this DescribeDirectConnectConnectionsRequest.  # noqa: E501


        :return: The direct_connect_connection_ids of this DescribeDirectConnectConnectionsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._direct_connect_connection_ids

    @direct_connect_connection_ids.setter
    def direct_connect_connection_ids(self, direct_connect_connection_ids):
        """Sets the direct_connect_connection_ids of this DescribeDirectConnectConnectionsRequest.


        :param direct_connect_connection_ids: The direct_connect_connection_ids of this DescribeDirectConnectConnectionsRequest.  # noqa: E501
        :type: list[str]
        """

        self._direct_connect_connection_ids = direct_connect_connection_ids

    @property
    def direct_connect_connection_name(self):
        """Gets the direct_connect_connection_name of this DescribeDirectConnectConnectionsRequest.  # noqa: E501


        :return: The direct_connect_connection_name of this DescribeDirectConnectConnectionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._direct_connect_connection_name

    @direct_connect_connection_name.setter
    def direct_connect_connection_name(self, direct_connect_connection_name):
        """Sets the direct_connect_connection_name of this DescribeDirectConnectConnectionsRequest.


        :param direct_connect_connection_name: The direct_connect_connection_name of this DescribeDirectConnectConnectionsRequest.  # noqa: E501
        :type: str
        """

        self._direct_connect_connection_name = direct_connect_connection_name

    @property
    def line_operator(self):
        """Gets the line_operator of this DescribeDirectConnectConnectionsRequest.  # noqa: E501


        :return: The line_operator of this DescribeDirectConnectConnectionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._line_operator

    @line_operator.setter
    def line_operator(self, line_operator):
        """Sets the line_operator of this DescribeDirectConnectConnectionsRequest.


        :param line_operator: The line_operator of this DescribeDirectConnectConnectionsRequest.  # noqa: E501
        :type: str
        """

        self._line_operator = line_operator

    @property
    def operator(self):
        """Gets the operator of this DescribeDirectConnectConnectionsRequest.  # noqa: E501


        :return: The operator of this DescribeDirectConnectConnectionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this DescribeDirectConnectConnectionsRequest.


        :param operator: The operator of this DescribeDirectConnectConnectionsRequest.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def page_number(self):
        """Gets the page_number of this DescribeDirectConnectConnectionsRequest.  # noqa: E501


        :return: The page_number of this DescribeDirectConnectConnectionsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeDirectConnectConnectionsRequest.


        :param page_number: The page_number of this DescribeDirectConnectConnectionsRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeDirectConnectConnectionsRequest.  # noqa: E501


        :return: The page_size of this DescribeDirectConnectConnectionsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeDirectConnectConnectionsRequest.


        :param page_size: The page_size of this DescribeDirectConnectConnectionsRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def peer_location(self):
        """Gets the peer_location of this DescribeDirectConnectConnectionsRequest.  # noqa: E501


        :return: The peer_location of this DescribeDirectConnectConnectionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._peer_location

    @peer_location.setter
    def peer_location(self, peer_location):
        """Sets the peer_location of this DescribeDirectConnectConnectionsRequest.


        :param peer_location: The peer_location of this DescribeDirectConnectConnectionsRequest.  # noqa: E501
        :type: str
        """

        self._peer_location = peer_location

    @property
    def tag_filters(self):
        """Gets the tag_filters of this DescribeDirectConnectConnectionsRequest.  # noqa: E501


        :return: The tag_filters of this DescribeDirectConnectConnectionsRequest.  # noqa: E501
        :rtype: list[TagFilterForDescribeDirectConnectConnectionsInput]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """Sets the tag_filters of this DescribeDirectConnectConnectionsRequest.


        :param tag_filters: The tag_filters of this DescribeDirectConnectConnectionsRequest.  # noqa: E501
        :type: list[TagFilterForDescribeDirectConnectConnectionsInput]
        """

        self._tag_filters = tag_filters

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
        if issubclass(DescribeDirectConnectConnectionsRequest, dict):
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
        if not isinstance(other, DescribeDirectConnectConnectionsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeDirectConnectConnectionsRequest):
            return True

        return self.to_dict() != other.to_dict()
