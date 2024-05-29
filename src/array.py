class Array:
    """
    A custom array class that enforces type consistency and provides basic array operations.
    """

    def __init__(self, data_type):
        """
        Initializes the Array with a specified data type.

        :param data_type: The data type for the array elements.
        """
        self.data_type = data_type
        self.array = []

    def _validate_type(self, value):
        """
        Validates that the value is of the correct data type.

        :param value: The value to validate.
        :raises TypeError: If the value is not of the specified data type.
        """
        if not isinstance(value, self.data_type):
            raise TypeError(f"Expected {self.data_type.__name__}, got {type(value).__name__}")

    def append(self, value):
        """
        Appends an element to the end of the array.

        :param value: The value to append to the array.
        """
        self._validate_type(value)
        self.array.append(value)

    def insert(self, index, value):
        """
        Inserts an element at a specified position in the array.

        :param index: The index at which to insert the value.
        :param value: The value to insert into the array.
        """
        self._validate_type(value)
        self.array.insert(index, value)

    def remove(self, value):
        """
        Removes the first occurrence of a value from the array.

        :param value: The value to remove from the array.
        """
        self.array.remove(value)

    def pop(self, index=-1):
        """
        Removes and returns the element at the specified index.

        :param index: The index of the element to pop. Defaults to -1 (last element).
        :returns: The element removed from the array.
        """
        return self.array.pop(index)

    def __getitem__(self, index):
        """
        Retrieves the element at the specified index.

        :param index: The index of the element to retrieve.
        :returns: The element at the specified index.
        """
        return self.array[index]

    def __setitem__(self, index, value):
        """
        Sets the element at the specified index.

        :param index: The index of the element to set.
        :param value: The new value for the element.
        :raises TypeError: If the value is not of the specified data type.
        """
        self._validate_type(value)
        self.array[index] = value

    def __len__(self):
        """
        Returns the number of elements in the array.

        :returns: The number of elements in the array.
        """
        return len(self.array)

    def __repr__(self):
        """
        Returns a string representation of the array.

        :returns: A string representation of the array.
        """
        return f"Array({self.data_type.__name__}, {self.array})"
