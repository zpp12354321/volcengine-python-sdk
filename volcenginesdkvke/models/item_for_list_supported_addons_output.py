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


class ItemForListSupportedAddonsOutput(object):
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
        'categories': 'list[str]',
        'deploy_mode': 'str',
        'deploy_node_types': 'list[str]',
        'name': 'str',
        'necessary': 'str',
        'pod_network_modes': 'list[str]',
        'versions': 'list[VersionForListSupportedAddonsOutput]'
    }

    attribute_map = {
        'categories': 'Categories',
        'deploy_mode': 'DeployMode',
        'deploy_node_types': 'DeployNodeTypes',
        'name': 'Name',
        'necessary': 'Necessary',
        'pod_network_modes': 'PodNetworkModes',
        'versions': 'Versions'
    }

    def __init__(self, categories=None, deploy_mode=None, deploy_node_types=None, name=None, necessary=None, pod_network_modes=None, versions=None, _configuration=None):  # noqa: E501
        """ItemForListSupportedAddonsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._categories = None
        self._deploy_mode = None
        self._deploy_node_types = None
        self._name = None
        self._necessary = None
        self._pod_network_modes = None
        self._versions = None
        self.discriminator = None

        if categories is not None:
            self.categories = categories
        if deploy_mode is not None:
            self.deploy_mode = deploy_mode
        if deploy_node_types is not None:
            self.deploy_node_types = deploy_node_types
        if name is not None:
            self.name = name
        if necessary is not None:
            self.necessary = necessary
        if pod_network_modes is not None:
            self.pod_network_modes = pod_network_modes
        if versions is not None:
            self.versions = versions

    @property
    def categories(self):
        """Gets the categories of this ItemForListSupportedAddonsOutput.  # noqa: E501


        :return: The categories of this ItemForListSupportedAddonsOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this ItemForListSupportedAddonsOutput.


        :param categories: The categories of this ItemForListSupportedAddonsOutput.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Dns", "Gpu", "Image", "Monitor", "Network", "Scheduler", "Security", "Storage"]  # noqa: E501
        if (self._configuration.client_side_validation and
                not set(categories).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `categories` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(categories) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._categories = categories

    @property
    def deploy_mode(self):
        """Gets the deploy_mode of this ItemForListSupportedAddonsOutput.  # noqa: E501


        :return: The deploy_mode of this ItemForListSupportedAddonsOutput.  # noqa: E501
        :rtype: str
        """
        return self._deploy_mode

    @deploy_mode.setter
    def deploy_mode(self, deploy_mode):
        """Sets the deploy_mode of this ItemForListSupportedAddonsOutput.


        :param deploy_mode: The deploy_mode of this ItemForListSupportedAddonsOutput.  # noqa: E501
        :type: str
        """
        allowed_values = ["Either", "Managed", "Unmanaged"]  # noqa: E501
        if (self._configuration.client_side_validation and
                deploy_mode not in allowed_values):
            raise ValueError(
                "Invalid value for `deploy_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(deploy_mode, allowed_values)
            )

        self._deploy_mode = deploy_mode

    @property
    def deploy_node_types(self):
        """Gets the deploy_node_types of this ItemForListSupportedAddonsOutput.  # noqa: E501


        :return: The deploy_node_types of this ItemForListSupportedAddonsOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._deploy_node_types

    @deploy_node_types.setter
    def deploy_node_types(self, deploy_node_types):
        """Sets the deploy_node_types of this ItemForListSupportedAddonsOutput.


        :param deploy_node_types: The deploy_node_types of this ItemForListSupportedAddonsOutput.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Node", "VirtualNode"]  # noqa: E501
        if (self._configuration.client_side_validation and
                not set(deploy_node_types).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `deploy_node_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(deploy_node_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._deploy_node_types = deploy_node_types

    @property
    def name(self):
        """Gets the name of this ItemForListSupportedAddonsOutput.  # noqa: E501


        :return: The name of this ItemForListSupportedAddonsOutput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ItemForListSupportedAddonsOutput.


        :param name: The name of this ItemForListSupportedAddonsOutput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def necessary(self):
        """Gets the necessary of this ItemForListSupportedAddonsOutput.  # noqa: E501


        :return: The necessary of this ItemForListSupportedAddonsOutput.  # noqa: E501
        :rtype: str
        """
        return self._necessary

    @necessary.setter
    def necessary(self, necessary):
        """Sets the necessary of this ItemForListSupportedAddonsOutput.


        :param necessary: The necessary of this ItemForListSupportedAddonsOutput.  # noqa: E501
        :type: str
        """
        allowed_values = ["OnDemand", "Recommended", "Required"]  # noqa: E501
        if (self._configuration.client_side_validation and
                necessary not in allowed_values):
            raise ValueError(
                "Invalid value for `necessary` ({0}), must be one of {1}"  # noqa: E501
                .format(necessary, allowed_values)
            )

        self._necessary = necessary

    @property
    def pod_network_modes(self):
        """Gets the pod_network_modes of this ItemForListSupportedAddonsOutput.  # noqa: E501


        :return: The pod_network_modes of this ItemForListSupportedAddonsOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._pod_network_modes

    @pod_network_modes.setter
    def pod_network_modes(self, pod_network_modes):
        """Sets the pod_network_modes of this ItemForListSupportedAddonsOutput.


        :param pod_network_modes: The pod_network_modes of this ItemForListSupportedAddonsOutput.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["CalicoBgp", "CalicoVxlan", "Flannel", "VpcCniDedicated", "VpcCniShared"]  # noqa: E501
        if (self._configuration.client_side_validation and
                not set(pod_network_modes).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `pod_network_modes` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(pod_network_modes) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._pod_network_modes = pod_network_modes

    @property
    def versions(self):
        """Gets the versions of this ItemForListSupportedAddonsOutput.  # noqa: E501


        :return: The versions of this ItemForListSupportedAddonsOutput.  # noqa: E501
        :rtype: list[VersionForListSupportedAddonsOutput]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this ItemForListSupportedAddonsOutput.


        :param versions: The versions of this ItemForListSupportedAddonsOutput.  # noqa: E501
        :type: list[VersionForListSupportedAddonsOutput]
        """

        self._versions = versions

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
        if issubclass(ItemForListSupportedAddonsOutput, dict):
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
        if not isinstance(other, ItemForListSupportedAddonsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ItemForListSupportedAddonsOutput):
            return True

        return self.to_dict() != other.to_dict()
