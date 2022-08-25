# coding: utf-8

"""
    redis

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class InstanceDetailForDescribeBackupsOutput(object):
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
        'account_id': 'int',
        'arch_type': 'str',
        'charge_type': 'str',
        'engine_version': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'maintenance_time': 'str',
        'network_type': 'str',
        'project_name': 'str',
        'region_id': 'str',
        'replicas': 'int',
        'server_cpu': 'int',
        'shard_capacity': 'int',
        'shard_count': 'int',
        'total_capacity': 'int',
        'used_capacity': 'int',
        'vpc_info': 'VpcInfoForDescribeBackupsOutput',
        'zone_ids': 'list[str]'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'arch_type': 'ArchType',
        'charge_type': 'ChargeType',
        'engine_version': 'EngineVersion',
        'instance_id': 'InstanceId',
        'instance_name': 'InstanceName',
        'maintenance_time': 'MaintenanceTime',
        'network_type': 'NetworkType',
        'project_name': 'ProjectName',
        'region_id': 'RegionId',
        'replicas': 'Replicas',
        'server_cpu': 'ServerCpu',
        'shard_capacity': 'ShardCapacity',
        'shard_count': 'ShardCount',
        'total_capacity': 'TotalCapacity',
        'used_capacity': 'UsedCapacity',
        'vpc_info': 'VpcInfo',
        'zone_ids': 'ZoneIds'
    }

    def __init__(self, account_id=None, arch_type=None, charge_type=None, engine_version=None, instance_id=None, instance_name=None, maintenance_time=None, network_type=None, project_name=None, region_id=None, replicas=None, server_cpu=None, shard_capacity=None, shard_count=None, total_capacity=None, used_capacity=None, vpc_info=None, zone_ids=None, _configuration=None):  # noqa: E501
        """InstanceDetailForDescribeBackupsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._arch_type = None
        self._charge_type = None
        self._engine_version = None
        self._instance_id = None
        self._instance_name = None
        self._maintenance_time = None
        self._network_type = None
        self._project_name = None
        self._region_id = None
        self._replicas = None
        self._server_cpu = None
        self._shard_capacity = None
        self._shard_count = None
        self._total_capacity = None
        self._used_capacity = None
        self._vpc_info = None
        self._zone_ids = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if arch_type is not None:
            self.arch_type = arch_type
        if charge_type is not None:
            self.charge_type = charge_type
        if engine_version is not None:
            self.engine_version = engine_version
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if maintenance_time is not None:
            self.maintenance_time = maintenance_time
        if network_type is not None:
            self.network_type = network_type
        if project_name is not None:
            self.project_name = project_name
        if region_id is not None:
            self.region_id = region_id
        if replicas is not None:
            self.replicas = replicas
        if server_cpu is not None:
            self.server_cpu = server_cpu
        if shard_capacity is not None:
            self.shard_capacity = shard_capacity
        if shard_count is not None:
            self.shard_count = shard_count
        if total_capacity is not None:
            self.total_capacity = total_capacity
        if used_capacity is not None:
            self.used_capacity = used_capacity
        if vpc_info is not None:
            self.vpc_info = vpc_info
        if zone_ids is not None:
            self.zone_ids = zone_ids

    @property
    def account_id(self):
        """Gets the account_id of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501


        :return: The account_id of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this InstanceDetailForDescribeBackupsOutput.


        :param account_id: The account_id of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def arch_type(self):
        """Gets the arch_type of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501


        :return: The arch_type of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._arch_type

    @arch_type.setter
    def arch_type(self, arch_type):
        """Sets the arch_type of this InstanceDetailForDescribeBackupsOutput.


        :param arch_type: The arch_type of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :type: str
        """

        self._arch_type = arch_type

    @property
    def charge_type(self):
        """Gets the charge_type of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501


        :return: The charge_type of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this InstanceDetailForDescribeBackupsOutput.


        :param charge_type: The charge_type of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :type: str
        """

        self._charge_type = charge_type

    @property
    def engine_version(self):
        """Gets the engine_version of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501


        :return: The engine_version of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this InstanceDetailForDescribeBackupsOutput.


        :param engine_version: The engine_version of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :type: str
        """

        self._engine_version = engine_version

    @property
    def instance_id(self):
        """Gets the instance_id of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501


        :return: The instance_id of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InstanceDetailForDescribeBackupsOutput.


        :param instance_id: The instance_id of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501


        :return: The instance_name of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this InstanceDetailForDescribeBackupsOutput.


        :param instance_name: The instance_name of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def maintenance_time(self):
        """Gets the maintenance_time of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501


        :return: The maintenance_time of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._maintenance_time

    @maintenance_time.setter
    def maintenance_time(self, maintenance_time):
        """Sets the maintenance_time of this InstanceDetailForDescribeBackupsOutput.


        :param maintenance_time: The maintenance_time of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :type: str
        """

        self._maintenance_time = maintenance_time

    @property
    def network_type(self):
        """Gets the network_type of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501


        :return: The network_type of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """Sets the network_type of this InstanceDetailForDescribeBackupsOutput.


        :param network_type: The network_type of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :type: str
        """

        self._network_type = network_type

    @property
    def project_name(self):
        """Gets the project_name of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501


        :return: The project_name of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this InstanceDetailForDescribeBackupsOutput.


        :param project_name: The project_name of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def region_id(self):
        """Gets the region_id of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501


        :return: The region_id of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this InstanceDetailForDescribeBackupsOutput.


        :param region_id: The region_id of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :type: str
        """

        self._region_id = region_id

    @property
    def replicas(self):
        """Gets the replicas of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501


        :return: The replicas of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this InstanceDetailForDescribeBackupsOutput.


        :param replicas: The replicas of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :type: int
        """

        self._replicas = replicas

    @property
    def server_cpu(self):
        """Gets the server_cpu of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501


        :return: The server_cpu of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._server_cpu

    @server_cpu.setter
    def server_cpu(self, server_cpu):
        """Sets the server_cpu of this InstanceDetailForDescribeBackupsOutput.


        :param server_cpu: The server_cpu of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :type: int
        """

        self._server_cpu = server_cpu

    @property
    def shard_capacity(self):
        """Gets the shard_capacity of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501


        :return: The shard_capacity of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._shard_capacity

    @shard_capacity.setter
    def shard_capacity(self, shard_capacity):
        """Sets the shard_capacity of this InstanceDetailForDescribeBackupsOutput.


        :param shard_capacity: The shard_capacity of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :type: int
        """

        self._shard_capacity = shard_capacity

    @property
    def shard_count(self):
        """Gets the shard_count of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501


        :return: The shard_count of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._shard_count

    @shard_count.setter
    def shard_count(self, shard_count):
        """Sets the shard_count of this InstanceDetailForDescribeBackupsOutput.


        :param shard_count: The shard_count of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :type: int
        """

        self._shard_count = shard_count

    @property
    def total_capacity(self):
        """Gets the total_capacity of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501


        :return: The total_capacity of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._total_capacity

    @total_capacity.setter
    def total_capacity(self, total_capacity):
        """Sets the total_capacity of this InstanceDetailForDescribeBackupsOutput.


        :param total_capacity: The total_capacity of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :type: int
        """

        self._total_capacity = total_capacity

    @property
    def used_capacity(self):
        """Gets the used_capacity of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501


        :return: The used_capacity of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :rtype: int
        """
        return self._used_capacity

    @used_capacity.setter
    def used_capacity(self, used_capacity):
        """Sets the used_capacity of this InstanceDetailForDescribeBackupsOutput.


        :param used_capacity: The used_capacity of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :type: int
        """

        self._used_capacity = used_capacity

    @property
    def vpc_info(self):
        """Gets the vpc_info of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501


        :return: The vpc_info of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :rtype: VpcInfoForDescribeBackupsOutput
        """
        return self._vpc_info

    @vpc_info.setter
    def vpc_info(self, vpc_info):
        """Sets the vpc_info of this InstanceDetailForDescribeBackupsOutput.


        :param vpc_info: The vpc_info of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :type: VpcInfoForDescribeBackupsOutput
        """

        self._vpc_info = vpc_info

    @property
    def zone_ids(self):
        """Gets the zone_ids of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501


        :return: The zone_ids of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._zone_ids

    @zone_ids.setter
    def zone_ids(self, zone_ids):
        """Sets the zone_ids of this InstanceDetailForDescribeBackupsOutput.


        :param zone_ids: The zone_ids of this InstanceDetailForDescribeBackupsOutput.  # noqa: E501
        :type: list[str]
        """

        self._zone_ids = zone_ids

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
        if issubclass(InstanceDetailForDescribeBackupsOutput, dict):
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
        if not isinstance(other, InstanceDetailForDescribeBackupsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstanceDetailForDescribeBackupsOutput):
            return True

        return self.to_dict() != other.to_dict()