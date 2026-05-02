# Imports
from datetime import datetime, timezone
from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass

# Types


# Types: Immutable typed types
# ============================================================================


@dataclass(frozen=True)
class Valid_Action:
    # Class variables and Constants

    _DEFAULT_ACTION_VALID = True
    _DEFAULT_CONSISTENCY_NAME = str('')
    _DEFAULT_CONSISTENCY_MESSAGE = str('')

    # Constructor | Constructors

    # Property | Properties

    is_valid: bool = _DEFAULT_ACTION_VALID
    consistency_name: str = _DEFAULT_CONSISTENCY_NAME
    consistency_message: str = _DEFAULT_CONSISTENCY_MESSAGE

    # Method | Methods


class Valid_Action_Set:
    # Class variables and Constants

    # Constructor | Constructors
    def __init__(self):
        self._actions: dict[str, Valid_Action] = {}

    # Property | Properties
    @property
    def actions(self) -> dict[str, Valid_Action]:
        return self._actions

    @property
    @actions.setter
    def actions(self, validation: Valid_Action) -> None:
        self.actions[validation.consistency_name] = validation

    # Method | Methods

    def is_valid(self) -> bool:
        valid = True
        for validation_result in self.actions.values():
            valid = valid and validation_result.is_valid
        return valid

    def get_consistencies(self, valid=None) -> list[str, str]:
        return [
            f"'{k}': '{v}'"
            for k, v in self.actions.items()
            if v.is_valid == valid or valid is None
        ]


# Types: Abstract classes / Interfaces
# ============================================================================


class Operation(ABC):
    # Class variables and Constants

    _DEFAULT_TIMEZONE_UTC = timezone.utc

    # Constructor | Constructors

    @abstractmethod
    def __init__(self, value: float): ...

    # Property | Properties
    @property
    @abstractmethod
    def time_stamp(self) -> None: ...

    @property
    @abstractmethod
    def value(self) -> float: ...

    # Method | Methods

    @abstractmethod
    def _operation_is_valid(
        self, value: float, valid_action_set: Valid_Action_Set
    ) -> Valid_Action: ...

    # def operation_type_is_valid(
    #         self, operation, target_operation, valid_action_set
    #     ):
    #         if not not issubclass(operation, BankTransaction):
    #             validation = Valid_Action(
    #                 False,
    #                 f'operation_type_{target_operation.__class__.name}',
    #                 f"Operation '{operation}' is not a type of {target_operation.__class__.name}'.",
    #             )
    #             valid_action_set.actions[validation.consistency_name] = validation


class BankTransaction(ABC):
    # Class variables and Constants

    # Constructor | Constructors

    # Property | Properties

    # Method | Methods

    # TODO: BankTransaction: Apply typing to method's  parameters?
    @abstractmethod
    def register(sel, account) -> tuple[None, Valid_Action]: ...

    @abstractmethod
    def _time_stamp(self, use_time_zone=Operation._DEFAULT_TIMEZONE_UTC) -> None: ...


# Types: Concrete classes
# ============================================================================


