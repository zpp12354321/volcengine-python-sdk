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


class ScalingInstanceForDescribeScalingInstancesOutput(object):
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
        'created_time': 'str',
        'creation_type': 'str',
        'entrusted': 'bool',
        'instance_id': 'str',
        'scaling_configuration_id': 'str',
        'scaling_group_id': 'str',
        'scaling_policy_id': 'str',
        'status': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'created_time': 'CreatedTime',
        'creation_type': 'CreationType',
        'entrusted': 'Entrusted',
        'instance_id': 'InstanceId',
        'scaling_configuration_id': 'ScalingConfigurationId',
        'scaling_group_id': 'ScalingGroupId',
        'scaling_policy_id': 'ScalingPolicyId',
        'status': 'Status',
        'zone_id': 'ZoneId'
    }

    def __init__(self, created_time=None, creation_type=None, entrusted=None, instance_id=None, scaling_configuration_id=None, scaling_group_id=None, scaling_policy_id=None, status=None, zone_id=None, _configuration=None):  # noqa: E501
        """ScalingInstanceForDescribeScalingInstancesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created_time = None
        self._creation_type = None
        self._entrusted = None
        self._instance_id = None
        self._scaling_configuration_id = None
        self._scaling_group_id = None
        self._scaling_policy_id = None
        self._status = None
        self._zone_id = None
        self.discriminator = None

        if created_time is not None:
            self.created_time = created_time
        if creation_type is not None:
            self.creation_type = creation_type
        if entrusted is not None:
            self.entrusted = entrusted
        if instance_id is not None:
            self.instance_id = instance_id
        if scaling_configuration_id is not None:
            self.scaling_configuration_id = scaling_configuration_id
        if scaling_group_id is not None:
            self.scaling_group_id = scaling_group_id
        if scaling_policy_id is not None:
            self.scaling_policy_id = scaling_policy_id
        if status is not None:
            self.status = status
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def created_time(self):
        """Gets the created_time of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501


        :return: The created_time of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ScalingInstanceForDescribeScalingInstancesOutput.


        :param created_time: The created_time of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501
        :type: str
        """

        self._created_time = created_time

    @property
    def creation_type(self):
        """Gets the creation_type of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501


        :return: The creation_type of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._creation_type

    @creation_type.setter
    def creation_type(self, creation_type):
        """Sets the creation_type of this ScalingInstanceForDescribeScalingInstancesOutput.


        :param creation_type: The creation_type of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501
        :type: str
        """

        self._creation_type = creation_type

    @property
    def entrusted(self):
        """Gets the entrusted of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501


        :return: The entrusted of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501
        :rtype: bool
        """
        return self._entrusted

    @entrusted.setter
    def entrusted(self, entrusted):
        """Sets the entrusted of this ScalingInstanceForDescribeScalingInstancesOutput.


        :param entrusted: The entrusted of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501
        :type: bool
        """

        self._entrusted = entrusted

    @property
    def instance_id(self):
        """Gets the instance_id of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501


        :return: The instance_id of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ScalingInstanceForDescribeScalingInstancesOutput.


        :param instance_id: The instance_id of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def scaling_configuration_id(self):
        """Gets the scaling_configuration_id of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501


        :return: The scaling_configuration_id of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._scaling_configuration_id

    @scaling_configuration_id.setter
    def scaling_configuration_id(self, scaling_configuration_id):
        """Sets the scaling_configuration_id of this ScalingInstanceForDescribeScalingInstancesOutput.


        :param scaling_configuration_id: The scaling_configuration_id of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501
        :type: str
        """

        self._scaling_configuration_id = scaling_configuration_id

    @property
    def scaling_group_id(self):
        """Gets the scaling_group_id of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501


        :return: The scaling_group_id of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        """Sets the scaling_group_id of this ScalingInstanceForDescribeScalingInstancesOutput.


        :param scaling_group_id: The scaling_group_id of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501
        :type: str
        """

        self._scaling_group_id = scaling_group_id

    @property
    def scaling_policy_id(self):
        """Gets the scaling_policy_id of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501


        :return: The scaling_policy_id of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._scaling_policy_id

    @scaling_policy_id.setter
    def scaling_policy_id(self, scaling_policy_id):
        """Sets the scaling_policy_id of this ScalingInstanceForDescribeScalingInstancesOutput.


        :param scaling_policy_id: The scaling_policy_id of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501
        :type: str
        """

        self._scaling_policy_id = scaling_policy_id

    @property
    def status(self):
        """Gets the status of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501


        :return: The status of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ScalingInstanceForDescribeScalingInstancesOutput.


        :param status: The status of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def zone_id(self):
        """Gets the zone_id of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501


        :return: The zone_id of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this ScalingInstanceForDescribeScalingInstancesOutput.


        :param zone_id: The zone_id of this ScalingInstanceForDescribeScalingInstancesOutput.  # noqa: E501
        :type: str
        """

        self._zone_id = zone_id

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
        if issubclass(ScalingInstanceForDescribeScalingInstancesOutput, dict):
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
        if not isinstance(other, ScalingInstanceForDescribeScalingInstancesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScalingInstanceForDescribeScalingInstancesOutput):
            return True

        return self.to_dict() != other.to_dict()
