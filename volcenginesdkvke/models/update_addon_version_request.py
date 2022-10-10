# coding: utf-8

"""
    vke

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UpdateAddonVersionRequest(object):
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
        'client_token': 'str',
        'cluster_id': 'str',
        'name': 'str',
        'version': 'str'
    }

    attribute_map = {
        'client_token': 'ClientToken',
        'cluster_id': 'ClusterId',
        'name': 'Name',
        'version': 'Version'
    }

    def __init__(self, client_token=None, cluster_id=None, name=None, version=None, _configuration=None):  # noqa: E501
        """UpdateAddonVersionRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_token = None
        self._cluster_id = None
        self._name = None
        self._version = None
        self.discriminator = None

        if client_token is not None:
            self.client_token = client_token
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version

    @property
    def client_token(self):
        """Gets the client_token of this UpdateAddonVersionRequest.  # noqa: E501


        :return: The client_token of this UpdateAddonVersionRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this UpdateAddonVersionRequest.


        :param client_token: The client_token of this UpdateAddonVersionRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def cluster_id(self):
        """Gets the cluster_id of this UpdateAddonVersionRequest.  # noqa: E501


        :return: The cluster_id of this UpdateAddonVersionRequest.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this UpdateAddonVersionRequest.


        :param cluster_id: The cluster_id of this UpdateAddonVersionRequest.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def name(self):
        """Gets the name of this UpdateAddonVersionRequest.  # noqa: E501


        :return: The name of this UpdateAddonVersionRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateAddonVersionRequest.


        :param name: The name of this UpdateAddonVersionRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def version(self):
        """Gets the version of this UpdateAddonVersionRequest.  # noqa: E501


        :return: The version of this UpdateAddonVersionRequest.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UpdateAddonVersionRequest.


        :param version: The version of this UpdateAddonVersionRequest.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(UpdateAddonVersionRequest, dict):
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
        if not isinstance(other, UpdateAddonVersionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateAddonVersionRequest):
            return True

        return self.to_dict() != other.to_dict()