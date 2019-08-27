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


class TssV2TransactionsGet200ResponseOrderInformationLineItems(object):
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
        'product_code': 'str',
        'product_name': 'str',
        'product_sku': 'str',
        'tax_amount': 'str',
        'quantity': 'int',
        'unit_price': 'str',
        'fulfillment_type': 'str'
    }

    attribute_map = {
        'product_code': 'productCode',
        'product_name': 'productName',
        'product_sku': 'productSku',
        'tax_amount': 'taxAmount',
        'quantity': 'quantity',
        'unit_price': 'unitPrice',
        'fulfillment_type': 'fulfillmentType'
    }

    def __init__(self, product_code=None, product_name=None, product_sku=None, tax_amount=None, quantity=None, unit_price=None, fulfillment_type=None):
        """
        TssV2TransactionsGet200ResponseOrderInformationLineItems - a model defined in Swagger
        """

        self._product_code = None
        self._product_name = None
        self._product_sku = None
        self._tax_amount = None
        self._quantity = None
        self._unit_price = None
        self._fulfillment_type = None

        if product_code is not None:
          self.product_code = product_code
        if product_name is not None:
          self.product_name = product_name
        if product_sku is not None:
          self.product_sku = product_sku
        if tax_amount is not None:
          self.tax_amount = tax_amount
        if quantity is not None:
          self.quantity = quantity
        if unit_price is not None:
          self.unit_price = unit_price
        if fulfillment_type is not None:
          self.fulfillment_type = fulfillment_type

    @property
    def product_code(self):
        """
        Gets the product_code of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        Type of product. This value is used to determine the category that the product is in: electronic, handling, physical, service, or shipping. The default value is **default**.  For a payment, when you set this field to a value other than default or any of the values related to shipping and handling, below fields _quantity_, _productName_, and _productSKU_ are required. 

        :return: The product_code of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        :rtype: str
        """
        return self._product_code

    @product_code.setter
    def product_code(self, product_code):
        """
        Sets the product_code of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        Type of product. This value is used to determine the category that the product is in: electronic, handling, physical, service, or shipping. The default value is **default**.  For a payment, when you set this field to a value other than default or any of the values related to shipping and handling, below fields _quantity_, _productName_, and _productSKU_ are required. 

        :param product_code: The product_code of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        :type: str
        """
        if product_code is not None and len(product_code) > 255:
            raise ValueError("Invalid value for `product_code`, length must be less than or equal to `255`")

        self._product_code = product_code

    @property
    def product_name(self):
        """
        Gets the product_name of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        For PAYMENT and CAPTURE API, this field is required when above _productCode_ is not **default** or one of the values related to shipping and handling. 

        :return: The product_name of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """
        Sets the product_name of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        For PAYMENT and CAPTURE API, this field is required when above _productCode_ is not **default** or one of the values related to shipping and handling. 

        :param product_name: The product_name of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        :type: str
        """
        if product_name is not None and len(product_name) > 255:
            raise ValueError("Invalid value for `product_name`, length must be less than or equal to `255`")

        self._product_name = product_name

    @property
    def product_sku(self):
        """
        Gets the product_sku of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        Identification code for the product. For PAYMENT and CAPTURE API, this field is required when above _productCode_ is not **default** or one of the values related to shipping and/or handling. 

        :return: The product_sku of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        :rtype: str
        """
        return self._product_sku

    @product_sku.setter
    def product_sku(self, product_sku):
        """
        Sets the product_sku of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        Identification code for the product. For PAYMENT and CAPTURE API, this field is required when above _productCode_ is not **default** or one of the values related to shipping and/or handling. 

        :param product_sku: The product_sku of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        :type: str
        """
        if product_sku is not None and len(product_sku) > 255:
            raise ValueError("Invalid value for `product_sku`, length must be less than or equal to `255`")

        self._product_sku = product_sku

    @property
    def tax_amount(self):
        """
        Gets the tax_amount of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        Total tax to apply to the product. This value cannot be negative. The tax amount and the offer amount must be in the same currency. The tax amount field is additive.  The following example uses a two-exponent currency such as USD:  1. You include each line item in your request.     - 1st line item has `amount=10.00`, `quantity=1`, and `taxAmount=0.80`     - 2nd line item has `amount=20.00`, `quantity=1`, and `taxAmount=1.60` 2. The total amount authorized will be 32.40, not 30.00 with 2.40 of tax included.  This field is frequently used for Level II and Level III transactions.  For details, see `tax_amount` field description in [Level II and Level III Processing Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :return: The tax_amount of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        :rtype: str
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """
        Sets the tax_amount of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        Total tax to apply to the product. This value cannot be negative. The tax amount and the offer amount must be in the same currency. The tax amount field is additive.  The following example uses a two-exponent currency such as USD:  1. You include each line item in your request.     - 1st line item has `amount=10.00`, `quantity=1`, and `taxAmount=0.80`     - 2nd line item has `amount=20.00`, `quantity=1`, and `taxAmount=1.60` 2. The total amount authorized will be 32.40, not 30.00 with 2.40 of tax included.  This field is frequently used for Level II and Level III transactions.  For details, see `tax_amount` field description in [Level II and Level III Processing Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :param tax_amount: The tax_amount of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        :type: str
        """
        if tax_amount is not None and len(tax_amount) > 15:
            raise ValueError("Invalid value for `tax_amount`, length must be less than or equal to `15`")

        self._tax_amount = tax_amount

    @property
    def quantity(self):
        """
        Gets the quantity of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        For a payment or capture, this field is required when _productCode_ is not **default** or one of the values related to shipping and handling. 

        :return: The quantity of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        For a payment or capture, this field is required when _productCode_ is not **default** or one of the values related to shipping and handling. 

        :param quantity: The quantity of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        :type: int
        """
        if quantity is not None and quantity > 999999999:
            raise ValueError("Invalid value for `quantity`, must be a value less than or equal to `999999999`")
        if quantity is not None and quantity < 1:
            raise ValueError("Invalid value for `quantity`, must be a value greater than or equal to `1`")

        self._quantity = quantity

    @property
    def unit_price(self):
        """
        Gets the unit_price of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        Per-item price of the product. This value cannot be negative. You can include a decimal point (.), but you cannot include any other special characters. CyberSource truncates the amount to the correct number of decimal places.  For processor-specific information, see the amount field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The unit_price of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        :rtype: str
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """
        Sets the unit_price of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        Per-item price of the product. This value cannot be negative. You can include a decimal point (.), but you cannot include any other special characters. CyberSource truncates the amount to the correct number of decimal places.  For processor-specific information, see the amount field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param unit_price: The unit_price of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        :type: str
        """
        if unit_price is not None and len(unit_price) > 15:
            raise ValueError("Invalid value for `unit_price`, length must be less than or equal to `15`")

        self._unit_price = unit_price

    @property
    def fulfillment_type(self):
        """
        Gets the fulfillment_type of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        The description for this field is not available.

        :return: The fulfillment_type of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        :rtype: str
        """
        return self._fulfillment_type

    @fulfillment_type.setter
    def fulfillment_type(self, fulfillment_type):
        """
        Sets the fulfillment_type of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        The description for this field is not available.

        :param fulfillment_type: The fulfillment_type of this TssV2TransactionsGet200ResponseOrderInformationLineItems.
        :type: str
        """

        self._fulfillment_type = fulfillment_type

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
        if not isinstance(other, TssV2TransactionsGet200ResponseOrderInformationLineItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
