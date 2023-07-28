# coding: utf-8

"""
    rds_mysql_v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateDatabaseRequest(object):
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
        'character_set_name': 'str',
        'db_desc': 'str',
        'db_name': 'str',
        'db_partition': 'int',
        'database_privileges': 'list[DatabasePrivilegeForCreateDatabaseInput]',
        'database_privileges_info': 'list[DatabasePrivilegesInfoForCreateDatabaseInput]',
        'instance_id': 'str'
    }

    attribute_map = {
        'character_set_name': 'CharacterSetName',
        'db_desc': 'DBDesc',
        'db_name': 'DBName',
        'db_partition': 'DBPartition',
        'database_privileges': 'DatabasePrivileges',
        'database_privileges_info': 'DatabasePrivilegesInfo',
        'instance_id': 'InstanceId'
    }

    def __init__(self, character_set_name=None, db_desc=None, db_name=None, db_partition=None, database_privileges=None, database_privileges_info=None, instance_id=None, _configuration=None):  # noqa: E501
        """CreateDatabaseRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._character_set_name = None
        self._db_desc = None
        self._db_name = None
        self._db_partition = None
        self._database_privileges = None
        self._database_privileges_info = None
        self._instance_id = None
        self.discriminator = None

        if character_set_name is not None:
            self.character_set_name = character_set_name
        if db_desc is not None:
            self.db_desc = db_desc
        if db_name is not None:
            self.db_name = db_name
        if db_partition is not None:
            self.db_partition = db_partition
        if database_privileges is not None:
            self.database_privileges = database_privileges
        if database_privileges_info is not None:
            self.database_privileges_info = database_privileges_info
        self.instance_id = instance_id

    @property
    def character_set_name(self):
        """Gets the character_set_name of this CreateDatabaseRequest.  # noqa: E501


        :return: The character_set_name of this CreateDatabaseRequest.  # noqa: E501
        :rtype: str
        """
        return self._character_set_name

    @character_set_name.setter
    def character_set_name(self, character_set_name):
        """Sets the character_set_name of this CreateDatabaseRequest.


        :param character_set_name: The character_set_name of this CreateDatabaseRequest.  # noqa: E501
        :type: str
        """

        self._character_set_name = character_set_name

    @property
    def db_desc(self):
        """Gets the db_desc of this CreateDatabaseRequest.  # noqa: E501


        :return: The db_desc of this CreateDatabaseRequest.  # noqa: E501
        :rtype: str
        """
        return self._db_desc

    @db_desc.setter
    def db_desc(self, db_desc):
        """Sets the db_desc of this CreateDatabaseRequest.


        :param db_desc: The db_desc of this CreateDatabaseRequest.  # noqa: E501
        :type: str
        """

        self._db_desc = db_desc

    @property
    def db_name(self):
        """Gets the db_name of this CreateDatabaseRequest.  # noqa: E501


        :return: The db_name of this CreateDatabaseRequest.  # noqa: E501
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this CreateDatabaseRequest.


        :param db_name: The db_name of this CreateDatabaseRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                db_name is not None and len(db_name) > 64):
            raise ValueError("Invalid value for `db_name`, length must be less than or equal to `64`")  # noqa: E501
        if (self._configuration.client_side_validation and
                db_name is not None and len(db_name) < 2):
            raise ValueError("Invalid value for `db_name`, length must be greater than or equal to `2`")  # noqa: E501

        self._db_name = db_name

    @property
    def db_partition(self):
        """Gets the db_partition of this CreateDatabaseRequest.  # noqa: E501


        :return: The db_partition of this CreateDatabaseRequest.  # noqa: E501
        :rtype: int
        """
        return self._db_partition

    @db_partition.setter
    def db_partition(self, db_partition):
        """Sets the db_partition of this CreateDatabaseRequest.


        :param db_partition: The db_partition of this CreateDatabaseRequest.  # noqa: E501
        :type: int
        """

        self._db_partition = db_partition

    @property
    def database_privileges(self):
        """Gets the database_privileges of this CreateDatabaseRequest.  # noqa: E501


        :return: The database_privileges of this CreateDatabaseRequest.  # noqa: E501
        :rtype: list[DatabasePrivilegeForCreateDatabaseInput]
        """
        return self._database_privileges

    @database_privileges.setter
    def database_privileges(self, database_privileges):
        """Sets the database_privileges of this CreateDatabaseRequest.


        :param database_privileges: The database_privileges of this CreateDatabaseRequest.  # noqa: E501
        :type: list[DatabasePrivilegeForCreateDatabaseInput]
        """

        self._database_privileges = database_privileges

    @property
    def database_privileges_info(self):
        """Gets the database_privileges_info of this CreateDatabaseRequest.  # noqa: E501


        :return: The database_privileges_info of this CreateDatabaseRequest.  # noqa: E501
        :rtype: list[DatabasePrivilegesInfoForCreateDatabaseInput]
        """
        return self._database_privileges_info

    @database_privileges_info.setter
    def database_privileges_info(self, database_privileges_info):
        """Sets the database_privileges_info of this CreateDatabaseRequest.


        :param database_privileges_info: The database_privileges_info of this CreateDatabaseRequest.  # noqa: E501
        :type: list[DatabasePrivilegesInfoForCreateDatabaseInput]
        """

        self._database_privileges_info = database_privileges_info

    @property
    def instance_id(self):
        """Gets the instance_id of this CreateDatabaseRequest.  # noqa: E501


        :return: The instance_id of this CreateDatabaseRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CreateDatabaseRequest.


        :param instance_id: The instance_id of this CreateDatabaseRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

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
        if issubclass(CreateDatabaseRequest, dict):
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
        if not isinstance(other, CreateDatabaseRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDatabaseRequest):
            return True

        return self.to_dict() != other.to_dict()
