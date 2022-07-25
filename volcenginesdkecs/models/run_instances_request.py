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


class RunInstancesRequest(object):
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
        'auto_renew': 'bool',
        'auto_renew_period': 'int',
        'client_token': 'str',
        'count': 'int',
        'credit_specification': 'str',
        'description': 'str',
        'dry_run': 'bool',
        'host_name': 'str',
        'hpc_cluster_id': 'str',
        'image_id': 'str',
        'instance_charge_type': 'str',
        'instance_name': 'str',
        'instance_type': 'str',
        'instance_type_id': 'str',
        'key_pair_name': 'str',
        'min_count': 'int',
        'network_interfaces': 'list[NetworkInterfaceForRunInstancesInput]',
        'password': 'str',
        'period': 'int',
        'period_unit': 'str',
        'security_enhancement_strategy': 'str',
        'suffix_index': 'int',
        'unique_suffix': 'bool',
        'user_data': 'str',
        'volumes': 'list[VolumeForRunInstancesInput]',
        'zone_id': 'str'
    }

    attribute_map = {
        'auto_renew': 'AutoRenew',
        'auto_renew_period': 'AutoRenewPeriod',
        'client_token': 'ClientToken',
        'count': 'Count',
        'credit_specification': 'CreditSpecification',
        'description': 'Description',
        'dry_run': 'DryRun',
        'host_name': 'HostName',
        'hpc_cluster_id': 'HpcClusterId',
        'image_id': 'ImageId',
        'instance_charge_type': 'InstanceChargeType',
        'instance_name': 'InstanceName',
        'instance_type': 'InstanceType',
        'instance_type_id': 'InstanceTypeId',
        'key_pair_name': 'KeyPairName',
        'min_count': 'MinCount',
        'network_interfaces': 'NetworkInterfaces',
        'password': 'Password',
        'period': 'Period',
        'period_unit': 'PeriodUnit',
        'security_enhancement_strategy': 'SecurityEnhancementStrategy',
        'suffix_index': 'SuffixIndex',
        'unique_suffix': 'UniqueSuffix',
        'user_data': 'UserData',
        'volumes': 'Volumes',
        'zone_id': 'ZoneId'
    }

    def __init__(self, auto_renew=None, auto_renew_period=None, client_token=None, count=None, credit_specification=None, description=None, dry_run=None, host_name=None, hpc_cluster_id=None, image_id=None, instance_charge_type=None, instance_name=None, instance_type=None, instance_type_id=None, key_pair_name=None, min_count=None, network_interfaces=None, password=None, period=None, period_unit=None, security_enhancement_strategy=None, suffix_index=None, unique_suffix=None, user_data=None, volumes=None, zone_id=None, _configuration=None):  # noqa: E501
        """RunInstancesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_renew = None
        self._auto_renew_period = None
        self._client_token = None
        self._count = None
        self._credit_specification = None
        self._description = None
        self._dry_run = None
        self._host_name = None
        self._hpc_cluster_id = None
        self._image_id = None
        self._instance_charge_type = None
        self._instance_name = None
        self._instance_type = None
        self._instance_type_id = None
        self._key_pair_name = None
        self._min_count = None
        self._network_interfaces = None
        self._password = None
        self._period = None
        self._period_unit = None
        self._security_enhancement_strategy = None
        self._suffix_index = None
        self._unique_suffix = None
        self._user_data = None
        self._volumes = None
        self._zone_id = None
        self.discriminator = None

        if auto_renew is not None:
            self.auto_renew = auto_renew
        if auto_renew_period is not None:
            self.auto_renew_period = auto_renew_period
        if client_token is not None:
            self.client_token = client_token
        if count is not None:
            self.count = count
        if credit_specification is not None:
            self.credit_specification = credit_specification
        if description is not None:
            self.description = description
        if dry_run is not None:
            self.dry_run = dry_run
        if host_name is not None:
            self.host_name = host_name
        if hpc_cluster_id is not None:
            self.hpc_cluster_id = hpc_cluster_id
        if image_id is not None:
            self.image_id = image_id
        if instance_charge_type is not None:
            self.instance_charge_type = instance_charge_type
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_type is not None:
            self.instance_type = instance_type
        if instance_type_id is not None:
            self.instance_type_id = instance_type_id
        if key_pair_name is not None:
            self.key_pair_name = key_pair_name
        if min_count is not None:
            self.min_count = min_count
        if network_interfaces is not None:
            self.network_interfaces = network_interfaces
        if password is not None:
            self.password = password
        if period is not None:
            self.period = period
        if period_unit is not None:
            self.period_unit = period_unit
        if security_enhancement_strategy is not None:
            self.security_enhancement_strategy = security_enhancement_strategy
        if suffix_index is not None:
            self.suffix_index = suffix_index
        if unique_suffix is not None:
            self.unique_suffix = unique_suffix
        if user_data is not None:
            self.user_data = user_data
        if volumes is not None:
            self.volumes = volumes
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def auto_renew(self):
        """Gets the auto_renew of this RunInstancesRequest.  # noqa: E501


        :return: The auto_renew of this RunInstancesRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this RunInstancesRequest.


        :param auto_renew: The auto_renew of this RunInstancesRequest.  # noqa: E501
        :type: bool
        """

        self._auto_renew = auto_renew

    @property
    def auto_renew_period(self):
        """Gets the auto_renew_period of this RunInstancesRequest.  # noqa: E501


        :return: The auto_renew_period of this RunInstancesRequest.  # noqa: E501
        :rtype: int
        """
        return self._auto_renew_period

    @auto_renew_period.setter
    def auto_renew_period(self, auto_renew_period):
        """Sets the auto_renew_period of this RunInstancesRequest.


        :param auto_renew_period: The auto_renew_period of this RunInstancesRequest.  # noqa: E501
        :type: int
        """

        self._auto_renew_period = auto_renew_period

    @property
    def client_token(self):
        """Gets the client_token of this RunInstancesRequest.  # noqa: E501


        :return: The client_token of this RunInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this RunInstancesRequest.


        :param client_token: The client_token of this RunInstancesRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def count(self):
        """Gets the count of this RunInstancesRequest.  # noqa: E501


        :return: The count of this RunInstancesRequest.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this RunInstancesRequest.


        :param count: The count of this RunInstancesRequest.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def credit_specification(self):
        """Gets the credit_specification of this RunInstancesRequest.  # noqa: E501


        :return: The credit_specification of this RunInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._credit_specification

    @credit_specification.setter
    def credit_specification(self, credit_specification):
        """Sets the credit_specification of this RunInstancesRequest.


        :param credit_specification: The credit_specification of this RunInstancesRequest.  # noqa: E501
        :type: str
        """

        self._credit_specification = credit_specification

    @property
    def description(self):
        """Gets the description of this RunInstancesRequest.  # noqa: E501


        :return: The description of this RunInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RunInstancesRequest.


        :param description: The description of this RunInstancesRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def dry_run(self):
        """Gets the dry_run of this RunInstancesRequest.  # noqa: E501


        :return: The dry_run of this RunInstancesRequest.  # noqa: E501
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this RunInstancesRequest.


        :param dry_run: The dry_run of this RunInstancesRequest.  # noqa: E501
        :type: bool
        """

        self._dry_run = dry_run

    @property
    def host_name(self):
        """Gets the host_name of this RunInstancesRequest.  # noqa: E501


        :return: The host_name of this RunInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this RunInstancesRequest.


        :param host_name: The host_name of this RunInstancesRequest.  # noqa: E501
        :type: str
        """

        self._host_name = host_name

    @property
    def hpc_cluster_id(self):
        """Gets the hpc_cluster_id of this RunInstancesRequest.  # noqa: E501


        :return: The hpc_cluster_id of this RunInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._hpc_cluster_id

    @hpc_cluster_id.setter
    def hpc_cluster_id(self, hpc_cluster_id):
        """Sets the hpc_cluster_id of this RunInstancesRequest.


        :param hpc_cluster_id: The hpc_cluster_id of this RunInstancesRequest.  # noqa: E501
        :type: str
        """

        self._hpc_cluster_id = hpc_cluster_id

    @property
    def image_id(self):
        """Gets the image_id of this RunInstancesRequest.  # noqa: E501


        :return: The image_id of this RunInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this RunInstancesRequest.


        :param image_id: The image_id of this RunInstancesRequest.  # noqa: E501
        :type: str
        """

        self._image_id = image_id

    @property
    def instance_charge_type(self):
        """Gets the instance_charge_type of this RunInstancesRequest.  # noqa: E501


        :return: The instance_charge_type of this RunInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_charge_type

    @instance_charge_type.setter
    def instance_charge_type(self, instance_charge_type):
        """Sets the instance_charge_type of this RunInstancesRequest.


        :param instance_charge_type: The instance_charge_type of this RunInstancesRequest.  # noqa: E501
        :type: str
        """

        self._instance_charge_type = instance_charge_type

    @property
    def instance_name(self):
        """Gets the instance_name of this RunInstancesRequest.  # noqa: E501


        :return: The instance_name of this RunInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this RunInstancesRequest.


        :param instance_name: The instance_name of this RunInstancesRequest.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def instance_type(self):
        """Gets the instance_type of this RunInstancesRequest.  # noqa: E501


        :return: The instance_type of this RunInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this RunInstancesRequest.


        :param instance_type: The instance_type of this RunInstancesRequest.  # noqa: E501
        :type: str
        """

        self._instance_type = instance_type

    @property
    def instance_type_id(self):
        """Gets the instance_type_id of this RunInstancesRequest.  # noqa: E501


        :return: The instance_type_id of this RunInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_type_id

    @instance_type_id.setter
    def instance_type_id(self, instance_type_id):
        """Sets the instance_type_id of this RunInstancesRequest.


        :param instance_type_id: The instance_type_id of this RunInstancesRequest.  # noqa: E501
        :type: str
        """

        self._instance_type_id = instance_type_id

    @property
    def key_pair_name(self):
        """Gets the key_pair_name of this RunInstancesRequest.  # noqa: E501


        :return: The key_pair_name of this RunInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._key_pair_name

    @key_pair_name.setter
    def key_pair_name(self, key_pair_name):
        """Sets the key_pair_name of this RunInstancesRequest.


        :param key_pair_name: The key_pair_name of this RunInstancesRequest.  # noqa: E501
        :type: str
        """

        self._key_pair_name = key_pair_name

    @property
    def min_count(self):
        """Gets the min_count of this RunInstancesRequest.  # noqa: E501


        :return: The min_count of this RunInstancesRequest.  # noqa: E501
        :rtype: int
        """
        return self._min_count

    @min_count.setter
    def min_count(self, min_count):
        """Sets the min_count of this RunInstancesRequest.


        :param min_count: The min_count of this RunInstancesRequest.  # noqa: E501
        :type: int
        """

        self._min_count = min_count

    @property
    def network_interfaces(self):
        """Gets the network_interfaces of this RunInstancesRequest.  # noqa: E501


        :return: The network_interfaces of this RunInstancesRequest.  # noqa: E501
        :rtype: list[NetworkInterfaceForRunInstancesInput]
        """
        return self._network_interfaces

    @network_interfaces.setter
    def network_interfaces(self, network_interfaces):
        """Sets the network_interfaces of this RunInstancesRequest.


        :param network_interfaces: The network_interfaces of this RunInstancesRequest.  # noqa: E501
        :type: list[NetworkInterfaceForRunInstancesInput]
        """

        self._network_interfaces = network_interfaces

    @property
    def password(self):
        """Gets the password of this RunInstancesRequest.  # noqa: E501


        :return: The password of this RunInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this RunInstancesRequest.


        :param password: The password of this RunInstancesRequest.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def period(self):
        """Gets the period of this RunInstancesRequest.  # noqa: E501


        :return: The period of this RunInstancesRequest.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this RunInstancesRequest.


        :param period: The period of this RunInstancesRequest.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def period_unit(self):
        """Gets the period_unit of this RunInstancesRequest.  # noqa: E501


        :return: The period_unit of this RunInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._period_unit

    @period_unit.setter
    def period_unit(self, period_unit):
        """Sets the period_unit of this RunInstancesRequest.


        :param period_unit: The period_unit of this RunInstancesRequest.  # noqa: E501
        :type: str
        """

        self._period_unit = period_unit

    @property
    def security_enhancement_strategy(self):
        """Gets the security_enhancement_strategy of this RunInstancesRequest.  # noqa: E501


        :return: The security_enhancement_strategy of this RunInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._security_enhancement_strategy

    @security_enhancement_strategy.setter
    def security_enhancement_strategy(self, security_enhancement_strategy):
        """Sets the security_enhancement_strategy of this RunInstancesRequest.


        :param security_enhancement_strategy: The security_enhancement_strategy of this RunInstancesRequest.  # noqa: E501
        :type: str
        """

        self._security_enhancement_strategy = security_enhancement_strategy

    @property
    def suffix_index(self):
        """Gets the suffix_index of this RunInstancesRequest.  # noqa: E501


        :return: The suffix_index of this RunInstancesRequest.  # noqa: E501
        :rtype: int
        """
        return self._suffix_index

    @suffix_index.setter
    def suffix_index(self, suffix_index):
        """Sets the suffix_index of this RunInstancesRequest.


        :param suffix_index: The suffix_index of this RunInstancesRequest.  # noqa: E501
        :type: int
        """

        self._suffix_index = suffix_index

    @property
    def unique_suffix(self):
        """Gets the unique_suffix of this RunInstancesRequest.  # noqa: E501


        :return: The unique_suffix of this RunInstancesRequest.  # noqa: E501
        :rtype: bool
        """
        return self._unique_suffix

    @unique_suffix.setter
    def unique_suffix(self, unique_suffix):
        """Sets the unique_suffix of this RunInstancesRequest.


        :param unique_suffix: The unique_suffix of this RunInstancesRequest.  # noqa: E501
        :type: bool
        """

        self._unique_suffix = unique_suffix

    @property
    def user_data(self):
        """Gets the user_data of this RunInstancesRequest.  # noqa: E501


        :return: The user_data of this RunInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this RunInstancesRequest.


        :param user_data: The user_data of this RunInstancesRequest.  # noqa: E501
        :type: str
        """

        self._user_data = user_data

    @property
    def volumes(self):
        """Gets the volumes of this RunInstancesRequest.  # noqa: E501


        :return: The volumes of this RunInstancesRequest.  # noqa: E501
        :rtype: list[VolumeForRunInstancesInput]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this RunInstancesRequest.


        :param volumes: The volumes of this RunInstancesRequest.  # noqa: E501
        :type: list[VolumeForRunInstancesInput]
        """

        self._volumes = volumes

    @property
    def zone_id(self):
        """Gets the zone_id of this RunInstancesRequest.  # noqa: E501


        :return: The zone_id of this RunInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this RunInstancesRequest.


        :param zone_id: The zone_id of this RunInstancesRequest.  # noqa: E501
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
        if issubclass(RunInstancesRequest, dict):
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
        if not isinstance(other, RunInstancesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RunInstancesRequest):
            return True

        return self.to_dict() != other.to_dict()