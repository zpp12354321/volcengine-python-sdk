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


class PodsConfigForListClustersOutput(object):
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
        'flannel_config': 'FlannelConfigForListClustersOutput',
        'pod_network_mode': 'str',
        'vpc_cni_config': 'VpcCniConfigForListClustersOutput'
    }

    attribute_map = {
        'flannel_config': 'FlannelConfig',
        'pod_network_mode': 'PodNetworkMode',
        'vpc_cni_config': 'VpcCniConfig'
    }

    def __init__(self, flannel_config=None, pod_network_mode=None, vpc_cni_config=None, _configuration=None):  # noqa: E501
        """PodsConfigForListClustersOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._flannel_config = None
        self._pod_network_mode = None
        self._vpc_cni_config = None
        self.discriminator = None

        if flannel_config is not None:
            self.flannel_config = flannel_config
        if pod_network_mode is not None:
            self.pod_network_mode = pod_network_mode
        if vpc_cni_config is not None:
            self.vpc_cni_config = vpc_cni_config

    @property
    def flannel_config(self):
        """Gets the flannel_config of this PodsConfigForListClustersOutput.  # noqa: E501


        :return: The flannel_config of this PodsConfigForListClustersOutput.  # noqa: E501
        :rtype: FlannelConfigForListClustersOutput
        """
        return self._flannel_config

    @flannel_config.setter
    def flannel_config(self, flannel_config):
        """Sets the flannel_config of this PodsConfigForListClustersOutput.


        :param flannel_config: The flannel_config of this PodsConfigForListClustersOutput.  # noqa: E501
        :type: FlannelConfigForListClustersOutput
        """

        self._flannel_config = flannel_config

    @property
    def pod_network_mode(self):
        """Gets the pod_network_mode of this PodsConfigForListClustersOutput.  # noqa: E501


        :return: The pod_network_mode of this PodsConfigForListClustersOutput.  # noqa: E501
        :rtype: str
        """
        return self._pod_network_mode

    @pod_network_mode.setter
    def pod_network_mode(self, pod_network_mode):
        """Sets the pod_network_mode of this PodsConfigForListClustersOutput.


        :param pod_network_mode: The pod_network_mode of this PodsConfigForListClustersOutput.  # noqa: E501
        :type: str
        """

        self._pod_network_mode = pod_network_mode

    @property
    def vpc_cni_config(self):
        """Gets the vpc_cni_config of this PodsConfigForListClustersOutput.  # noqa: E501


        :return: The vpc_cni_config of this PodsConfigForListClustersOutput.  # noqa: E501
        :rtype: VpcCniConfigForListClustersOutput
        """
        return self._vpc_cni_config

    @vpc_cni_config.setter
    def vpc_cni_config(self, vpc_cni_config):
        """Sets the vpc_cni_config of this PodsConfigForListClustersOutput.


        :param vpc_cni_config: The vpc_cni_config of this PodsConfigForListClustersOutput.  # noqa: E501
        :type: VpcCniConfigForListClustersOutput
        """

        self._vpc_cni_config = vpc_cni_config

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
        if issubclass(PodsConfigForListClustersOutput, dict):
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
        if not isinstance(other, PodsConfigForListClustersOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PodsConfigForListClustersOutput):
            return True

        return self.to_dict() != other.to_dict()