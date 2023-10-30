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


class DescribeVpcAttributesResponse(object):
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
        'associate_cens': 'list[AssociateCenForDescribeVpcAttributesOutput]',
        'cidr_block': 'str',
        'creation_time': 'str',
        'description': 'str',
        'dns_servers': 'list[str]',
        'ipv6_cidr_block': 'str',
        'is_default': 'bool',
        'nat_gateway_ids': 'list[str]',
        'network_acl_num': 'str',
        'project_name': 'str',
        'request_id': 'str',
        'route_table_ids': 'list[str]',
        'secondary_cidr_blocks': 'list[str]',
        'security_group_ids': 'list[str]',
        'status': 'str',
        'subnet_ids': 'list[str]',
        'tags': 'list[TagForDescribeVpcAttributesOutput]',
        'update_time': 'str',
        'user_cidr_blocks': 'list[str]',
        'vpc_id': 'str',
        'vpc_name': 'str'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'associate_cens': 'AssociateCens',
        'cidr_block': 'CidrBlock',
        'creation_time': 'CreationTime',
        'description': 'Description',
        'dns_servers': 'DnsServers',
        'ipv6_cidr_block': 'Ipv6CidrBlock',
        'is_default': 'IsDefault',
        'nat_gateway_ids': 'NatGatewayIds',
        'network_acl_num': 'NetworkAclNum',
        'project_name': 'ProjectName',
        'request_id': 'RequestId',
        'route_table_ids': 'RouteTableIds',
        'secondary_cidr_blocks': 'SecondaryCidrBlocks',
        'security_group_ids': 'SecurityGroupIds',
        'status': 'Status',
        'subnet_ids': 'SubnetIds',
        'tags': 'Tags',
        'update_time': 'UpdateTime',
        'user_cidr_blocks': 'UserCidrBlocks',
        'vpc_id': 'VpcId',
        'vpc_name': 'VpcName'
    }

    def __init__(self, account_id=None, associate_cens=None, cidr_block=None, creation_time=None, description=None, dns_servers=None, ipv6_cidr_block=None, is_default=None, nat_gateway_ids=None, network_acl_num=None, project_name=None, request_id=None, route_table_ids=None, secondary_cidr_blocks=None, security_group_ids=None, status=None, subnet_ids=None, tags=None, update_time=None, user_cidr_blocks=None, vpc_id=None, vpc_name=None, _configuration=None):  # noqa: E501
        """DescribeVpcAttributesResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._associate_cens = None
        self._cidr_block = None
        self._creation_time = None
        self._description = None
        self._dns_servers = None
        self._ipv6_cidr_block = None
        self._is_default = None
        self._nat_gateway_ids = None
        self._network_acl_num = None
        self._project_name = None
        self._request_id = None
        self._route_table_ids = None
        self._secondary_cidr_blocks = None
        self._security_group_ids = None
        self._status = None
        self._subnet_ids = None
        self._tags = None
        self._update_time = None
        self._user_cidr_blocks = None
        self._vpc_id = None
        self._vpc_name = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if associate_cens is not None:
            self.associate_cens = associate_cens
        if cidr_block is not None:
            self.cidr_block = cidr_block
        if creation_time is not None:
            self.creation_time = creation_time
        if description is not None:
            self.description = description
        if dns_servers is not None:
            self.dns_servers = dns_servers
        if ipv6_cidr_block is not None:
            self.ipv6_cidr_block = ipv6_cidr_block
        if is_default is not None:
            self.is_default = is_default
        if nat_gateway_ids is not None:
            self.nat_gateway_ids = nat_gateway_ids
        if network_acl_num is not None:
            self.network_acl_num = network_acl_num
        if project_name is not None:
            self.project_name = project_name
        if request_id is not None:
            self.request_id = request_id
        if route_table_ids is not None:
            self.route_table_ids = route_table_ids
        if secondary_cidr_blocks is not None:
            self.secondary_cidr_blocks = secondary_cidr_blocks
        if security_group_ids is not None:
            self.security_group_ids = security_group_ids
        if status is not None:
            self.status = status
        if subnet_ids is not None:
            self.subnet_ids = subnet_ids
        if tags is not None:
            self.tags = tags
        if update_time is not None:
            self.update_time = update_time
        if user_cidr_blocks is not None:
            self.user_cidr_blocks = user_cidr_blocks
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if vpc_name is not None:
            self.vpc_name = vpc_name

    @property
    def account_id(self):
        """Gets the account_id of this DescribeVpcAttributesResponse.  # noqa: E501


        :return: The account_id of this DescribeVpcAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this DescribeVpcAttributesResponse.


        :param account_id: The account_id of this DescribeVpcAttributesResponse.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def associate_cens(self):
        """Gets the associate_cens of this DescribeVpcAttributesResponse.  # noqa: E501


        :return: The associate_cens of this DescribeVpcAttributesResponse.  # noqa: E501
        :rtype: list[AssociateCenForDescribeVpcAttributesOutput]
        """
        return self._associate_cens

    @associate_cens.setter
    def associate_cens(self, associate_cens):
        """Sets the associate_cens of this DescribeVpcAttributesResponse.


        :param associate_cens: The associate_cens of this DescribeVpcAttributesResponse.  # noqa: E501
        :type: list[AssociateCenForDescribeVpcAttributesOutput]
        """

        self._associate_cens = associate_cens

    @property
    def cidr_block(self):
        """Gets the cidr_block of this DescribeVpcAttributesResponse.  # noqa: E501


        :return: The cidr_block of this DescribeVpcAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """Sets the cidr_block of this DescribeVpcAttributesResponse.


        :param cidr_block: The cidr_block of this DescribeVpcAttributesResponse.  # noqa: E501
        :type: str
        """

        self._cidr_block = cidr_block

    @property
    def creation_time(self):
        """Gets the creation_time of this DescribeVpcAttributesResponse.  # noqa: E501


        :return: The creation_time of this DescribeVpcAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this DescribeVpcAttributesResponse.


        :param creation_time: The creation_time of this DescribeVpcAttributesResponse.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def description(self):
        """Gets the description of this DescribeVpcAttributesResponse.  # noqa: E501


        :return: The description of this DescribeVpcAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DescribeVpcAttributesResponse.


        :param description: The description of this DescribeVpcAttributesResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def dns_servers(self):
        """Gets the dns_servers of this DescribeVpcAttributesResponse.  # noqa: E501


        :return: The dns_servers of this DescribeVpcAttributesResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._dns_servers

    @dns_servers.setter
    def dns_servers(self, dns_servers):
        """Sets the dns_servers of this DescribeVpcAttributesResponse.


        :param dns_servers: The dns_servers of this DescribeVpcAttributesResponse.  # noqa: E501
        :type: list[str]
        """

        self._dns_servers = dns_servers

    @property
    def ipv6_cidr_block(self):
        """Gets the ipv6_cidr_block of this DescribeVpcAttributesResponse.  # noqa: E501


        :return: The ipv6_cidr_block of this DescribeVpcAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._ipv6_cidr_block

    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, ipv6_cidr_block):
        """Sets the ipv6_cidr_block of this DescribeVpcAttributesResponse.


        :param ipv6_cidr_block: The ipv6_cidr_block of this DescribeVpcAttributesResponse.  # noqa: E501
        :type: str
        """

        self._ipv6_cidr_block = ipv6_cidr_block

    @property
    def is_default(self):
        """Gets the is_default of this DescribeVpcAttributesResponse.  # noqa: E501


        :return: The is_default of this DescribeVpcAttributesResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this DescribeVpcAttributesResponse.


        :param is_default: The is_default of this DescribeVpcAttributesResponse.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def nat_gateway_ids(self):
        """Gets the nat_gateway_ids of this DescribeVpcAttributesResponse.  # noqa: E501


        :return: The nat_gateway_ids of this DescribeVpcAttributesResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._nat_gateway_ids

    @nat_gateway_ids.setter
    def nat_gateway_ids(self, nat_gateway_ids):
        """Sets the nat_gateway_ids of this DescribeVpcAttributesResponse.


        :param nat_gateway_ids: The nat_gateway_ids of this DescribeVpcAttributesResponse.  # noqa: E501
        :type: list[str]
        """

        self._nat_gateway_ids = nat_gateway_ids

    @property
    def network_acl_num(self):
        """Gets the network_acl_num of this DescribeVpcAttributesResponse.  # noqa: E501


        :return: The network_acl_num of this DescribeVpcAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._network_acl_num

    @network_acl_num.setter
    def network_acl_num(self, network_acl_num):
        """Sets the network_acl_num of this DescribeVpcAttributesResponse.


        :param network_acl_num: The network_acl_num of this DescribeVpcAttributesResponse.  # noqa: E501
        :type: str
        """

        self._network_acl_num = network_acl_num

    @property
    def project_name(self):
        """Gets the project_name of this DescribeVpcAttributesResponse.  # noqa: E501


        :return: The project_name of this DescribeVpcAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeVpcAttributesResponse.


        :param project_name: The project_name of this DescribeVpcAttributesResponse.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def request_id(self):
        """Gets the request_id of this DescribeVpcAttributesResponse.  # noqa: E501


        :return: The request_id of this DescribeVpcAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this DescribeVpcAttributesResponse.


        :param request_id: The request_id of this DescribeVpcAttributesResponse.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def route_table_ids(self):
        """Gets the route_table_ids of this DescribeVpcAttributesResponse.  # noqa: E501


        :return: The route_table_ids of this DescribeVpcAttributesResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._route_table_ids

    @route_table_ids.setter
    def route_table_ids(self, route_table_ids):
        """Sets the route_table_ids of this DescribeVpcAttributesResponse.


        :param route_table_ids: The route_table_ids of this DescribeVpcAttributesResponse.  # noqa: E501
        :type: list[str]
        """

        self._route_table_ids = route_table_ids

    @property
    def secondary_cidr_blocks(self):
        """Gets the secondary_cidr_blocks of this DescribeVpcAttributesResponse.  # noqa: E501


        :return: The secondary_cidr_blocks of this DescribeVpcAttributesResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._secondary_cidr_blocks

    @secondary_cidr_blocks.setter
    def secondary_cidr_blocks(self, secondary_cidr_blocks):
        """Sets the secondary_cidr_blocks of this DescribeVpcAttributesResponse.


        :param secondary_cidr_blocks: The secondary_cidr_blocks of this DescribeVpcAttributesResponse.  # noqa: E501
        :type: list[str]
        """

        self._secondary_cidr_blocks = secondary_cidr_blocks

    @property
    def security_group_ids(self):
        """Gets the security_group_ids of this DescribeVpcAttributesResponse.  # noqa: E501


        :return: The security_group_ids of this DescribeVpcAttributesResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._security_group_ids

    @security_group_ids.setter
    def security_group_ids(self, security_group_ids):
        """Sets the security_group_ids of this DescribeVpcAttributesResponse.


        :param security_group_ids: The security_group_ids of this DescribeVpcAttributesResponse.  # noqa: E501
        :type: list[str]
        """

        self._security_group_ids = security_group_ids

    @property
    def status(self):
        """Gets the status of this DescribeVpcAttributesResponse.  # noqa: E501


        :return: The status of this DescribeVpcAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DescribeVpcAttributesResponse.


        :param status: The status of this DescribeVpcAttributesResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def subnet_ids(self):
        """Gets the subnet_ids of this DescribeVpcAttributesResponse.  # noqa: E501


        :return: The subnet_ids of this DescribeVpcAttributesResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        """Sets the subnet_ids of this DescribeVpcAttributesResponse.


        :param subnet_ids: The subnet_ids of this DescribeVpcAttributesResponse.  # noqa: E501
        :type: list[str]
        """

        self._subnet_ids = subnet_ids

    @property
    def tags(self):
        """Gets the tags of this DescribeVpcAttributesResponse.  # noqa: E501


        :return: The tags of this DescribeVpcAttributesResponse.  # noqa: E501
        :rtype: list[TagForDescribeVpcAttributesOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DescribeVpcAttributesResponse.


        :param tags: The tags of this DescribeVpcAttributesResponse.  # noqa: E501
        :type: list[TagForDescribeVpcAttributesOutput]
        """

        self._tags = tags

    @property
    def update_time(self):
        """Gets the update_time of this DescribeVpcAttributesResponse.  # noqa: E501


        :return: The update_time of this DescribeVpcAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this DescribeVpcAttributesResponse.


        :param update_time: The update_time of this DescribeVpcAttributesResponse.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

    @property
    def user_cidr_blocks(self):
        """Gets the user_cidr_blocks of this DescribeVpcAttributesResponse.  # noqa: E501


        :return: The user_cidr_blocks of this DescribeVpcAttributesResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_cidr_blocks

    @user_cidr_blocks.setter
    def user_cidr_blocks(self, user_cidr_blocks):
        """Sets the user_cidr_blocks of this DescribeVpcAttributesResponse.


        :param user_cidr_blocks: The user_cidr_blocks of this DescribeVpcAttributesResponse.  # noqa: E501
        :type: list[str]
        """

        self._user_cidr_blocks = user_cidr_blocks

    @property
    def vpc_id(self):
        """Gets the vpc_id of this DescribeVpcAttributesResponse.  # noqa: E501


        :return: The vpc_id of this DescribeVpcAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this DescribeVpcAttributesResponse.


        :param vpc_id: The vpc_id of this DescribeVpcAttributesResponse.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

    @property
    def vpc_name(self):
        """Gets the vpc_name of this DescribeVpcAttributesResponse.  # noqa: E501


        :return: The vpc_name of this DescribeVpcAttributesResponse.  # noqa: E501
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        """Sets the vpc_name of this DescribeVpcAttributesResponse.


        :param vpc_name: The vpc_name of this DescribeVpcAttributesResponse.  # noqa: E501
        :type: str
        """

        self._vpc_name = vpc_name

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
        if issubclass(DescribeVpcAttributesResponse, dict):
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
        if not isinstance(other, DescribeVpcAttributesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeVpcAttributesResponse):
            return True

        return self.to_dict() != other.to_dict()
