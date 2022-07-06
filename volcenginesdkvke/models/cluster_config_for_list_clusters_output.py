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


class ClusterConfigForListClustersOutput(object):
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
        'api_server_endpoints': 'ApiServerEndpointsForListClustersOutput',
        'api_server_public_access_config': 'ApiServerPublicAccessConfigForListClustersOutput',
        'api_server_public_access_enabled': 'bool',
        'resource_public_access_default_enabled': 'bool',
        'security_group_ids': 'list[str]',
        'subnet_ids': 'list[str]',
        'vpc_id': 'str'
    }

    attribute_map = {
        'api_server_endpoints': 'ApiServerEndpoints',
        'api_server_public_access_config': 'ApiServerPublicAccessConfig',
        'api_server_public_access_enabled': 'ApiServerPublicAccessEnabled',
        'resource_public_access_default_enabled': 'ResourcePublicAccessDefaultEnabled',
        'security_group_ids': 'SecurityGroupIds',
        'subnet_ids': 'SubnetIds',
        'vpc_id': 'VpcId'
    }

    def __init__(self, api_server_endpoints=None, api_server_public_access_config=None, api_server_public_access_enabled=None, resource_public_access_default_enabled=None, security_group_ids=None, subnet_ids=None, vpc_id=None, _configuration=None):  # noqa: E501
        """ClusterConfigForListClustersOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._api_server_endpoints = None
        self._api_server_public_access_config = None
        self._api_server_public_access_enabled = None
        self._resource_public_access_default_enabled = None
        self._security_group_ids = None
        self._subnet_ids = None
        self._vpc_id = None
        self.discriminator = None

        if api_server_endpoints is not None:
            self.api_server_endpoints = api_server_endpoints
        if api_server_public_access_config is not None:
            self.api_server_public_access_config = api_server_public_access_config
        if api_server_public_access_enabled is not None:
            self.api_server_public_access_enabled = api_server_public_access_enabled
        if resource_public_access_default_enabled is not None:
            self.resource_public_access_default_enabled = resource_public_access_default_enabled
        if security_group_ids is not None:
            self.security_group_ids = security_group_ids
        if subnet_ids is not None:
            self.subnet_ids = subnet_ids
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def api_server_endpoints(self):
        """Gets the api_server_endpoints of this ClusterConfigForListClustersOutput.  # noqa: E501


        :return: The api_server_endpoints of this ClusterConfigForListClustersOutput.  # noqa: E501
        :rtype: ApiServerEndpointsForListClustersOutput
        """
        return self._api_server_endpoints

    @api_server_endpoints.setter
    def api_server_endpoints(self, api_server_endpoints):
        """Sets the api_server_endpoints of this ClusterConfigForListClustersOutput.


        :param api_server_endpoints: The api_server_endpoints of this ClusterConfigForListClustersOutput.  # noqa: E501
        :type: ApiServerEndpointsForListClustersOutput
        """

        self._api_server_endpoints = api_server_endpoints

    @property
    def api_server_public_access_config(self):
        """Gets the api_server_public_access_config of this ClusterConfigForListClustersOutput.  # noqa: E501


        :return: The api_server_public_access_config of this ClusterConfigForListClustersOutput.  # noqa: E501
        :rtype: ApiServerPublicAccessConfigForListClustersOutput
        """
        return self._api_server_public_access_config

    @api_server_public_access_config.setter
    def api_server_public_access_config(self, api_server_public_access_config):
        """Sets the api_server_public_access_config of this ClusterConfigForListClustersOutput.


        :param api_server_public_access_config: The api_server_public_access_config of this ClusterConfigForListClustersOutput.  # noqa: E501
        :type: ApiServerPublicAccessConfigForListClustersOutput
        """

        self._api_server_public_access_config = api_server_public_access_config

    @property
    def api_server_public_access_enabled(self):
        """Gets the api_server_public_access_enabled of this ClusterConfigForListClustersOutput.  # noqa: E501


        :return: The api_server_public_access_enabled of this ClusterConfigForListClustersOutput.  # noqa: E501
        :rtype: bool
        """
        return self._api_server_public_access_enabled

    @api_server_public_access_enabled.setter
    def api_server_public_access_enabled(self, api_server_public_access_enabled):
        """Sets the api_server_public_access_enabled of this ClusterConfigForListClustersOutput.


        :param api_server_public_access_enabled: The api_server_public_access_enabled of this ClusterConfigForListClustersOutput.  # noqa: E501
        :type: bool
        """

        self._api_server_public_access_enabled = api_server_public_access_enabled

    @property
    def resource_public_access_default_enabled(self):
        """Gets the resource_public_access_default_enabled of this ClusterConfigForListClustersOutput.  # noqa: E501


        :return: The resource_public_access_default_enabled of this ClusterConfigForListClustersOutput.  # noqa: E501
        :rtype: bool
        """
        return self._resource_public_access_default_enabled

    @resource_public_access_default_enabled.setter
    def resource_public_access_default_enabled(self, resource_public_access_default_enabled):
        """Sets the resource_public_access_default_enabled of this ClusterConfigForListClustersOutput.


        :param resource_public_access_default_enabled: The resource_public_access_default_enabled of this ClusterConfigForListClustersOutput.  # noqa: E501
        :type: bool
        """

        self._resource_public_access_default_enabled = resource_public_access_default_enabled

    @property
    def security_group_ids(self):
        """Gets the security_group_ids of this ClusterConfigForListClustersOutput.  # noqa: E501


        :return: The security_group_ids of this ClusterConfigForListClustersOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._security_group_ids

    @security_group_ids.setter
    def security_group_ids(self, security_group_ids):
        """Sets the security_group_ids of this ClusterConfigForListClustersOutput.


        :param security_group_ids: The security_group_ids of this ClusterConfigForListClustersOutput.  # noqa: E501
        :type: list[str]
        """

        self._security_group_ids = security_group_ids

    @property
    def subnet_ids(self):
        """Gets the subnet_ids of this ClusterConfigForListClustersOutput.  # noqa: E501


        :return: The subnet_ids of this ClusterConfigForListClustersOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        """Sets the subnet_ids of this ClusterConfigForListClustersOutput.


        :param subnet_ids: The subnet_ids of this ClusterConfigForListClustersOutput.  # noqa: E501
        :type: list[str]
        """

        self._subnet_ids = subnet_ids

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ClusterConfigForListClustersOutput.  # noqa: E501


        :return: The vpc_id of this ClusterConfigForListClustersOutput.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ClusterConfigForListClustersOutput.


        :param vpc_id: The vpc_id of this ClusterConfigForListClustersOutput.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

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
        if issubclass(ClusterConfigForListClustersOutput, dict):
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
        if not isinstance(other, ClusterConfigForListClustersOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterConfigForListClustersOutput):
            return True

        return self.to_dict() != other.to_dict()
