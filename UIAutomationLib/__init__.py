from .datepicker import DatePicker
from .dropdown import Dropdown
from .textarea import TextArea
from .textfield import TextField

class UIAutomationLib(DatePicker,Dropdown,TextArea,TextField):
    """Unified library combining all UI element keywords"""
    pass