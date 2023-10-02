def ispangram(str) -> bool:
  """
    Check if the given string is a pangram (contains all letters of the alphabet).

    Parameters:
        str (str): Input string.

    Returns:
        bool: True if the string is a pangram, False otherwise.

    >>>ispangram("the quick brown fox jumps over the lazy dog")
    True
    >>>ispangram(' sibsiba')
    False

    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
 
    return True


