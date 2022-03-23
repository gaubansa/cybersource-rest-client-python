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


class TssV2TransactionsGet200ResponseProcessorInformation(object):
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
        'processor': 'TssV2TransactionsGet200ResponseProcessorInformationProcessor',
        'multi_processor_routing': 'list[TssV2TransactionsGet200ResponseProcessorInformationMultiProcessorRouting]',
        'transaction_id': 'str',
        'network_transaction_id': 'str',
        'retrieval_reference_number': 'str',
        'response_id': 'str',
        'approval_code': 'str',
        'response_code': 'str',
        'avs': 'PtsV2PaymentsPost201ResponseProcessorInformationAvs',
        'card_verification': 'Riskv1decisionsProcessorInformationCardVerification',
        'ach_verification': 'PtsV2PaymentsPost201ResponseProcessorInformationAchVerification',
        'electronic_verification_results': 'TssV2TransactionsGet200ResponseProcessorInformationElectronicVerificationResults',
        'system_trace_audit_number': 'str',
        'response_code_source': 'str',
        'payment_account_reference_number': 'str'
    }

    attribute_map = {
        'processor': 'processor',
        'multi_processor_routing': 'multiProcessorRouting',
        'transaction_id': 'transactionId',
        'network_transaction_id': 'networkTransactionId',
        'retrieval_reference_number': 'retrievalReferenceNumber',
        'response_id': 'responseId',
        'approval_code': 'approvalCode',
        'response_code': 'responseCode',
        'avs': 'avs',
        'card_verification': 'cardVerification',
        'ach_verification': 'achVerification',
        'electronic_verification_results': 'electronicVerificationResults',
        'system_trace_audit_number': 'systemTraceAuditNumber',
        'response_code_source': 'responseCodeSource',
        'payment_account_reference_number': 'paymentAccountReferenceNumber'
    }

    def __init__(self, processor=None, multi_processor_routing=None, transaction_id=None, network_transaction_id=None, retrieval_reference_number=None, response_id=None, approval_code=None, response_code=None, avs=None, card_verification=None, ach_verification=None, electronic_verification_results=None, system_trace_audit_number=None, response_code_source=None, payment_account_reference_number=None):
        """
        TssV2TransactionsGet200ResponseProcessorInformation - a model defined in Swagger
        """

        self._processor = None
        self._multi_processor_routing = None
        self._transaction_id = None
        self._network_transaction_id = None
        self._retrieval_reference_number = None
        self._response_id = None
        self._approval_code = None
        self._response_code = None
        self._avs = None
        self._card_verification = None
        self._ach_verification = None
        self._electronic_verification_results = None
        self._system_trace_audit_number = None
        self._response_code_source = None
        self._payment_account_reference_number = None

        if processor is not None:
          self.processor = processor
        if multi_processor_routing is not None:
          self.multi_processor_routing = multi_processor_routing
        if transaction_id is not None:
          self.transaction_id = transaction_id
        if network_transaction_id is not None:
          self.network_transaction_id = network_transaction_id
        if retrieval_reference_number is not None:
          self.retrieval_reference_number = retrieval_reference_number
        if response_id is not None:
          self.response_id = response_id
        if approval_code is not None:
          self.approval_code = approval_code
        if response_code is not None:
          self.response_code = response_code
        if avs is not None:
          self.avs = avs
        if card_verification is not None:
          self.card_verification = card_verification
        if ach_verification is not None:
          self.ach_verification = ach_verification
        if electronic_verification_results is not None:
          self.electronic_verification_results = electronic_verification_results
        if system_trace_audit_number is not None:
          self.system_trace_audit_number = system_trace_audit_number
        if response_code_source is not None:
          self.response_code_source = response_code_source
        if payment_account_reference_number is not None:
          self.payment_account_reference_number = payment_account_reference_number

    @property
    def processor(self):
        """
        Gets the processor of this TssV2TransactionsGet200ResponseProcessorInformation.

        :return: The processor of this TssV2TransactionsGet200ResponseProcessorInformation.
        :rtype: TssV2TransactionsGet200ResponseProcessorInformationProcessor
        """
        return self._processor

    @processor.setter
    def processor(self, processor):
        """
        Sets the processor of this TssV2TransactionsGet200ResponseProcessorInformation.

        :param processor: The processor of this TssV2TransactionsGet200ResponseProcessorInformation.
        :type: TssV2TransactionsGet200ResponseProcessorInformationProcessor
        """

        self._processor = processor

    @property
    def multi_processor_routing(self):
        """
        Gets the multi_processor_routing of this TssV2TransactionsGet200ResponseProcessorInformation.
        An array of object that contains the list of acquirer response codes & reasons if a transaction is routed to multiple acquirers.

        :return: The multi_processor_routing of this TssV2TransactionsGet200ResponseProcessorInformation.
        :rtype: list[TssV2TransactionsGet200ResponseProcessorInformationMultiProcessorRouting]
        """
        return self._multi_processor_routing

    @multi_processor_routing.setter
    def multi_processor_routing(self, multi_processor_routing):
        """
        Sets the multi_processor_routing of this TssV2TransactionsGet200ResponseProcessorInformation.
        An array of object that contains the list of acquirer response codes & reasons if a transaction is routed to multiple acquirers.

        :param multi_processor_routing: The multi_processor_routing of this TssV2TransactionsGet200ResponseProcessorInformation.
        :type: list[TssV2TransactionsGet200ResponseProcessorInformationMultiProcessorRouting]
        """

        self._multi_processor_routing = multi_processor_routing

    @property
    def transaction_id(self):
        """
        Gets the transaction_id of this TssV2TransactionsGet200ResponseProcessorInformation.
        Network transaction identifier (TID). You can use this value to identify a specific transaction when you are discussing the transaction with your processor. Not all processors provide this value.  Returned by the authorization service.  #### PIN debit Transaction identifier generated by the processor.  Returned by PIN debit credit.  #### GPX Processor transaction ID.  #### Cielo For Cielo, this value is the non-sequential unit (NSU) and is supported for all transactions. The value is generated by Cielo or the issuing bank.  #### Comercio Latino For Comercio Latino, this value is the proof of sale or non-sequential unit (NSU) number generated by the acquirers Cielo and Rede, or the issuing bank.  #### CyberSource through VisaNet and GPN For details about this value for CyberSource through VisaNet and GPN, see \"Network Transaction Identifiers\" in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### Moneris This value identifies the transaction on a host system. It contains the following information: - Terminal used to process the transaction - Shift during which the transaction took place - Batch number - Transaction number within the batch You must store this value. If you give the customer a receipt, display this value on the receipt.  **Example** For the value 66012345001069003: - Terminal ID = 66012345 - Shift number = 001 - Batch number = 069 - Transaction number = 003 

        :return: The transaction_id of this TssV2TransactionsGet200ResponseProcessorInformation.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """
        Sets the transaction_id of this TssV2TransactionsGet200ResponseProcessorInformation.
        Network transaction identifier (TID). You can use this value to identify a specific transaction when you are discussing the transaction with your processor. Not all processors provide this value.  Returned by the authorization service.  #### PIN debit Transaction identifier generated by the processor.  Returned by PIN debit credit.  #### GPX Processor transaction ID.  #### Cielo For Cielo, this value is the non-sequential unit (NSU) and is supported for all transactions. The value is generated by Cielo or the issuing bank.  #### Comercio Latino For Comercio Latino, this value is the proof of sale or non-sequential unit (NSU) number generated by the acquirers Cielo and Rede, or the issuing bank.  #### CyberSource through VisaNet and GPN For details about this value for CyberSource through VisaNet and GPN, see \"Network Transaction Identifiers\" in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### Moneris This value identifies the transaction on a host system. It contains the following information: - Terminal used to process the transaction - Shift during which the transaction took place - Batch number - Transaction number within the batch You must store this value. If you give the customer a receipt, display this value on the receipt.  **Example** For the value 66012345001069003: - Terminal ID = 66012345 - Shift number = 001 - Batch number = 069 - Transaction number = 003 

        :param transaction_id: The transaction_id of this TssV2TransactionsGet200ResponseProcessorInformation.
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def network_transaction_id(self):
        """
        Gets the network_transaction_id of this TssV2TransactionsGet200ResponseProcessorInformation.
        Same value as `processorInformation.transactionId`

        :return: The network_transaction_id of this TssV2TransactionsGet200ResponseProcessorInformation.
        :rtype: str
        """
        return self._network_transaction_id

    @network_transaction_id.setter
    def network_transaction_id(self, network_transaction_id):
        """
        Sets the network_transaction_id of this TssV2TransactionsGet200ResponseProcessorInformation.
        Same value as `processorInformation.transactionId`

        :param network_transaction_id: The network_transaction_id of this TssV2TransactionsGet200ResponseProcessorInformation.
        :type: str
        """

        self._network_transaction_id = network_transaction_id

    @property
    def retrieval_reference_number(self):
        """
        Gets the retrieval_reference_number of this TssV2TransactionsGet200ResponseProcessorInformation.
        #### Ingenico ePayments Unique number that CyberSource generates to identify the transaction. You can use this value to identify transactions in the Ingenico ePayments Collections Report, which provides settlement information. Contact customer support for information about the report.  ### CyberSource through VisaNet Retrieval request number. 

        :return: The retrieval_reference_number of this TssV2TransactionsGet200ResponseProcessorInformation.
        :rtype: str
        """
        return self._retrieval_reference_number

    @retrieval_reference_number.setter
    def retrieval_reference_number(self, retrieval_reference_number):
        """
        Sets the retrieval_reference_number of this TssV2TransactionsGet200ResponseProcessorInformation.
        #### Ingenico ePayments Unique number that CyberSource generates to identify the transaction. You can use this value to identify transactions in the Ingenico ePayments Collections Report, which provides settlement information. Contact customer support for information about the report.  ### CyberSource through VisaNet Retrieval request number. 

        :param retrieval_reference_number: The retrieval_reference_number of this TssV2TransactionsGet200ResponseProcessorInformation.
        :type: str
        """

        self._retrieval_reference_number = retrieval_reference_number

    @property
    def response_id(self):
        """
        Gets the response_id of this TssV2TransactionsGet200ResponseProcessorInformation.
        Response ID sent from the processor. 

        :return: The response_id of this TssV2TransactionsGet200ResponseProcessorInformation.
        :rtype: str
        """
        return self._response_id

    @response_id.setter
    def response_id(self, response_id):
        """
        Sets the response_id of this TssV2TransactionsGet200ResponseProcessorInformation.
        Response ID sent from the processor. 

        :param response_id: The response_id of this TssV2TransactionsGet200ResponseProcessorInformation.
        :type: str
        """

        self._response_id = response_id

    @property
    def approval_code(self):
        """
        Gets the approval_code of this TssV2TransactionsGet200ResponseProcessorInformation.
        Authorization code. Returned only when the processor returns this value.  The length of this value depends on your processor.  Returned by authorization service.  #### PIN debit Authorization code that is returned by the processor.  Returned by PIN debit credit.  #### Elavon Encrypted Account Number Program The returned value is OFFLINE.  #### TSYS Acquiring Solutions The returned value for a successful zero amount authorization is 000000. 

        :return: The approval_code of this TssV2TransactionsGet200ResponseProcessorInformation.
        :rtype: str
        """
        return self._approval_code

    @approval_code.setter
    def approval_code(self, approval_code):
        """
        Sets the approval_code of this TssV2TransactionsGet200ResponseProcessorInformation.
        Authorization code. Returned only when the processor returns this value.  The length of this value depends on your processor.  Returned by authorization service.  #### PIN debit Authorization code that is returned by the processor.  Returned by PIN debit credit.  #### Elavon Encrypted Account Number Program The returned value is OFFLINE.  #### TSYS Acquiring Solutions The returned value for a successful zero amount authorization is 000000. 

        :param approval_code: The approval_code of this TssV2TransactionsGet200ResponseProcessorInformation.
        :type: str
        """

        self._approval_code = approval_code

    @property
    def response_code(self):
        """
        Gets the response_code of this TssV2TransactionsGet200ResponseProcessorInformation.
        For most processors, this is the error message sent directly from the bank. Returned only when the processor returns this value.  **Important** Do not use this field to evaluate the result of the authorization.  #### PIN debit Response value that is returned by the processor or bank. **Important** Do not use this field to evaluate the results of the transaction request.  Returned by PIN debit credit, PIN debit purchase, and PIN debit reversal.  #### AIBMS If this value is `08`, you can accept the transaction if the customer provides you with identification.  #### Atos This value is the response code sent from Atos and it might also include the response code from the bank. Format: `aa,bb` with the two values separated by a comma and where: - `aa` is the two-digit error message from Atos. - `bb` is the optional two-digit error message from the bank.  #### Comercio Latino This value is the status code and the error or response code received from the processor separated by a colon. Format: [status code]:E[error code] or [status code]:R[response code] Example `2:R06`  #### JCN Gateway Processor-defined detail error code. The associated response category code is in the `processorInformation.responseCategoryCode` field. String (3) 

        :return: The response_code of this TssV2TransactionsGet200ResponseProcessorInformation.
        :rtype: str
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """
        Sets the response_code of this TssV2TransactionsGet200ResponseProcessorInformation.
        For most processors, this is the error message sent directly from the bank. Returned only when the processor returns this value.  **Important** Do not use this field to evaluate the result of the authorization.  #### PIN debit Response value that is returned by the processor or bank. **Important** Do not use this field to evaluate the results of the transaction request.  Returned by PIN debit credit, PIN debit purchase, and PIN debit reversal.  #### AIBMS If this value is `08`, you can accept the transaction if the customer provides you with identification.  #### Atos This value is the response code sent from Atos and it might also include the response code from the bank. Format: `aa,bb` with the two values separated by a comma and where: - `aa` is the two-digit error message from Atos. - `bb` is the optional two-digit error message from the bank.  #### Comercio Latino This value is the status code and the error or response code received from the processor separated by a colon. Format: [status code]:E[error code] or [status code]:R[response code] Example `2:R06`  #### JCN Gateway Processor-defined detail error code. The associated response category code is in the `processorInformation.responseCategoryCode` field. String (3) 

        :param response_code: The response_code of this TssV2TransactionsGet200ResponseProcessorInformation.
        :type: str
        """

        self._response_code = response_code

    @property
    def avs(self):
        """
        Gets the avs of this TssV2TransactionsGet200ResponseProcessorInformation.

        :return: The avs of this TssV2TransactionsGet200ResponseProcessorInformation.
        :rtype: PtsV2PaymentsPost201ResponseProcessorInformationAvs
        """
        return self._avs

    @avs.setter
    def avs(self, avs):
        """
        Sets the avs of this TssV2TransactionsGet200ResponseProcessorInformation.

        :param avs: The avs of this TssV2TransactionsGet200ResponseProcessorInformation.
        :type: PtsV2PaymentsPost201ResponseProcessorInformationAvs
        """

        self._avs = avs

    @property
    def card_verification(self):
        """
        Gets the card_verification of this TssV2TransactionsGet200ResponseProcessorInformation.

        :return: The card_verification of this TssV2TransactionsGet200ResponseProcessorInformation.
        :rtype: Riskv1decisionsProcessorInformationCardVerification
        """
        return self._card_verification

    @card_verification.setter
    def card_verification(self, card_verification):
        """
        Sets the card_verification of this TssV2TransactionsGet200ResponseProcessorInformation.

        :param card_verification: The card_verification of this TssV2TransactionsGet200ResponseProcessorInformation.
        :type: Riskv1decisionsProcessorInformationCardVerification
        """

        self._card_verification = card_verification

    @property
    def ach_verification(self):
        """
        Gets the ach_verification of this TssV2TransactionsGet200ResponseProcessorInformation.

        :return: The ach_verification of this TssV2TransactionsGet200ResponseProcessorInformation.
        :rtype: PtsV2PaymentsPost201ResponseProcessorInformationAchVerification
        """
        return self._ach_verification

    @ach_verification.setter
    def ach_verification(self, ach_verification):
        """
        Sets the ach_verification of this TssV2TransactionsGet200ResponseProcessorInformation.

        :param ach_verification: The ach_verification of this TssV2TransactionsGet200ResponseProcessorInformation.
        :type: PtsV2PaymentsPost201ResponseProcessorInformationAchVerification
        """

        self._ach_verification = ach_verification

    @property
    def electronic_verification_results(self):
        """
        Gets the electronic_verification_results of this TssV2TransactionsGet200ResponseProcessorInformation.

        :return: The electronic_verification_results of this TssV2TransactionsGet200ResponseProcessorInformation.
        :rtype: TssV2TransactionsGet200ResponseProcessorInformationElectronicVerificationResults
        """
        return self._electronic_verification_results

    @electronic_verification_results.setter
    def electronic_verification_results(self, electronic_verification_results):
        """
        Sets the electronic_verification_results of this TssV2TransactionsGet200ResponseProcessorInformation.

        :param electronic_verification_results: The electronic_verification_results of this TssV2TransactionsGet200ResponseProcessorInformation.
        :type: TssV2TransactionsGet200ResponseProcessorInformationElectronicVerificationResults
        """

        self._electronic_verification_results = electronic_verification_results

    @property
    def system_trace_audit_number(self):
        """
        Gets the system_trace_audit_number of this TssV2TransactionsGet200ResponseProcessorInformation.
        This field is returned only for **American Express Direct** and **CyberSource through VisaNet**. Returned by authorization and incremental authorization services.  #### American Express Direct  System trace audit number (STAN). This value identifies the transaction and is useful when investigating a chargeback dispute.  #### CyberSource through VisaNet  System trace number that must be printed on the customer’s receipt. 

        :return: The system_trace_audit_number of this TssV2TransactionsGet200ResponseProcessorInformation.
        :rtype: str
        """
        return self._system_trace_audit_number

    @system_trace_audit_number.setter
    def system_trace_audit_number(self, system_trace_audit_number):
        """
        Sets the system_trace_audit_number of this TssV2TransactionsGet200ResponseProcessorInformation.
        This field is returned only for **American Express Direct** and **CyberSource through VisaNet**. Returned by authorization and incremental authorization services.  #### American Express Direct  System trace audit number (STAN). This value identifies the transaction and is useful when investigating a chargeback dispute.  #### CyberSource through VisaNet  System trace number that must be printed on the customer’s receipt. 

        :param system_trace_audit_number: The system_trace_audit_number of this TssV2TransactionsGet200ResponseProcessorInformation.
        :type: str
        """

        self._system_trace_audit_number = system_trace_audit_number

    @property
    def response_code_source(self):
        """
        Gets the response_code_source of this TssV2TransactionsGet200ResponseProcessorInformation.
        Used by Visa only and contains the response source/reason code that identifies the source of the response decision. 

        :return: The response_code_source of this TssV2TransactionsGet200ResponseProcessorInformation.
        :rtype: str
        """
        return self._response_code_source

    @response_code_source.setter
    def response_code_source(self, response_code_source):
        """
        Sets the response_code_source of this TssV2TransactionsGet200ResponseProcessorInformation.
        Used by Visa only and contains the response source/reason code that identifies the source of the response decision. 

        :param response_code_source: The response_code_source of this TssV2TransactionsGet200ResponseProcessorInformation.
        :type: str
        """

        self._response_code_source = response_code_source

    @property
    def payment_account_reference_number(self):
        """
        Gets the payment_account_reference_number of this TssV2TransactionsGet200ResponseProcessorInformation.
        Visa-generated reference number that identifies a card-present transaction for which you provided one of the following:   - Visa primary account number (PAN)  - Visa-generated token for a PAN  This reference number serves as a link to the cardholder account and to all transactions for that account. This reply field is returned only for CyberSource through VisaNet.  **Note** On CyberSource through VisaNet, the value for this field corresponds to the following data in the TC 33 capture file: - Record: CP01 TCR8 - Position: 79-110 - Field: Payment Account Reference  The TC 33 Capture file contains information about the purchases and refunds that a merchant submits to CyberSource. CyberSource through VisaNet creates the TC 33 Capture file at the end of the day and sends it to the merchant’s acquirer, who uses this information to facilitate end-of-day clearing processing with payment networks. 

        :return: The payment_account_reference_number of this TssV2TransactionsGet200ResponseProcessorInformation.
        :rtype: str
        """
        return self._payment_account_reference_number

    @payment_account_reference_number.setter
    def payment_account_reference_number(self, payment_account_reference_number):
        """
        Sets the payment_account_reference_number of this TssV2TransactionsGet200ResponseProcessorInformation.
        Visa-generated reference number that identifies a card-present transaction for which you provided one of the following:   - Visa primary account number (PAN)  - Visa-generated token for a PAN  This reference number serves as a link to the cardholder account and to all transactions for that account. This reply field is returned only for CyberSource through VisaNet.  **Note** On CyberSource through VisaNet, the value for this field corresponds to the following data in the TC 33 capture file: - Record: CP01 TCR8 - Position: 79-110 - Field: Payment Account Reference  The TC 33 Capture file contains information about the purchases and refunds that a merchant submits to CyberSource. CyberSource through VisaNet creates the TC 33 Capture file at the end of the day and sends it to the merchant’s acquirer, who uses this information to facilitate end-of-day clearing processing with payment networks. 

        :param payment_account_reference_number: The payment_account_reference_number of this TssV2TransactionsGet200ResponseProcessorInformation.
        :type: str
        """

        self._payment_account_reference_number = payment_account_reference_number

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
        if not isinstance(other, TssV2TransactionsGet200ResponseProcessorInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
