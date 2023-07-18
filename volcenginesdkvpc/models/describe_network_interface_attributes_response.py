# coding: utf-8

"""
    vpc

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeNetworkInterfaceAttributesResponse(object):
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
        'account_id': 'str',
        'associated_elastic_ip': 'AssociatedElasticIpForDescribeNetworkInterfaceAttributesOutput',
        'created_at': 'str',
        'description': 'str',
        'device_id': 'str',
        'ipv6_sets': 'list[str]',
        'mac_address': 'str',
        'network_interface_id': 'str',
        'network_interface_name': 'str',
        'port_security_enabled': 'bool',
        'primary_ip_address': 'str',
        'private_ip_sets': 'PrivateIpSetsForDescribeNetworkInterfaceAttributesOutput',
        'project_name': 'str',
        'request_id': 'str',
        'security_group_ids': 'list[str]',
        'service_managed': 'bool',
        'status': 'str',
        'subnet_id': 'str',
        'tags': 'list[TagForDescribeNetworkInterfaceAttributesOutput]',
        'type': 'str',
        'updated_at': 'str',
        'vpc_id': 'str',
        'vpc_name': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'associated_elastic_ip': 'AssociatedElasticIp',
        'created_at': 'CreatedAt',
        'description': 'Description',
        'device_id': 'DeviceId',
        'ipv6_sets': 'IPv6Sets',
        'mac_address': 'MacAddress',
        'network_interface_id': 'NetworkInterfaceId',
        'network_interface_name': 'NetworkInterfaceName',
        'port_security_enabled': 'PortSecurityEnabled',
        'primary_ip_address': 'PrimaryIpAddress',
        'private_ip_sets': 'PrivateIpSets',
        'project_name': 'ProjectName',
        'request_id': 'RequestId',
        'security_group_ids': 'SecurityGroupIds',
        'service_managed': 'ServiceManaged',
        'status': 'Status',
        'subnet_id': 'SubnetId',
        'tags': 'Tags',
        'type': 'Type',
        'updated_at': 'UpdatedAt',
        'vpc_id': 'VpcId',
        'vpc_name': 'VpcName',
        'zone_id': 'ZoneId'
    }

    def __init__(self, account_id=None, associated_elastic_ip=None, created_at=None, description=None, device_id=None, ipv6_sets=None, mac_address=None, network_interface_id=None, network_interface_name=None, port_security_enabled=None, primary_ip_address=None, private_ip_sets=None, project_name=None, request_id=None, security_group_ids=None, service_managed=None, status=None, subnet_id=None, tags=None, type=None, updated_at=None, vpc_id=None, vpc_name=None, zone_id=None, _configuration=None):  # noqa: E501
        """DescribeNetworkInterfaceAttributesResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._associated_elastic_ip = None
        self._created_at = None
        self._description = None
        self._device_id = None
        self._ipv6_sets = None
        self._mac_address = None
        self._network_interface_id = None
        self._network_interface_name = None
        self._port_security_enabled = None
        self._primary_ip_address = None
        self._private_ip_sets = None
        self._project_name = None
        self._request_id = None
        self._security_group_ids = None
        self._service_managed = None
        self._status = None
        self._subnet_id = None
        self._tags = None
        self._type = None
        self._updated_at = None
        self._vpc_id = None
        self._vpc_name = None
        self._zone_id = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if associated_elastic_ip is not None:
            self.associated_elastic_ip = associated_elastic_ip
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if device_id is not None:
            self.device_id = device_id
        if ipv6_sets is not None:
            self.ipv6_sets = ipv6_sets
        if mac_address is not None:
            self.mac_address = mac_address
        if network_interface_id is not None:
            self.network_interface_id = network_interface_id
        if network_interface_name is not None:
            self.network_interface_name = network_interface_name
        if port_security_enabled is not None:
            self.port_security_enabled = port_security_enabled
        if primary_ip_address is not None:
            self.primary_ip_address = primary_ip_address
        if private_ip_sets is not None:
            self.private_ip_sets = private_ip_sets
        if project_name is not None:
            self.project_name = project_name
        if request_id is not None:
            self.request_id = request_id
        if security_group_ids is not None:
            self.security_group_ids = security_group_ids
        if service_managed is not None:
            self.service_managed = service_managed
        if status is not None:
            self.status = status
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if tags is not None:
            self.tags = tags
        if type is not None:
            self.type = type
        if updated_at is not None:
            self.updated_at = updated_at
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if vpc_name is not None:
            self.vpc_name = vpc_name
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def account_id(self):
        """Gets the account_id of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501


        :return: The account_id of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this DescribeNetworkInterfaceAttributesResponse.


        :param account_id: The account_id of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def associated_elastic_ip(self):
        """Gets the associated_elastic_ip of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501


        :return: The associated_elastic_ip of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :rtype: AssociatedElasticIpForDescribeNetworkInterfaceAttributesOutput
        """
        return self._associated_elastic_ip

    @associated_elastic_ip.setter
    def associated_elastic_ip(self, associated_elastic_ip):
        """Sets the associated_elastic_ip of this DescribeNetworkInterfaceAttributesResponse.


        :param associated_elastic_ip: The associated_elastic_ip of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :type: AssociatedElasticIpForDescribeNetworkInterfaceAttributesOutput
        """

        self._associated_elastic_ip = associated_elastic_ip

    @property
    def created_at(self):
        """Gets the created_at of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501


        :return: The created_at of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DescribeNetworkInterfaceAttributesResponse.


        :param created_at: The created_at of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501


        :return: The description of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DescribeNetworkInterfaceAttributesResponse.


        :param description: The description of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def device_id(self):
        """Gets the device_id of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501


        :return: The device_id of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this DescribeNetworkInterfaceAttributesResponse.


        :param device_id: The device_id of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def ipv6_sets(self):
        """Gets the ipv6_sets of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501


        :return: The ipv6_sets of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._ipv6_sets

    @ipv6_sets.setter
    def ipv6_sets(self, ipv6_sets):
        """Sets the ipv6_sets of this DescribeNetworkInterfaceAttributesResponse.


        :param ipv6_sets: The ipv6_sets of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :type: list[str]
        """

        self._ipv6_sets = ipv6_sets

    @property
    def mac_address(self):
        """Gets the mac_address of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501


        :return: The mac_address of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this DescribeNetworkInterfaceAttributesResponse.


        :param mac_address: The mac_address of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def network_interface_id(self):
        """Gets the network_interface_id of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501


        :return: The network_interface_id of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._network_interface_id

    @network_interface_id.setter
    def network_interface_id(self, network_interface_id):
        """Sets the network_interface_id of this DescribeNetworkInterfaceAttributesResponse.


        :param network_interface_id: The network_interface_id of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :type: str
        """

        self._network_interface_id = network_interface_id

    @property
    def network_interface_name(self):
        """Gets the network_interface_name of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501


        :return: The network_interface_name of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._network_interface_name

    @network_interface_name.setter
    def network_interface_name(self, network_interface_name):
        """Sets the network_interface_name of this DescribeNetworkInterfaceAttributesResponse.


        :param network_interface_name: The network_interface_name of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :type: str
        """

        self._network_interface_name = network_interface_name

    @property
    def port_security_enabled(self):
        """Gets the port_security_enabled of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501


        :return: The port_security_enabled of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :rtype: bool
        """
        return self._port_security_enabled

    @port_security_enabled.setter
    def port_security_enabled(self, port_security_enabled):
        """Sets the port_security_enabled of this DescribeNetworkInterfaceAttributesResponse.


        :param port_security_enabled: The port_security_enabled of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :type: bool
        """

        self._port_security_enabled = port_security_enabled

    @property
    def primary_ip_address(self):
        """Gets the primary_ip_address of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501


        :return: The primary_ip_address of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._primary_ip_address

    @primary_ip_address.setter
    def primary_ip_address(self, primary_ip_address):
        """Sets the primary_ip_address of this DescribeNetworkInterfaceAttributesResponse.


        :param primary_ip_address: The primary_ip_address of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :type: str
        """

        self._primary_ip_address = primary_ip_address

    @property
    def private_ip_sets(self):
        """Gets the private_ip_sets of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501


        :return: The private_ip_sets of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :rtype: PrivateIpSetsForDescribeNetworkInterfaceAttributesOutput
        """
        return self._private_ip_sets

    @private_ip_sets.setter
    def private_ip_sets(self, private_ip_sets):
        """Sets the private_ip_sets of this DescribeNetworkInterfaceAttributesResponse.


        :param private_ip_sets: The private_ip_sets of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :type: PrivateIpSetsForDescribeNetworkInterfaceAttributesOutput
        """

        self._private_ip_sets = private_ip_sets

    @property
    def project_name(self):
        """Gets the project_name of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501


        :return: The project_name of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeNetworkInterfaceAttributesResponse.


        :param project_name: The project_name of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def request_id(self):
        """Gets the request_id of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501


        :return: The request_id of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this DescribeNetworkInterfaceAttributesResponse.


        :param request_id: The request_id of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def security_group_ids(self):
        """Gets the security_group_ids of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501


        :return: The security_group_ids of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._security_group_ids

    @security_group_ids.setter
    def security_group_ids(self, security_group_ids):
        """Sets the security_group_ids of this DescribeNetworkInterfaceAttributesResponse.


        :param security_group_ids: The security_group_ids of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :type: list[str]
        """

        self._security_group_ids = security_group_ids

    @property
    def service_managed(self):
        """Gets the service_managed of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501


        :return: The service_managed of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :rtype: bool
        """
        return self._service_managed

    @service_managed.setter
    def service_managed(self, service_managed):
        """Sets the service_managed of this DescribeNetworkInterfaceAttributesResponse.


        :param service_managed: The service_managed of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :type: bool
        """

        self._service_managed = service_managed

    @property
    def status(self):
        """Gets the status of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501


        :return: The status of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DescribeNetworkInterfaceAttributesResponse.


        :param status: The status of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def subnet_id(self):
        """Gets the subnet_id of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501


        :return: The subnet_id of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this DescribeNetworkInterfaceAttributesResponse.


        :param subnet_id: The subnet_id of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

    @property
    def tags(self):
        """Gets the tags of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501


        :return: The tags of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :rtype: list[TagForDescribeNetworkInterfaceAttributesOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DescribeNetworkInterfaceAttributesResponse.


        :param tags: The tags of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :type: list[TagForDescribeNetworkInterfaceAttributesOutput]
        """

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501


        :return: The type of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DescribeNetworkInterfaceAttributesResponse.


        :param type: The type of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def updated_at(self):
        """Gets the updated_at of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501


        :return: The updated_at of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DescribeNetworkInterfaceAttributesResponse.


        :param updated_at: The updated_at of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def vpc_id(self):
        """Gets the vpc_id of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501


        :return: The vpc_id of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this DescribeNetworkInterfaceAttributesResponse.


        :param vpc_id: The vpc_id of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

    @property
    def vpc_name(self):
        """Gets the vpc_name of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501


        :return: The vpc_name of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        """Sets the vpc_name of this DescribeNetworkInterfaceAttributesResponse.


        :param vpc_name: The vpc_name of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :type: str
        """

        self._vpc_name = vpc_name

    @property
    def zone_id(self):
        """Gets the zone_id of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501


        :return: The zone_id of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this DescribeNetworkInterfaceAttributesResponse.


        :param zone_id: The zone_id of this DescribeNetworkInterfaceAttributesResponse.  # noqa: E501
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
        if issubclass(DescribeNetworkInterfaceAttributesResponse, dict):
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
        if not isinstance(other, DescribeNetworkInterfaceAttributesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeNetworkInterfaceAttributesResponse):
            return True

        return self.to_dict() != other.to_dict()
