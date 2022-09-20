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


class CreateDefaultNodePoolRequest(object):
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
        'kubernetes_config': 'KubernetesConfigForCreateDefaultNodePoolInput',
        'node_config': 'NodeConfigForCreateDefaultNodePoolInput'
    }

    attribute_map = {
        'client_token': 'ClientToken',
        'cluster_id': 'ClusterId',
        'kubernetes_config': 'KubernetesConfig',
        'node_config': 'NodeConfig'
    }

    def __init__(self, client_token=None, cluster_id=None, kubernetes_config=None, node_config=None, _configuration=None):  # noqa: E501
        """CreateDefaultNodePoolRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_token = None
        self._cluster_id = None
        self._kubernetes_config = None
        self._node_config = None
        self.discriminator = None

        if client_token is not None:
            self.client_token = client_token
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if kubernetes_config is not None:
            self.kubernetes_config = kubernetes_config
        if node_config is not None:
            self.node_config = node_config

    @property
    def client_token(self):
        """Gets the client_token of this CreateDefaultNodePoolRequest.  # noqa: E501


        :return: The client_token of this CreateDefaultNodePoolRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this CreateDefaultNodePoolRequest.


        :param client_token: The client_token of this CreateDefaultNodePoolRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def cluster_id(self):
        """Gets the cluster_id of this CreateDefaultNodePoolRequest.  # noqa: E501


        :return: The cluster_id of this CreateDefaultNodePoolRequest.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this CreateDefaultNodePoolRequest.


        :param cluster_id: The cluster_id of this CreateDefaultNodePoolRequest.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def kubernetes_config(self):
        """Gets the kubernetes_config of this CreateDefaultNodePoolRequest.  # noqa: E501


        :return: The kubernetes_config of this CreateDefaultNodePoolRequest.  # noqa: E501
        :rtype: KubernetesConfigForCreateDefaultNodePoolInput
        """
        return self._kubernetes_config

    @kubernetes_config.setter
    def kubernetes_config(self, kubernetes_config):
        """Sets the kubernetes_config of this CreateDefaultNodePoolRequest.


        :param kubernetes_config: The kubernetes_config of this CreateDefaultNodePoolRequest.  # noqa: E501
        :type: KubernetesConfigForCreateDefaultNodePoolInput
        """

        self._kubernetes_config = kubernetes_config

    @property
    def node_config(self):
        """Gets the node_config of this CreateDefaultNodePoolRequest.  # noqa: E501


        :return: The node_config of this CreateDefaultNodePoolRequest.  # noqa: E501
        :rtype: NodeConfigForCreateDefaultNodePoolInput
        """
        return self._node_config

    @node_config.setter
    def node_config(self, node_config):
        """Sets the node_config of this CreateDefaultNodePoolRequest.


        :param node_config: The node_config of this CreateDefaultNodePoolRequest.  # noqa: E501
        :type: NodeConfigForCreateDefaultNodePoolInput
        """

        self._node_config = node_config

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
        if issubclass(CreateDefaultNodePoolRequest, dict):
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
        if not isinstance(other, CreateDefaultNodePoolRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDefaultNodePoolRequest):
            return True

        return self.to_dict() != other.to_dict()
