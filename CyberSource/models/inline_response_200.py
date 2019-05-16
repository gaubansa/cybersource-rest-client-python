# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse200(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'start_time': 'datetime',
        'end_time': 'datetime',
        'payment_batch_summaries': 'list[InlineResponse200PaymentBatchSummaries]'
    }

    attribute_map = {
        'start_time': 'startTime',
        'end_time': 'endTime',
        'payment_batch_summaries': 'paymentBatchSummaries'
    }

    def __init__(self, start_time=None, end_time=None, payment_batch_summaries=None):
        """
        InlineResponse200 - a model defined in Swagger
        """

        self._start_time = None
        self._end_time = None
        self._payment_batch_summaries = None

        if start_time is not None:
          self.start_time = start_time
        if end_time is not None:
          self.end_time = end_time
        if payment_batch_summaries is not None:
          self.payment_batch_summaries = payment_batch_summaries

    @property
    def start_time(self):
        """
        Gets the start_time of this InlineResponse200.

        :return: The start_time of this InlineResponse200.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this InlineResponse200.

        :param start_time: The start_time of this InlineResponse200.
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """
        Gets the end_time of this InlineResponse200.

        :return: The end_time of this InlineResponse200.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this InlineResponse200.

        :param end_time: The end_time of this InlineResponse200.
        :type: datetime
        """

        self._end_time = end_time

    @property
    def payment_batch_summaries(self):
        """
        Gets the payment_batch_summaries of this InlineResponse200.

        :return: The payment_batch_summaries of this InlineResponse200.
        :rtype: list[InlineResponse200PaymentBatchSummaries]
        """
        return self._payment_batch_summaries

    @payment_batch_summaries.setter
    def payment_batch_summaries(self, payment_batch_summaries):
        """
        Sets the payment_batch_summaries of this InlineResponse200.

        :param payment_batch_summaries: The payment_batch_summaries of this InlineResponse200.
        :type: list[InlineResponse200PaymentBatchSummaries]
        """

        self._payment_batch_summaries = payment_batch_summaries

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other