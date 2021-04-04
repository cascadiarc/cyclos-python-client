# coding: utf-8

"""
    Cyclos 4.11.5 API

    The REST API for Cyclos 4.11.5  # noqa: E501

    OpenAPI spec version: 4.11.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class OperationDataForRun(object):
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
        'result_information_text': 'str',
        'custom_submit_label': 'str',
        'form_parameters': 'list[CustomFieldDetailed]',
        'confirmation_password_input': 'PasswordInput',
        'row_action': 'OperationRowActionEnum',
        'search_automatically': 'bool',
        'row_location': 'str',
        'row_operation': 'Operation',
        'row_url': 'str',
        'row_parameters': 'list[str]'
    }

    attribute_map = {
        'result_information_text': 'resultInformationText',
        'custom_submit_label': 'customSubmitLabel',
        'form_parameters': 'formParameters',
        'confirmation_password_input': 'confirmationPasswordInput',
        'row_action': 'rowAction',
        'search_automatically': 'searchAutomatically',
        'row_location': 'rowLocation',
        'row_operation': 'rowOperation',
        'row_url': 'rowUrl',
        'row_parameters': 'rowParameters'
    }

    def __init__(self, result_information_text=None, custom_submit_label=None, form_parameters=None, confirmation_password_input=None, row_action=None, search_automatically=None, row_location=None, row_operation=None, row_url=None, row_parameters=None, _configuration=None):  # noqa: E501
        """OperationDataForRun - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._result_information_text = None
        self._custom_submit_label = None
        self._form_parameters = None
        self._confirmation_password_input = None
        self._row_action = None
        self._search_automatically = None
        self._row_location = None
        self._row_operation = None
        self._row_url = None
        self._row_parameters = None
        self.discriminator = None

        if result_information_text is not None:
            self.result_information_text = result_information_text
        if custom_submit_label is not None:
            self.custom_submit_label = custom_submit_label
        if form_parameters is not None:
            self.form_parameters = form_parameters
        if confirmation_password_input is not None:
            self.confirmation_password_input = confirmation_password_input
        if row_action is not None:
            self.row_action = row_action
        if search_automatically is not None:
            self.search_automatically = search_automatically
        if row_location is not None:
            self.row_location = row_location
        if row_operation is not None:
            self.row_operation = row_operation
        if row_url is not None:
            self.row_url = row_url
        if row_parameters is not None:
            self.row_parameters = row_parameters

    @property
    def result_information_text(self):
        """Gets the result_information_text of this OperationDataForRun.  # noqa: E501

        A message to be displayed to the user when displaying the page  results. Only returned if `resultType` is `resultPage`.   # noqa: E501

        :return: The result_information_text of this OperationDataForRun.  # noqa: E501
        :rtype: str
        """
        return self._result_information_text

    @result_information_text.setter
    def result_information_text(self, result_information_text):
        """Sets the result_information_text of this OperationDataForRun.

        A message to be displayed to the user when displaying the page  results. Only returned if `resultType` is `resultPage`.   # noqa: E501

        :param result_information_text: The result_information_text of this OperationDataForRun.  # noqa: E501
        :type: str
        """

        self._result_information_text = result_information_text

    @property
    def custom_submit_label(self):
        """Gets the custom_submit_label of this OperationDataForRun.  # noqa: E501

        A label to be shown on the submit button. When not returned, a generic 'Submit' should be displayed.   # noqa: E501

        :return: The custom_submit_label of this OperationDataForRun.  # noqa: E501
        :rtype: str
        """
        return self._custom_submit_label

    @custom_submit_label.setter
    def custom_submit_label(self, custom_submit_label):
        """Sets the custom_submit_label of this OperationDataForRun.

        A label to be shown on the submit button. When not returned, a generic 'Submit' should be displayed.   # noqa: E501

        :param custom_submit_label: The custom_submit_label of this OperationDataForRun.  # noqa: E501
        :type: str
        """

        self._custom_submit_label = custom_submit_label

    @property
    def form_parameters(self):
        """Gets the form_parameters of this OperationDataForRun.  # noqa: E501

        The custom fields which are used in a form as parameters for the operation execution.   # noqa: E501

        :return: The form_parameters of this OperationDataForRun.  # noqa: E501
        :rtype: list[CustomFieldDetailed]
        """
        return self._form_parameters

    @form_parameters.setter
    def form_parameters(self, form_parameters):
        """Sets the form_parameters of this OperationDataForRun.

        The custom fields which are used in a form as parameters for the operation execution.   # noqa: E501

        :param form_parameters: The form_parameters of this OperationDataForRun.  # noqa: E501
        :type: list[CustomFieldDetailed]
        """

        self._form_parameters = form_parameters

    @property
    def confirmation_password_input(self):
        """Gets the confirmation_password_input of this OperationDataForRun.  # noqa: E501

        If a confirmation password is used, contains the definitions on how to request that password from the user. This confirmation password is required when performing sensible actions. Sometimes this is dynamic, for example, the confirmation might be configured to be used only once per session, or operations like payments may have a limit per day to be without confirmation (pinless).   # noqa: E501

        :return: The confirmation_password_input of this OperationDataForRun.  # noqa: E501
        :rtype: PasswordInput
        """
        return self._confirmation_password_input

    @confirmation_password_input.setter
    def confirmation_password_input(self, confirmation_password_input):
        """Sets the confirmation_password_input of this OperationDataForRun.

        If a confirmation password is used, contains the definitions on how to request that password from the user. This confirmation password is required when performing sensible actions. Sometimes this is dynamic, for example, the confirmation might be configured to be used only once per session, or operations like payments may have a limit per day to be without confirmation (pinless).   # noqa: E501

        :param confirmation_password_input: The confirmation_password_input of this OperationDataForRun.  # noqa: E501
        :type: PasswordInput
        """

        self._confirmation_password_input = confirmation_password_input

    @property
    def row_action(self):
        """Gets the row_action of this OperationDataForRun.  # noqa: E501

        The action that should be performed when the user clicks a row in the results table Possible values are: * location: Navigate to a standard Cyclos location * operation: Run an internal custom operation, which is set on the custom operation itself * url: Navigate to an arbitrary URL, which is set in the custom operation itself   # noqa: E501

        :return: The row_action of this OperationDataForRun.  # noqa: E501
        :rtype: OperationRowActionEnum
        """
        return self._row_action

    @row_action.setter
    def row_action(self, row_action):
        """Sets the row_action of this OperationDataForRun.

        The action that should be performed when the user clicks a row in the results table Possible values are: * location: Navigate to a standard Cyclos location * operation: Run an internal custom operation, which is set on the custom operation itself * url: Navigate to an arbitrary URL, which is set in the custom operation itself   # noqa: E501

        :param row_action: The row_action of this OperationDataForRun.  # noqa: E501
        :type: OperationRowActionEnum
        """

        self._row_action = row_action

    @property
    def search_automatically(self):
        """Gets the search_automatically of this OperationDataForRun.  # noqa: E501

        Should the operation be immediately executed by the third party client software when first presenting the form to the user  (when `true`) or only when the user clicks submit (when `false`)? Only returned if `resultType` is `resultPage`.   # noqa: E501

        :return: The search_automatically of this OperationDataForRun.  # noqa: E501
        :rtype: bool
        """
        return self._search_automatically

    @search_automatically.setter
    def search_automatically(self, search_automatically):
        """Sets the search_automatically of this OperationDataForRun.

        Should the operation be immediately executed by the third party client software when first presenting the form to the user  (when `true`) or only when the user clicks submit (when `false`)? Only returned if `resultType` is `resultPage`.   # noqa: E501

        :param search_automatically: The search_automatically of this OperationDataForRun.  # noqa: E501
        :type: bool
        """

        self._search_automatically = search_automatically

    @property
    def row_location(self):
        """Gets the row_location of this OperationDataForRun.  # noqa: E501

        The location to which the client should be redirected when selecting a row in the results table. Only returned if `resultType` is `resultPage` and `rowAction` is `location`.   # noqa: E501

        :return: The row_location of this OperationDataForRun.  # noqa: E501
        :rtype: str
        """
        return self._row_location

    @row_location.setter
    def row_location(self, row_location):
        """Sets the row_location of this OperationDataForRun.

        The location to which the client should be redirected when selecting a row in the results table. Only returned if `resultType` is `resultPage` and `rowAction` is `location`.   # noqa: E501

        :param row_location: The row_location of this OperationDataForRun.  # noqa: E501
        :type: str
        """

        self._row_location = row_location

    @property
    def row_operation(self):
        """Gets the row_operation of this OperationDataForRun.  # noqa: E501

        The custom operation that should be executed when clicking a row. Only returned if `resultType` is `resultPage` and `rowAction` is `operation`.   # noqa: E501

        :return: The row_operation of this OperationDataForRun.  # noqa: E501
        :rtype: Operation
        """
        return self._row_operation

    @row_operation.setter
    def row_operation(self, row_operation):
        """Sets the row_operation of this OperationDataForRun.

        The custom operation that should be executed when clicking a row. Only returned if `resultType` is `resultPage` and `rowAction` is `operation`.   # noqa: E501

        :param row_operation: The row_operation of this OperationDataForRun.  # noqa: E501
        :type: Operation
        """

        self._row_operation = row_operation

    @property
    def row_url(self):
        """Gets the row_url of this OperationDataForRun.  # noqa: E501

        The URL the client should be redirected when clicking a row. Only returned if `resultType` is `resultPage` and `rowAction` is `url`.   # noqa: E501

        :return: The row_url of this OperationDataForRun.  # noqa: E501
        :rtype: str
        """
        return self._row_url

    @row_url.setter
    def row_url(self, row_url):
        """Sets the row_url of this OperationDataForRun.

        The URL the client should be redirected when clicking a row. Only returned if `resultType` is `resultPage` and `rowAction` is `url`.   # noqa: E501

        :param row_url: The row_url of this OperationDataForRun.  # noqa: E501
        :type: str
        """

        self._row_url = row_url

    @property
    def row_parameters(self):
        """Gets the row_parameters of this OperationDataForRun.  # noqa: E501

        The names of parameters belonging to each custom operation result that should be passed as parameter to the custom operation or URL which is executed when selecting a row in the table. Only returned if `resultType` is `resultPage`.   # noqa: E501

        :return: The row_parameters of this OperationDataForRun.  # noqa: E501
        :rtype: list[str]
        """
        return self._row_parameters

    @row_parameters.setter
    def row_parameters(self, row_parameters):
        """Sets the row_parameters of this OperationDataForRun.

        The names of parameters belonging to each custom operation result that should be passed as parameter to the custom operation or URL which is executed when selecting a row in the table. Only returned if `resultType` is `resultPage`.   # noqa: E501

        :param row_parameters: The row_parameters of this OperationDataForRun.  # noqa: E501
        :type: list[str]
        """

        self._row_parameters = row_parameters

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
        if issubclass(OperationDataForRun, dict):
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
        if not isinstance(other, OperationDataForRun):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OperationDataForRun):
            return True

        return self.to_dict() != other.to_dict()