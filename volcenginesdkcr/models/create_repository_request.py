# coding: utf-8

"""
    cr

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CreateRepositoryRequest(object):
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
        'access_level': 'str',
        'client_token': 'str',
        'description': 'str',
        'name': 'str',
        'namespace': 'str',
        'registry': 'str'
    }

    attribute_map = {
        'access_level': 'AccessLevel',
        'client_token': 'ClientToken',
        'description': 'Description',
        'name': 'Name',
        'namespace': 'Namespace',
        'registry': 'Registry'
    }

    def __init__(self, access_level=None, client_token=None, description=None, name=None, namespace=None, registry=None, _configuration=None):  # noqa: E501
        """CreateRepositoryRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_level = None
        self._client_token = None
        self._description = None
        self._name = None
        self._namespace = None
        self._registry = None
        self.discriminator = None

        if access_level is not None:
            self.access_level = access_level
        if client_token is not None:
            self.client_token = client_token
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if registry is not None:
            self.registry = registry

    @property
    def access_level(self):
        """Gets the access_level of this CreateRepositoryRequest.  # noqa: E501


        :return: The access_level of this CreateRepositoryRequest.  # noqa: E501
        :rtype: str
        """
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        """Sets the access_level of this CreateRepositoryRequest.


        :param access_level: The access_level of this CreateRepositoryRequest.  # noqa: E501
        :type: str
        """

        self._access_level = access_level

    @property
    def client_token(self):
        """Gets the client_token of this CreateRepositoryRequest.  # noqa: E501


        :return: The client_token of this CreateRepositoryRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this CreateRepositoryRequest.


        :param client_token: The client_token of this CreateRepositoryRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def description(self):
        """Gets the description of this CreateRepositoryRequest.  # noqa: E501


        :return: The description of this CreateRepositoryRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateRepositoryRequest.


        :param description: The description of this CreateRepositoryRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this CreateRepositoryRequest.  # noqa: E501


        :return: The name of this CreateRepositoryRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateRepositoryRequest.


        :param name: The name of this CreateRepositoryRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this CreateRepositoryRequest.  # noqa: E501


        :return: The namespace of this CreateRepositoryRequest.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this CreateRepositoryRequest.


        :param namespace: The namespace of this CreateRepositoryRequest.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def registry(self):
        """Gets the registry of this CreateRepositoryRequest.  # noqa: E501


        :return: The registry of this CreateRepositoryRequest.  # noqa: E501
        :rtype: str
        """
        return self._registry

    @registry.setter
    def registry(self, registry):
        """Sets the registry of this CreateRepositoryRequest.


        :param registry: The registry of this CreateRepositoryRequest.  # noqa: E501
        :type: str
        """

        self._registry = registry

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
        if issubclass(CreateRepositoryRequest, dict):
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
        if not isinstance(other, CreateRepositoryRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateRepositoryRequest):
            return True

        return self.to_dict() != other.to_dict()