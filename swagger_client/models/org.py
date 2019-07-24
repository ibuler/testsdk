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


class Org(object):
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
        'created_by': 'str',
        'date_created': 'datetime',
        'comment': 'str',
        'users': 'list[str]',
        'admins': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'created_by': 'created_by',
        'date_created': 'date_created',
        'comment': 'comment',
        'users': 'users',
        'admins': 'admins'
    }

    def __init__(self, id=None, name=None, created_by=None, date_created=None, comment=None, users=None, admins=None):  # noqa: E501
        """Org - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._created_by = None
        self._date_created = None
        self._comment = None
        self._users = None
        self._admins = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if created_by is not None:
            self.created_by = created_by
        if date_created is not None:
            self.date_created = date_created
        if comment is not None:
            self.comment = comment
        if users is not None:
            self.users = users
        if admins is not None:
            self.admins = admins

    @property
    def id(self):
        """Gets the id of this Org.  # noqa: E501


        :return: The id of this Org.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Org.


        :param id: The id of this Org.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Org.  # noqa: E501


        :return: The name of this Org.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Org.


        :param name: The name of this Org.  # noqa: E501
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
    def created_by(self):
        """Gets the created_by of this Org.  # noqa: E501


        :return: The created_by of this Org.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Org.


        :param created_by: The created_by of this Org.  # noqa: E501
        :type: str
        """
        if created_by is not None and len(created_by) < 1:
            raise ValueError("Invalid value for `created_by`, length must be greater than or equal to `1`")  # noqa: E501

        self._created_by = created_by

    @property
    def date_created(self):
        """Gets the date_created of this Org.  # noqa: E501


        :return: The date_created of this Org.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this Org.


        :param date_created: The date_created of this Org.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def comment(self):
        """Gets the comment of this Org.  # noqa: E501


        :return: The comment of this Org.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Org.


        :param comment: The comment of this Org.  # noqa: E501
        :type: str
        """
        if comment is not None and len(comment) > 128:
            raise ValueError("Invalid value for `comment`, length must be less than or equal to `128`")  # noqa: E501

        self._comment = comment

    @property
    def users(self):
        """Gets the users of this Org.  # noqa: E501


        :return: The users of this Org.  # noqa: E501
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this Org.


        :param users: The users of this Org.  # noqa: E501
        :type: list[str]
        """

        self._users = users

    @property
    def admins(self):
        """Gets the admins of this Org.  # noqa: E501


        :return: The admins of this Org.  # noqa: E501
        :rtype: list[str]
        """
        return self._admins

    @admins.setter
    def admins(self, admins):
        """Sets the admins of this Org.


        :param admins: The admins of this Org.  # noqa: E501
        :type: list[str]
        """

        self._admins = admins

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
        if not isinstance(other, Org):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
