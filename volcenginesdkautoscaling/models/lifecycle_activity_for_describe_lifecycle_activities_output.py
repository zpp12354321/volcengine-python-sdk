# coding: utf-8

"""
    auto_scaling

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class LifecycleActivityForDescribeLifecycleActivitiesOutput(object):
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
        'instance_id': 'str',
        'lifecycle_activity_id': 'str',
        'lifecycle_activity_status': 'str',
        'lifecycle_hook_id': 'str',
        'lifecycle_hook_policy': 'str',
        'scaling_activity_id': 'str'
    }

    attribute_map = {
        'instance_id': 'InstanceId',
        'lifecycle_activity_id': 'LifecycleActivityId',
        'lifecycle_activity_status': 'LifecycleActivityStatus',
        'lifecycle_hook_id': 'LifecycleHookId',
        'lifecycle_hook_policy': 'LifecycleHookPolicy',
        'scaling_activity_id': 'ScalingActivityId'
    }

    def __init__(self, instance_id=None, lifecycle_activity_id=None, lifecycle_activity_status=None, lifecycle_hook_id=None, lifecycle_hook_policy=None, scaling_activity_id=None, _configuration=None):  # noqa: E501
        """LifecycleActivityForDescribeLifecycleActivitiesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._instance_id = None
        self._lifecycle_activity_id = None
        self._lifecycle_activity_status = None
        self._lifecycle_hook_id = None
        self._lifecycle_hook_policy = None
        self._scaling_activity_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if lifecycle_activity_id is not None:
            self.lifecycle_activity_id = lifecycle_activity_id
        if lifecycle_activity_status is not None:
            self.lifecycle_activity_status = lifecycle_activity_status
        if lifecycle_hook_id is not None:
            self.lifecycle_hook_id = lifecycle_hook_id
        if lifecycle_hook_policy is not None:
            self.lifecycle_hook_policy = lifecycle_hook_policy
        if scaling_activity_id is not None:
            self.scaling_activity_id = scaling_activity_id

    @property
    def instance_id(self):
        """Gets the instance_id of this LifecycleActivityForDescribeLifecycleActivitiesOutput.  # noqa: E501


        :return: The instance_id of this LifecycleActivityForDescribeLifecycleActivitiesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this LifecycleActivityForDescribeLifecycleActivitiesOutput.


        :param instance_id: The instance_id of this LifecycleActivityForDescribeLifecycleActivitiesOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def lifecycle_activity_id(self):
        """Gets the lifecycle_activity_id of this LifecycleActivityForDescribeLifecycleActivitiesOutput.  # noqa: E501


        :return: The lifecycle_activity_id of this LifecycleActivityForDescribeLifecycleActivitiesOutput.  # noqa: E501
        :rtype: str
        """
        return self._lifecycle_activity_id

    @lifecycle_activity_id.setter
    def lifecycle_activity_id(self, lifecycle_activity_id):
        """Sets the lifecycle_activity_id of this LifecycleActivityForDescribeLifecycleActivitiesOutput.


        :param lifecycle_activity_id: The lifecycle_activity_id of this LifecycleActivityForDescribeLifecycleActivitiesOutput.  # noqa: E501
        :type: str
        """

        self._lifecycle_activity_id = lifecycle_activity_id

    @property
    def lifecycle_activity_status(self):
        """Gets the lifecycle_activity_status of this LifecycleActivityForDescribeLifecycleActivitiesOutput.  # noqa: E501


        :return: The lifecycle_activity_status of this LifecycleActivityForDescribeLifecycleActivitiesOutput.  # noqa: E501
        :rtype: str
        """
        return self._lifecycle_activity_status

    @lifecycle_activity_status.setter
    def lifecycle_activity_status(self, lifecycle_activity_status):
        """Sets the lifecycle_activity_status of this LifecycleActivityForDescribeLifecycleActivitiesOutput.


        :param lifecycle_activity_status: The lifecycle_activity_status of this LifecycleActivityForDescribeLifecycleActivitiesOutput.  # noqa: E501
        :type: str
        """

        self._lifecycle_activity_status = lifecycle_activity_status

    @property
    def lifecycle_hook_id(self):
        """Gets the lifecycle_hook_id of this LifecycleActivityForDescribeLifecycleActivitiesOutput.  # noqa: E501


        :return: The lifecycle_hook_id of this LifecycleActivityForDescribeLifecycleActivitiesOutput.  # noqa: E501
        :rtype: str
        """
        return self._lifecycle_hook_id

    @lifecycle_hook_id.setter
    def lifecycle_hook_id(self, lifecycle_hook_id):
        """Sets the lifecycle_hook_id of this LifecycleActivityForDescribeLifecycleActivitiesOutput.


        :param lifecycle_hook_id: The lifecycle_hook_id of this LifecycleActivityForDescribeLifecycleActivitiesOutput.  # noqa: E501
        :type: str
        """

        self._lifecycle_hook_id = lifecycle_hook_id

    @property
    def lifecycle_hook_policy(self):
        """Gets the lifecycle_hook_policy of this LifecycleActivityForDescribeLifecycleActivitiesOutput.  # noqa: E501


        :return: The lifecycle_hook_policy of this LifecycleActivityForDescribeLifecycleActivitiesOutput.  # noqa: E501
        :rtype: str
        """
        return self._lifecycle_hook_policy

    @lifecycle_hook_policy.setter
    def lifecycle_hook_policy(self, lifecycle_hook_policy):
        """Sets the lifecycle_hook_policy of this LifecycleActivityForDescribeLifecycleActivitiesOutput.


        :param lifecycle_hook_policy: The lifecycle_hook_policy of this LifecycleActivityForDescribeLifecycleActivitiesOutput.  # noqa: E501
        :type: str
        """

        self._lifecycle_hook_policy = lifecycle_hook_policy

    @property
    def scaling_activity_id(self):
        """Gets the scaling_activity_id of this LifecycleActivityForDescribeLifecycleActivitiesOutput.  # noqa: E501


        :return: The scaling_activity_id of this LifecycleActivityForDescribeLifecycleActivitiesOutput.  # noqa: E501
        :rtype: str
        """
        return self._scaling_activity_id

    @scaling_activity_id.setter
    def scaling_activity_id(self, scaling_activity_id):
        """Sets the scaling_activity_id of this LifecycleActivityForDescribeLifecycleActivitiesOutput.


        :param scaling_activity_id: The scaling_activity_id of this LifecycleActivityForDescribeLifecycleActivitiesOutput.  # noqa: E501
        :type: str
        """

        self._scaling_activity_id = scaling_activity_id

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
        if issubclass(LifecycleActivityForDescribeLifecycleActivitiesOutput, dict):
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
        if not isinstance(other, LifecycleActivityForDescribeLifecycleActivitiesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LifecycleActivityForDescribeLifecycleActivitiesOutput):
            return True

        return self.to_dict() != other.to_dict()