class Deposit(Operation, BankTransaction):
    # Class variables and Constants

    _MINIMUM_VALUE_EXPECTED: float = 0

    # Constructor | Constructors

    def __init__(self, value):
        validation = self.valid_operation(value)
        if not validation.is_valid:
            raise ValueError(validation.consistency_message)

        self._value = value
        self._time_stamp(self)

    # Property | Properties

    @property
    def time_stamp(self) -> datetime:
        return self.time_stamp

    @property
    def value(self) -> float:
        return self._value

    # Method | Methods

    def _time_stamp(self, use_time_zone=Operation._DEFAULT_TIMEZONE_UTC) -> None:
        self.time_stamp = use_time_zone

    def _operation_is_valid(self, value, validations: Valid_Action_Set = None) -> None:
        if validations is None:
            validations = Valid_Action_Set()

        self.__operation_type_is_valid(value, validations)
        self.__operation_value_is_valid(value, validations)

    def __operation_type_is_valid(
        self, operation, validations: Valid_Action_Set
    ) -> None:

        consistency_name = f'operation_{self.__class__.__name__}_type'

        match operation:
            case Deposit() | float() | int():
                validation = Valid_Action(True, consistency_name)
                validations.actions(validation)

            case _:
                consistency_details = f"Parameter operation is not a subclass of '{self.__class__.__name__} | float | int', it's '{type(operation)}'"
                validation = Valid_Action(False, consistency_name, consistency_details)
                validations.actions(validation)

    def __operation_value_is_valid(self, value, validations: Valid_Action_Set) -> None:
        consistency_name = f'operation_{self.__class__.__name__}_value'

        if value > self._MINIMUM_VALUE_EXPECTED:
            validation = Valid_Action(True, consistency_name, '')

        else:
            consistency_details = f"Value '{value}' less than the minimum expected value '{self._MINIMUM_VALUE_EXPECTED} 'for operation '{self.__class__.__name__}'."
            validation = Valid_Action(False, consistency_name, consistency_details)

        validations.actions(validation)

    def register(sel, account) -> tuple[None, Valid_Action]:
        pass


class Withdrawal(Operation, BankTransaction):
    # Class variables and Constants

    _MINIMUM_VALUE_EXPECTED: float = -1

    # Constructor | Constructors

    def __init__(self, value):
        super().__init__()
        validation = self._operation_is_valid(value)
        if not validation.is_valid:
            return ValueError(validation.consistency_message)

        self._value = value
        self._time_stamp(self)

    # Property | Properties

    @property
    def time_stamp(self) -> datetime:
        return self.time_stamp

    @property
    def value(self) -> float:
        return self._value

    # Method | Methods

    def _time_stamp(self, use_time_zone=Operation._DEFAULT_TIMEZONE_UTC) -> None:
        self.time_stamp = use_time_zone

    def _operation_is_valid(self, value, validations: Valid_Action_Set = None) -> None:
        if validations is None:
            validations = Valid_Action_Set()

        self.__operation_type_is_valid(value, validations)
        self.__operation_value_is_valid(value, validations)

    def __operation_type_is_valid(
        self, operation, validations: Valid_Action_Set
    ) -> None:

        consistency_name = f'operation_{self.__class__.__name__}_type'

        match operation:
            case Withdrawal() | float() | int():
                validation = Valid_Action(True, consistency_name)
                validations.actions(validation)

            case _:
                consistency_details = f"Parameter operation is not a subclass of '{self.__class__.__name__} | float | int', it's '{type(operation)}'"
                validation = Valid_Action(False, consistency_name, consistency_details)
                validations.actions(validation)

    def __operation_value_is_valid(self, value, validations: Valid_Action_Set) -> None:
        consistency_name = f'operation_{self.__class__.__name__}_value'

        if value > self._MINIMUM_VALUE_EXPECTED:
            validation = Valid_Action(True, consistency_name, '')

        else:
            consistency_details = f"Value '{value}' greater than the minimum expected value '{self._MINIMUM_VALUE_EXPECTED} 'for operation '{self.__class__.__name__}'."
            validation = Valid_Action(False, consistency_name, consistency_details)

        validations.actions(validation)

    def register(self, account) -> tuple[None, Valid_Action]:
        pass


# TODO: TransactionHistory class: Apply type to Lists ?
class TransactionHistory:
    # Class variables and Constants
    # Constructor | Constructors
    def __init__(self, transactions=[]):
        self._transactions = transactions

    # Property | Properties
    @property
    def transactions(self) -> list:
        return self._transactions

    # Method | Methods
    def add_transaction(self, bank_transaction) -> tuple[None, ValueError]:
        if not isinstance(bank_transaction, BankTransaction):
            return ValueError(
                f'transaction {bank_transaction}  is not type of Bank Transaction.'
            )

        self._transactions.append(bank_transaction)


