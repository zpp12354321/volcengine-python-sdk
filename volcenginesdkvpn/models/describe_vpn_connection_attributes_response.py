# coding: utf-8

"""
    vpn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeVpnConnectionAttributesResponse(object):
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
        'attach_status': 'str',
        'attach_type': 'str',
        'business_status': 'str',
        'connect_status': 'str',
        'creation_time': 'str',
        'customer_gateway_id': 'str',
        'deleted_time': 'str',
        'description': 'str',
        'dpd_action': 'str',
        'ike_config': 'IkeConfigForDescribeVpnConnectionAttributesOutput',
        'ip_address': 'str',
        'ipsec_config': 'IpsecConfigForDescribeVpnConnectionAttributesOutput',
        'local_subnet': 'list[str]',
        'log_enabled': 'bool',
        'nat_traversal': 'bool',
        'negotiate_instantly': 'bool',
        'overdue_time': 'str',
        'project_name': 'str',
        'remote_subnet': 'list[str]',
        'request_id': 'str',
        'status': 'str',
        'transit_router_id': 'str',
        'update_time': 'str',
        'vpn_connection_id': 'str',
        'vpn_connection_name': 'str',
        'vpn_gateway_id': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'attach_status': 'AttachStatus',
        'attach_type': 'AttachType',
        'business_status': 'BusinessStatus',
        'connect_status': 'ConnectStatus',
        'creation_time': 'CreationTime',
        'customer_gateway_id': 'CustomerGatewayId',
        'deleted_time': 'DeletedTime',
        'description': 'Description',
        'dpd_action': 'DpdAction',
        'ike_config': 'IkeConfig',
        'ip_address': 'IpAddress',
        'ipsec_config': 'IpsecConfig',
        'local_subnet': 'LocalSubnet',
        'log_enabled': 'LogEnabled',
        'nat_traversal': 'NatTraversal',
        'negotiate_instantly': 'NegotiateInstantly',
        'overdue_time': 'OverdueTime',
        'project_name': 'ProjectName',
        'remote_subnet': 'RemoteSubnet',
        'request_id': 'RequestId',
        'status': 'Status',
        'transit_router_id': 'TransitRouterId',
        'update_time': 'UpdateTime',
        'vpn_connection_id': 'VpnConnectionId',
        'vpn_connection_name': 'VpnConnectionName',
        'vpn_gateway_id': 'VpnGatewayId',
        'zone_id': 'ZoneId'
    }

    def __init__(self, account_id=None, attach_status=None, attach_type=None, business_status=None, connect_status=None, creation_time=None, customer_gateway_id=None, deleted_time=None, description=None, dpd_action=None, ike_config=None, ip_address=None, ipsec_config=None, local_subnet=None, log_enabled=None, nat_traversal=None, negotiate_instantly=None, overdue_time=None, project_name=None, remote_subnet=None, request_id=None, status=None, transit_router_id=None, update_time=None, vpn_connection_id=None, vpn_connection_name=None, vpn_gateway_id=None, zone_id=None, _configuration=None):  # noqa: E501
        """DescribeVpnConnectionAttributesResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._attach_status = None
        self._attach_type = None
        self._business_status = None
        self._connect_status = None
        self._creation_time = None
        self._customer_gateway_id = None
        self._deleted_time = None
        self._description = None
        self._dpd_action = None
        self._ike_config = None
        self._ip_address = None
        self._ipsec_config = None
        self._local_subnet = None
        self._log_enabled = None
        self._nat_traversal = None
        self._negotiate_instantly = None
        self._overdue_time = None
        self._project_name = None
        self._remote_subnet = None
        self._request_id = None
        self._status = None
        self._transit_router_id = None
        self._update_time = None
        self._vpn_connection_id = None
        self._vpn_connection_name = None
        self._vpn_gateway_id = None
        self._zone_id = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if attach_status is not None:
            self.attach_status = attach_status
        if attach_type is not None:
            self.attach_type = attach_type
        if business_status is not None:
            self.business_status = business_status
        if connect_status is not None:
            self.connect_status = connect_status
        if creation_time is not None:
            self.creation_time = creation_time
        if customer_gateway_id is not None:
            self.customer_gateway_id = customer_gateway_id
        if deleted_time is not None:
            self.deleted_time = deleted_time
        if description is not None:
            self.description = description
        if dpd_action is not None:
            self.dpd_action = dpd_action
        if ike_config is not None:
            self.ike_config = ike_config
        if ip_address is not None:
            self.ip_address = ip_address
        if ipsec_config is not None:
            self.ipsec_config = ipsec_config
        if local_subnet is not None:
            self.local_subnet = local_subnet
        if log_enabled is not None:
            self.log_enabled = log_enabled
        if nat_traversal is not None:
            self.nat_traversal = nat_traversal
        if negotiate_instantly is not None:
            self.negotiate_instantly = negotiate_instantly
        if overdue_time is not None:
            self.overdue_time = overdue_time
        if project_name is not None:
            self.project_name = project_name
        if remote_subnet is not None:
            self.remote_subnet = remote_subnet
        if request_id is not None:
            self.request_id = request_id
        if status is not None:
            self.status = status
        if transit_router_id is not None:
            self.transit_router_id = transit_router_id
        if update_time is not None:
            self.update_time = update_time
        if vpn_connection_id is not None:
            self.vpn_connection_id = vpn_connection_id
        if vpn_connection_name is not None:
            self.vpn_connection_name = vpn_connection_name
        if vpn_gateway_id is not None:
            self.vpn_gateway_id = vpn_gateway_id
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def account_id(self):
        """Gets the account_id of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The account_id of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this DescribeVpnConnectionAttributesResponse.


        :param account_id: The account_id of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def attach_status(self):
        """Gets the attach_status of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The attach_status of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._attach_status

    @attach_status.setter
    def attach_status(self, attach_status):
        """Sets the attach_status of this DescribeVpnConnectionAttributesResponse.


        :param attach_status: The attach_status of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: str
        """

        self._attach_status = attach_status

    @property
    def attach_type(self):
        """Gets the attach_type of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The attach_type of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._attach_type

    @attach_type.setter
    def attach_type(self, attach_type):
        """Sets the attach_type of this DescribeVpnConnectionAttributesResponse.


        :param attach_type: The attach_type of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: str
        """

        self._attach_type = attach_type

    @property
    def business_status(self):
        """Gets the business_status of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The business_status of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._business_status

    @business_status.setter
    def business_status(self, business_status):
        """Sets the business_status of this DescribeVpnConnectionAttributesResponse.


        :param business_status: The business_status of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: str
        """

        self._business_status = business_status

    @property
    def connect_status(self):
        """Gets the connect_status of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The connect_status of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._connect_status

    @connect_status.setter
    def connect_status(self, connect_status):
        """Sets the connect_status of this DescribeVpnConnectionAttributesResponse.


        :param connect_status: The connect_status of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: str
        """

        self._connect_status = connect_status

    @property
    def creation_time(self):
        """Gets the creation_time of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The creation_time of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this DescribeVpnConnectionAttributesResponse.


        :param creation_time: The creation_time of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def customer_gateway_id(self):
        """Gets the customer_gateway_id of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The customer_gateway_id of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._customer_gateway_id

    @customer_gateway_id.setter
    def customer_gateway_id(self, customer_gateway_id):
        """Sets the customer_gateway_id of this DescribeVpnConnectionAttributesResponse.


        :param customer_gateway_id: The customer_gateway_id of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: str
        """

        self._customer_gateway_id = customer_gateway_id

    @property
    def deleted_time(self):
        """Gets the deleted_time of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The deleted_time of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._deleted_time

    @deleted_time.setter
    def deleted_time(self, deleted_time):
        """Sets the deleted_time of this DescribeVpnConnectionAttributesResponse.


        :param deleted_time: The deleted_time of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: str
        """

        self._deleted_time = deleted_time

    @property
    def description(self):
        """Gets the description of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The description of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DescribeVpnConnectionAttributesResponse.


        :param description: The description of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def dpd_action(self):
        """Gets the dpd_action of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The dpd_action of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._dpd_action

    @dpd_action.setter
    def dpd_action(self, dpd_action):
        """Sets the dpd_action of this DescribeVpnConnectionAttributesResponse.


        :param dpd_action: The dpd_action of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: str
        """

        self._dpd_action = dpd_action

    @property
    def ike_config(self):
        """Gets the ike_config of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The ike_config of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: IkeConfigForDescribeVpnConnectionAttributesOutput
        """
        return self._ike_config

    @ike_config.setter
    def ike_config(self, ike_config):
        """Sets the ike_config of this DescribeVpnConnectionAttributesResponse.


        :param ike_config: The ike_config of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: IkeConfigForDescribeVpnConnectionAttributesOutput
        """

        self._ike_config = ike_config

    @property
    def ip_address(self):
        """Gets the ip_address of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The ip_address of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this DescribeVpnConnectionAttributesResponse.


        :param ip_address: The ip_address of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def ipsec_config(self):
        """Gets the ipsec_config of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The ipsec_config of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: IpsecConfigForDescribeVpnConnectionAttributesOutput
        """
        return self._ipsec_config

    @ipsec_config.setter
    def ipsec_config(self, ipsec_config):
        """Sets the ipsec_config of this DescribeVpnConnectionAttributesResponse.


        :param ipsec_config: The ipsec_config of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: IpsecConfigForDescribeVpnConnectionAttributesOutput
        """

        self._ipsec_config = ipsec_config

    @property
    def local_subnet(self):
        """Gets the local_subnet of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The local_subnet of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._local_subnet

    @local_subnet.setter
    def local_subnet(self, local_subnet):
        """Sets the local_subnet of this DescribeVpnConnectionAttributesResponse.


        :param local_subnet: The local_subnet of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: list[str]
        """

        self._local_subnet = local_subnet

    @property
    def log_enabled(self):
        """Gets the log_enabled of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The log_enabled of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: bool
        """
        return self._log_enabled

    @log_enabled.setter
    def log_enabled(self, log_enabled):
        """Sets the log_enabled of this DescribeVpnConnectionAttributesResponse.


        :param log_enabled: The log_enabled of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: bool
        """

        self._log_enabled = log_enabled

    @property
    def nat_traversal(self):
        """Gets the nat_traversal of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The nat_traversal of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: bool
        """
        return self._nat_traversal

    @nat_traversal.setter
    def nat_traversal(self, nat_traversal):
        """Sets the nat_traversal of this DescribeVpnConnectionAttributesResponse.


        :param nat_traversal: The nat_traversal of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: bool
        """

        self._nat_traversal = nat_traversal

    @property
    def negotiate_instantly(self):
        """Gets the negotiate_instantly of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The negotiate_instantly of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: bool
        """
        return self._negotiate_instantly

    @negotiate_instantly.setter
    def negotiate_instantly(self, negotiate_instantly):
        """Sets the negotiate_instantly of this DescribeVpnConnectionAttributesResponse.


        :param negotiate_instantly: The negotiate_instantly of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: bool
        """

        self._negotiate_instantly = negotiate_instantly

    @property
    def overdue_time(self):
        """Gets the overdue_time of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The overdue_time of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._overdue_time

    @overdue_time.setter
    def overdue_time(self, overdue_time):
        """Sets the overdue_time of this DescribeVpnConnectionAttributesResponse.


        :param overdue_time: The overdue_time of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: str
        """

        self._overdue_time = overdue_time

    @property
    def project_name(self):
        """Gets the project_name of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The project_name of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeVpnConnectionAttributesResponse.


        :param project_name: The project_name of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def remote_subnet(self):
        """Gets the remote_subnet of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The remote_subnet of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._remote_subnet

    @remote_subnet.setter
    def remote_subnet(self, remote_subnet):
        """Sets the remote_subnet of this DescribeVpnConnectionAttributesResponse.


        :param remote_subnet: The remote_subnet of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: list[str]
        """

        self._remote_subnet = remote_subnet

    @property
    def request_id(self):
        """Gets the request_id of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The request_id of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this DescribeVpnConnectionAttributesResponse.


        :param request_id: The request_id of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def status(self):
        """Gets the status of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The status of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DescribeVpnConnectionAttributesResponse.


        :param status: The status of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def transit_router_id(self):
        """Gets the transit_router_id of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The transit_router_id of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_id

    @transit_router_id.setter
    def transit_router_id(self, transit_router_id):
        """Sets the transit_router_id of this DescribeVpnConnectionAttributesResponse.


        :param transit_router_id: The transit_router_id of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: str
        """

        self._transit_router_id = transit_router_id

    @property
    def update_time(self):
        """Gets the update_time of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The update_time of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this DescribeVpnConnectionAttributesResponse.


        :param update_time: The update_time of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

    @property
    def vpn_connection_id(self):
        """Gets the vpn_connection_id of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The vpn_connection_id of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._vpn_connection_id

    @vpn_connection_id.setter
    def vpn_connection_id(self, vpn_connection_id):
        """Sets the vpn_connection_id of this DescribeVpnConnectionAttributesResponse.


        :param vpn_connection_id: The vpn_connection_id of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: str
        """

        self._vpn_connection_id = vpn_connection_id

    @property
    def vpn_connection_name(self):
        """Gets the vpn_connection_name of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The vpn_connection_name of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._vpn_connection_name

    @vpn_connection_name.setter
    def vpn_connection_name(self, vpn_connection_name):
        """Sets the vpn_connection_name of this DescribeVpnConnectionAttributesResponse.


        :param vpn_connection_name: The vpn_connection_name of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: str
        """

        self._vpn_connection_name = vpn_connection_name

    @property
    def vpn_gateway_id(self):
        """Gets the vpn_gateway_id of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The vpn_gateway_id of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._vpn_gateway_id

    @vpn_gateway_id.setter
    def vpn_gateway_id(self, vpn_gateway_id):
        """Sets the vpn_gateway_id of this DescribeVpnConnectionAttributesResponse.


        :param vpn_gateway_id: The vpn_gateway_id of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :type: str
        """

        self._vpn_gateway_id = vpn_gateway_id

    @property
    def zone_id(self):
        """Gets the zone_id of this DescribeVpnConnectionAttributesResponse.  # noqa: E501


        :return: The zone_id of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this DescribeVpnConnectionAttributesResponse.


        :param zone_id: The zone_id of this DescribeVpnConnectionAttributesResponse.  # noqa: E501
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
        if issubclass(DescribeVpnConnectionAttributesResponse, dict):
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
        if not isinstance(other, DescribeVpnConnectionAttributesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeVpnConnectionAttributesResponse):
            return True

        return self.to_dict() != other.to_dict()
