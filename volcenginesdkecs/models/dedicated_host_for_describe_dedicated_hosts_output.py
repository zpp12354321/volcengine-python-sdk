# coding: utf-8

"""
    ecs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DedicatedHostForDescribeDedicatedHostsOutput(object):
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
        'auto_placement': 'str',
        'capacity': 'CapacityForDescribeDedicatedHostsOutput',
        'charge_type': 'str',
        'cpu_overcommit_ratio': 'float',
        'created_at': 'str',
        'dedicated_host_cluster_id': 'str',
        'dedicated_host_id': 'str',
        'dedicated_host_name': 'str',
        'dedicated_host_type_id': 'str',
        'description': 'str',
        'expired_at': 'str',
        'host_recovery': 'str',
        'instances': 'list[InstanceForDescribeDedicatedHostsOutput]',
        'status': 'str',
        'updated_at': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'auto_placement': 'AutoPlacement',
        'capacity': 'Capacity',
        'charge_type': 'ChargeType',
        'cpu_overcommit_ratio': 'CpuOvercommitRatio',
        'created_at': 'CreatedAt',
        'dedicated_host_cluster_id': 'DedicatedHostClusterId',
        'dedicated_host_id': 'DedicatedHostId',
        'dedicated_host_name': 'DedicatedHostName',
        'dedicated_host_type_id': 'DedicatedHostTypeId',
        'description': 'Description',
        'expired_at': 'ExpiredAt',
        'host_recovery': 'HostRecovery',
        'instances': 'Instances',
        'status': 'Status',
        'updated_at': 'UpdatedAt',
        'zone_id': 'ZoneId'
    }

    def __init__(self, auto_placement=None, capacity=None, charge_type=None, cpu_overcommit_ratio=None, created_at=None, dedicated_host_cluster_id=None, dedicated_host_id=None, dedicated_host_name=None, dedicated_host_type_id=None, description=None, expired_at=None, host_recovery=None, instances=None, status=None, updated_at=None, zone_id=None, _configuration=None):  # noqa: E501
        """DedicatedHostForDescribeDedicatedHostsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_placement = None
        self._capacity = None
        self._charge_type = None
        self._cpu_overcommit_ratio = None
        self._created_at = None
        self._dedicated_host_cluster_id = None
        self._dedicated_host_id = None
        self._dedicated_host_name = None
        self._dedicated_host_type_id = None
        self._description = None
        self._expired_at = None
        self._host_recovery = None
        self._instances = None
        self._status = None
        self._updated_at = None
        self._zone_id = None
        self.discriminator = None

        if auto_placement is not None:
            self.auto_placement = auto_placement
        if capacity is not None:
            self.capacity = capacity
        if charge_type is not None:
            self.charge_type = charge_type
        if cpu_overcommit_ratio is not None:
            self.cpu_overcommit_ratio = cpu_overcommit_ratio
        if created_at is not None:
            self.created_at = created_at
        if dedicated_host_cluster_id is not None:
            self.dedicated_host_cluster_id = dedicated_host_cluster_id
        if dedicated_host_id is not None:
            self.dedicated_host_id = dedicated_host_id
        if dedicated_host_name is not None:
            self.dedicated_host_name = dedicated_host_name
        if dedicated_host_type_id is not None:
            self.dedicated_host_type_id = dedicated_host_type_id
        if description is not None:
            self.description = description
        if expired_at is not None:
            self.expired_at = expired_at
        if host_recovery is not None:
            self.host_recovery = host_recovery
        if instances is not None:
            self.instances = instances
        if status is not None:
            self.status = status
        if updated_at is not None:
            self.updated_at = updated_at
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def auto_placement(self):
        """Gets the auto_placement of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501


        :return: The auto_placement of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :rtype: str
        """
        return self._auto_placement

    @auto_placement.setter
    def auto_placement(self, auto_placement):
        """Sets the auto_placement of this DedicatedHostForDescribeDedicatedHostsOutput.


        :param auto_placement: The auto_placement of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :type: str
        """

        self._auto_placement = auto_placement

    @property
    def capacity(self):
        """Gets the capacity of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501


        :return: The capacity of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :rtype: CapacityForDescribeDedicatedHostsOutput
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this DedicatedHostForDescribeDedicatedHostsOutput.


        :param capacity: The capacity of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :type: CapacityForDescribeDedicatedHostsOutput
        """

        self._capacity = capacity

    @property
    def charge_type(self):
        """Gets the charge_type of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501


        :return: The charge_type of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this DedicatedHostForDescribeDedicatedHostsOutput.


        :param charge_type: The charge_type of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :type: str
        """

        self._charge_type = charge_type

    @property
    def cpu_overcommit_ratio(self):
        """Gets the cpu_overcommit_ratio of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501


        :return: The cpu_overcommit_ratio of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :rtype: float
        """
        return self._cpu_overcommit_ratio

    @cpu_overcommit_ratio.setter
    def cpu_overcommit_ratio(self, cpu_overcommit_ratio):
        """Sets the cpu_overcommit_ratio of this DedicatedHostForDescribeDedicatedHostsOutput.


        :param cpu_overcommit_ratio: The cpu_overcommit_ratio of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :type: float
        """

        self._cpu_overcommit_ratio = cpu_overcommit_ratio

    @property
    def created_at(self):
        """Gets the created_at of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501


        :return: The created_at of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DedicatedHostForDescribeDedicatedHostsOutput.


        :param created_at: The created_at of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def dedicated_host_cluster_id(self):
        """Gets the dedicated_host_cluster_id of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501


        :return: The dedicated_host_cluster_id of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :rtype: str
        """
        return self._dedicated_host_cluster_id

    @dedicated_host_cluster_id.setter
    def dedicated_host_cluster_id(self, dedicated_host_cluster_id):
        """Sets the dedicated_host_cluster_id of this DedicatedHostForDescribeDedicatedHostsOutput.


        :param dedicated_host_cluster_id: The dedicated_host_cluster_id of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :type: str
        """

        self._dedicated_host_cluster_id = dedicated_host_cluster_id

    @property
    def dedicated_host_id(self):
        """Gets the dedicated_host_id of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501


        :return: The dedicated_host_id of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :rtype: str
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        """Sets the dedicated_host_id of this DedicatedHostForDescribeDedicatedHostsOutput.


        :param dedicated_host_id: The dedicated_host_id of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :type: str
        """

        self._dedicated_host_id = dedicated_host_id

    @property
    def dedicated_host_name(self):
        """Gets the dedicated_host_name of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501


        :return: The dedicated_host_name of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :rtype: str
        """
        return self._dedicated_host_name

    @dedicated_host_name.setter
    def dedicated_host_name(self, dedicated_host_name):
        """Sets the dedicated_host_name of this DedicatedHostForDescribeDedicatedHostsOutput.


        :param dedicated_host_name: The dedicated_host_name of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :type: str
        """

        self._dedicated_host_name = dedicated_host_name

    @property
    def dedicated_host_type_id(self):
        """Gets the dedicated_host_type_id of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501


        :return: The dedicated_host_type_id of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :rtype: str
        """
        return self._dedicated_host_type_id

    @dedicated_host_type_id.setter
    def dedicated_host_type_id(self, dedicated_host_type_id):
        """Sets the dedicated_host_type_id of this DedicatedHostForDescribeDedicatedHostsOutput.


        :param dedicated_host_type_id: The dedicated_host_type_id of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :type: str
        """

        self._dedicated_host_type_id = dedicated_host_type_id

    @property
    def description(self):
        """Gets the description of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501


        :return: The description of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DedicatedHostForDescribeDedicatedHostsOutput.


        :param description: The description of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def expired_at(self):
        """Gets the expired_at of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501


        :return: The expired_at of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :rtype: str
        """
        return self._expired_at

    @expired_at.setter
    def expired_at(self, expired_at):
        """Sets the expired_at of this DedicatedHostForDescribeDedicatedHostsOutput.


        :param expired_at: The expired_at of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :type: str
        """

        self._expired_at = expired_at

    @property
    def host_recovery(self):
        """Gets the host_recovery of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501


        :return: The host_recovery of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :rtype: str
        """
        return self._host_recovery

    @host_recovery.setter
    def host_recovery(self, host_recovery):
        """Sets the host_recovery of this DedicatedHostForDescribeDedicatedHostsOutput.


        :param host_recovery: The host_recovery of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :type: str
        """

        self._host_recovery = host_recovery

    @property
    def instances(self):
        """Gets the instances of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501


        :return: The instances of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :rtype: list[InstanceForDescribeDedicatedHostsOutput]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this DedicatedHostForDescribeDedicatedHostsOutput.


        :param instances: The instances of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :type: list[InstanceForDescribeDedicatedHostsOutput]
        """

        self._instances = instances

    @property
    def status(self):
        """Gets the status of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501


        :return: The status of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DedicatedHostForDescribeDedicatedHostsOutput.


        :param status: The status of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def updated_at(self):
        """Gets the updated_at of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501


        :return: The updated_at of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DedicatedHostForDescribeDedicatedHostsOutput.


        :param updated_at: The updated_at of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def zone_id(self):
        """Gets the zone_id of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501


        :return: The zone_id of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this DedicatedHostForDescribeDedicatedHostsOutput.


        :param zone_id: The zone_id of this DedicatedHostForDescribeDedicatedHostsOutput.  # noqa: E501
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
        if issubclass(DedicatedHostForDescribeDedicatedHostsOutput, dict):
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
        if not isinstance(other, DedicatedHostForDescribeDedicatedHostsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DedicatedHostForDescribeDedicatedHostsOutput):
            return True

        return self.to_dict() != other.to_dict()