# TODO: Customer class: Apply type to Lists ?
class Customer:
    # Class variables and Constants

    # Constructor | Constructors

    def __init__(self, address: str, accounts=[]):
        self._address = address
        self._accounts = accounts

    # Property | Properties
    @property
    def address(self) -> str:
        return self._address

    @property
    def accounts(self) -> list:
        return self._accounts

    # Method | Methods
    @abstractmethod
    def perform_transaction(self, account, bank_transaction): ...

    @abstractmethod
    def add_account(self, account): ...


class NaturalPerson(Customer):
    # Class variables and Constants

    # Constructor | Constructors

    def __init__(self, cpf: str, name: str, birth_date: datetime, **kw):
        super().__init__(**kw)
        self._cpf = cpf
        self._name = name
        self._birth_date = birth_date

    # Property | Properties

    @property
    def cpf(self) -> str:
        return self._cpf

    @property
    def name(self) -> str:
        return self._name

    @property
    def birth_date(self) -> datetime:
        return self._birth_date

    # Method | Methods

    def perform_transaction(self, account, bank_transaction): ...

    def add_account(self, account) -> None:
        self._accounts.append(account)


class Account:
    # Class variables and Constants

    _DEFAULT_BRANCH = '0001'
    _DEFAULT_BALANCE = float(0.0)

    # Constructor | Constructors

    def __init__(self, balance: float, number: int, branch: str, customer: Customer):
        self._balance: float = balance
        self._number: int = number
        self._branch: str = branch
        self._customer: Customer = customer
        self._transaction_history: TransactionHistory = TransactionHistory()

        # Factory methods

        @classmethod
        def new_account(cls, customer, account_number):
            return cls(
                number=account_number,
                customer=customer,
                balance=Account._DEFAULT_BALANCE,
                branch=Account._DEFAULT_BRANCH,
            )

        # Property | Properties

        @property
        def balance(self) -> float:
            return self._balance

        # Method | Methods
        def withdraw(self, withdraw_value, validations: Valid_Action_Set) -> None:
            if validations is None:
                validations = Valid_Action_Set()

            consistency_name = 'account_withdraw_operation'

            if withdraw_value > -1:
                consistency_details = (
                    'Insufficient account balance to complete the transaction.'
                )
                validation = Valid_Action(False, consistency_name, consistency_details)
                validations.actions(validation)
                return

            if withdraw_value > self.balance:
                consistency_name = 'account_operation_withdraw'
                consistency_details = (
                    'Insufficient account balance to complete the transaction.'
                )
                validation = Valid_Action(False, consistency_name, consistency_details)
                validations.actions(validation)
                return

            self._balance += withdraw_value

        def deposit(self):
            pass


class CheckingAccount(Account):
    # Class variables and Constants
    # Constructor | Constructors
    def __init__(self, limit, withdrawal_limit, **kw):
        super().__init__(**kw)
        self._limit = limit
        self._withdrawal_limit = withdrawal_limit

    # Property | Properties
    @property
    def limit(self):
        return self._limit

    @property
    def withdrawal_limit(self):
        return self._withdrawal_limit

        # Method | Methods

        def _account_operation_is_valid(
            self, operation, target_operation, validations: Valid_Action_Set
        ) -> None:

            if validations is None:
                validations = Valid_Action_Set()

            self.__operation_type_is_valid(operation, target_operation, validations)

        def withdraw(self, withdraw_value) -> tuple[bool, Valid_Action_Set]:
            operation = Withdrawal(withdraw_value)
            validations = _account_operation_is_valid(operation, Withdrawal.__class__)

            if not validations.is_valid():
                return (False, validations)

        def deposit(self):
            pass


# ============================================================================

# tests
# a = Deposit(-2)
# print(a)

# vs = Valid_Action_Set()
# vs.actions['t1'] = Valid_Action()
# vs.actions['t2'] = Valid_Action()
# vs.actions['t3'] = Valid_Action(
#     is_valid=False, consistency_name='t3', consistency_message='error'
# )
# vs.actions['t4'] = Valid_Action(
#     is_valid=False, consistency_name='t4', consistency_message='error'
# )

# print(vs.is_valid())
# print(vs.get_consistencies())
# print('=' * 100)
# print(vs.get_consistencies(False))
# print('=' * 100)
# print(vs.get_consistencies(True))
