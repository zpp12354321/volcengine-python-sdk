# coding: utf-8

"""
    spark

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListApplicationInstanceRequest(object):
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
        'application_name': 'str',
        'application_trn': 'str',
        'engine_version': 'str',
        'instance_id': 'int',
        'page_num': 'int',
        'page_size': 'int',
        'project_id': 'str',
        'resource_pool_trn': 'str',
        'sort_field': 'str',
        'sort_order': 'str',
        'state': 'str'
    }

    attribute_map = {
        'application_name': 'ApplicationName',
        'application_trn': 'ApplicationTrn',
        'engine_version': 'EngineVersion',
        'instance_id': 'InstanceId',
        'page_num': 'PageNum',
        'page_size': 'PageSize',
        'project_id': 'ProjectId',
        'resource_pool_trn': 'ResourcePoolTrn',
        'sort_field': 'SortField',
        'sort_order': 'SortOrder',
        'state': 'State'
    }

    def __init__(self, application_name=None, application_trn=None, engine_version=None, instance_id=None, page_num=None, page_size=None, project_id=None, resource_pool_trn=None, sort_field=None, sort_order=None, state=None, _configuration=None):  # noqa: E501
        """ListApplicationInstanceRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._application_name = None
        self._application_trn = None
        self._engine_version = None
        self._instance_id = None
        self._page_num = None
        self._page_size = None
        self._project_id = None
        self._resource_pool_trn = None
        self._sort_field = None
        self._sort_order = None
        self._state = None
        self.discriminator = None

        if application_name is not None:
            self.application_name = application_name
        if application_trn is not None:
            self.application_trn = application_trn
        if engine_version is not None:
            self.engine_version = engine_version
        if instance_id is not None:
            self.instance_id = instance_id
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size
        if project_id is not None:
            self.project_id = project_id
        if resource_pool_trn is not None:
            self.resource_pool_trn = resource_pool_trn
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_order is not None:
            self.sort_order = sort_order
        if state is not None:
            self.state = state

    @property
    def application_name(self):
        """Gets the application_name of this ListApplicationInstanceRequest.  # noqa: E501


        :return: The application_name of this ListApplicationInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this ListApplicationInstanceRequest.


        :param application_name: The application_name of this ListApplicationInstanceRequest.  # noqa: E501
        :type: str
        """

        self._application_name = application_name

    @property
    def application_trn(self):
        """Gets the application_trn of this ListApplicationInstanceRequest.  # noqa: E501


        :return: The application_trn of this ListApplicationInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._application_trn

    @application_trn.setter
    def application_trn(self, application_trn):
        """Sets the application_trn of this ListApplicationInstanceRequest.


        :param application_trn: The application_trn of this ListApplicationInstanceRequest.  # noqa: E501
        :type: str
        """

        self._application_trn = application_trn

    @property
    def engine_version(self):
        """Gets the engine_version of this ListApplicationInstanceRequest.  # noqa: E501


        :return: The engine_version of this ListApplicationInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this ListApplicationInstanceRequest.


        :param engine_version: The engine_version of this ListApplicationInstanceRequest.  # noqa: E501
        :type: str
        """

        self._engine_version = engine_version

    @property
    def instance_id(self):
        """Gets the instance_id of this ListApplicationInstanceRequest.  # noqa: E501


        :return: The instance_id of this ListApplicationInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListApplicationInstanceRequest.


        :param instance_id: The instance_id of this ListApplicationInstanceRequest.  # noqa: E501
        :type: int
        """

        self._instance_id = instance_id

    @property
    def page_num(self):
        """Gets the page_num of this ListApplicationInstanceRequest.  # noqa: E501


        :return: The page_num of this ListApplicationInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        """Sets the page_num of this ListApplicationInstanceRequest.


        :param page_num: The page_num of this ListApplicationInstanceRequest.  # noqa: E501
        :type: int
        """

        self._page_num = page_num

    @property
    def page_size(self):
        """Gets the page_size of this ListApplicationInstanceRequest.  # noqa: E501


        :return: The page_size of this ListApplicationInstanceRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListApplicationInstanceRequest.


        :param page_size: The page_size of this ListApplicationInstanceRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def project_id(self):
        """Gets the project_id of this ListApplicationInstanceRequest.  # noqa: E501


        :return: The project_id of this ListApplicationInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListApplicationInstanceRequest.


        :param project_id: The project_id of this ListApplicationInstanceRequest.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def resource_pool_trn(self):
        """Gets the resource_pool_trn of this ListApplicationInstanceRequest.  # noqa: E501


        :return: The resource_pool_trn of this ListApplicationInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._resource_pool_trn

    @resource_pool_trn.setter
    def resource_pool_trn(self, resource_pool_trn):
        """Sets the resource_pool_trn of this ListApplicationInstanceRequest.


        :param resource_pool_trn: The resource_pool_trn of this ListApplicationInstanceRequest.  # noqa: E501
        :type: str
        """

        self._resource_pool_trn = resource_pool_trn

    @property
    def sort_field(self):
        """Gets the sort_field of this ListApplicationInstanceRequest.  # noqa: E501


        :return: The sort_field of this ListApplicationInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        """Sets the sort_field of this ListApplicationInstanceRequest.


        :param sort_field: The sort_field of this ListApplicationInstanceRequest.  # noqa: E501
        :type: str
        """

        self._sort_field = sort_field

    @property
    def sort_order(self):
        """Gets the sort_order of this ListApplicationInstanceRequest.  # noqa: E501


        :return: The sort_order of this ListApplicationInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this ListApplicationInstanceRequest.


        :param sort_order: The sort_order of this ListApplicationInstanceRequest.  # noqa: E501
        :type: str
        """

        self._sort_order = sort_order

    @property
    def state(self):
        """Gets the state of this ListApplicationInstanceRequest.  # noqa: E501


        :return: The state of this ListApplicationInstanceRequest.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ListApplicationInstanceRequest.


        :param state: The state of this ListApplicationInstanceRequest.  # noqa: E501
        :type: str
        """

        self._state = state

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
        if issubclass(ListApplicationInstanceRequest, dict):
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
        if not isinstance(other, ListApplicationInstanceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListApplicationInstanceRequest):
            return True

        return self.to_dict() != other.to_dict()
