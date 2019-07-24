# coding: utf-8

"""
    Jumpserver API Docs

    Jumpserver Restful api docs  # noqa: E501

    OpenAPI spec version: v1
    Contact: support@fit2cloud.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SyncInstanceTask(object):
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
        'id': 'str',
        'name': 'str',
        'account_name': 'str',
        'history_count': 'str',
        'instance_count': 'str',
        'comment': 'str',
        'date_last_sync': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'account_name': 'account_name',
        'history_count': 'history_count',
        'instance_count': 'instance_count',
        'comment': 'comment',
        'date_last_sync': 'date_last_sync'
    }

    def __init__(self, id=None, name=None, account_name=None, history_count=None, instance_count=None, comment=None, date_last_sync=None):  # noqa: E501
        """SyncInstanceTask - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._account_name = None
        self._history_count = None
        self._instance_count = None
        self._comment = None
        self._date_last_sync = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if account_name is not None:
            self.account_name = account_name
        if history_count is not None:
            self.history_count = history_count
        if instance_count is not None:
            self.instance_count = instance_count
        if comment is not None:
            self.comment = comment
        if date_last_sync is not None:
            self.date_last_sync = date_last_sync

    @property
    def id(self):
        """Gets the id of this SyncInstanceTask.  # noqa: E501


        :return: The id of this SyncInstanceTask.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SyncInstanceTask.


        :param id: The id of this SyncInstanceTask.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SyncInstanceTask.  # noqa: E501


        :return: The name of this SyncInstanceTask.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SyncInstanceTask.


        :param name: The name of this SyncInstanceTask.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 128:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def account_name(self):
        """Gets the account_name of this SyncInstanceTask.  # noqa: E501


        :return: The account_name of this SyncInstanceTask.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this SyncInstanceTask.


        :param account_name: The account_name of this SyncInstanceTask.  # noqa: E501
        :type: str
        """

        self._account_name = account_name

    @property
    def history_count(self):
        """Gets the history_count of this SyncInstanceTask.  # noqa: E501


        :return: The history_count of this SyncInstanceTask.  # noqa: E501
        :rtype: str
        """
        return self._history_count

    @history_count.setter
    def history_count(self, history_count):
        """Sets the history_count of this SyncInstanceTask.


        :param history_count: The history_count of this SyncInstanceTask.  # noqa: E501
        :type: str
        """

        self._history_count = history_count

    @property
    def instance_count(self):
        """Gets the instance_count of this SyncInstanceTask.  # noqa: E501


        :return: The instance_count of this SyncInstanceTask.  # noqa: E501
        :rtype: str
        """
        return self._instance_count

    @instance_count.setter
    def instance_count(self, instance_count):
        """Sets the instance_count of this SyncInstanceTask.


        :param instance_count: The instance_count of this SyncInstanceTask.  # noqa: E501
        :type: str
        """

        self._instance_count = instance_count

    @property
    def comment(self):
        """Gets the comment of this SyncInstanceTask.  # noqa: E501


        :return: The comment of this SyncInstanceTask.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this SyncInstanceTask.


        :param comment: The comment of this SyncInstanceTask.  # noqa: E501
        :type: str
        """
        if comment is not None and len(comment) > 2048:
            raise ValueError("Invalid value for `comment`, length must be less than or equal to `2048`")  # noqa: E501

        self._comment = comment

    @property
    def date_last_sync(self):
        """Gets the date_last_sync of this SyncInstanceTask.  # noqa: E501


        :return: The date_last_sync of this SyncInstanceTask.  # noqa: E501
        :rtype: datetime
        """
        return self._date_last_sync

    @date_last_sync.setter
    def date_last_sync(self, date_last_sync):
        """Sets the date_last_sync of this SyncInstanceTask.


        :param date_last_sync: The date_last_sync of this SyncInstanceTask.  # noqa: E501
        :type: datetime
        """

        self._date_last_sync = date_last_sync

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SyncInstanceTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
