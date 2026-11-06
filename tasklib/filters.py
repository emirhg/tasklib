import abc
from .serializing import SerializingObject


class TaskFilter(object):
    """
    Abstract base class that defines interface of a TaskFilter.
    """

    @abc.abstractmethod
    def add_filter(self, arg):
        """
        Processes an non-keyword filter.
        """
        pass

    @abc.abstractmethod
    def add_filter_param(self, key, value):
        """
        Processes a keyword filter.
        """
        pass

    @abc.abstractmethod
    def clone(self):
        """
        Returns a new deep copy of itself.
        """
        pass


class TaskWarriorFilter(TaskFilter, SerializingObject):
    """
    A set of parameters to filter the task list with.
    """

    def __init__(self, backend, filter_params=None):
        self.filter_params = filter_params or []
        super(TaskFilter, self).__init__(backend)

    def add_filter(self, filter_str):
        self.filter_params.append(filter_str)

    def add_filter_param(self, key, value):
        key = key.replace('__', '.')

        # Replace the value with empty string, since that is the
        # convention in TW for empty values
        attribute_key = key.split('.')[0]

        # Since this is user input, we need to normalize before we serialize
        value = self._normalize(attribute_key, value)
        value = self._serialize(attribute_key, value)

        # If we are filtering by uuid:, do not use uuid keyword
        # due to TW-1452 bug
        if key == 'uuid':
            self.filter_params.insert(0, value)
        else:
            # Surround value with aphostrophes unless it's a empty string
            value = "'%s'" % value if value else ''

            self.filter_params.append("{0}:{1}".format(key, value))

    def get_filter_params(self):
        return [f for f in self.filter_params if f]

    def clone(self):
        c = self.__class__(self.backend)
        c.filter_params = list(self.filter_params)
        return c
