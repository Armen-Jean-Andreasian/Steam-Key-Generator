import string
import random


class Generator:
    @classmethod
    def _chars_generator(cls, length_of_chars: int) -> str:
        """
        Generates a random string of characters.

        :param length_of_chars: The length of the generated string.
        :return: A random string of characters.
        """
        all_characters = string.ascii_uppercase + string.digits
        result = ''
        count = 0

        while count < length_of_chars:
            random_character = random.choice(all_characters)
            result += random_character
            count += 1

        return result

    @classmethod
    def _add_separator(cls, raw: str) -> str:
        """
        Add a separator after every 5 characters in the input string.

        :param raw: The input string.
        :return: The input string with separators added.
        """
        # result = '-'.join(raw[i:i + 5] for i in range(0, len(raw), 5)) but I like readability, so:

        result = ''
        count = 0

        for i in raw:
            if count < 5:
                result += i
                count += 1

            elif count == 5:
                result += '-'
                result += i
                count = 1

        return result


class KeyGenerator(Generator):
    """
    This class generates Steam-like keys with different formats based on the specified generation type.


    Params: generation_type (str):

    - *Standard*: generates a 15-symbol Steam key: CVOLP-EZ67M-FCKQF
    - *Extended*: generates a 25-symbol Steam key: CVOLP-EZ67M-FCKQF-UNYMG-K4KJN
    - *Special*: generates a 15-symbol special Steam key: 237ABCDGHJLPRST 23

    For more information about Steam key types, visit: https://store.steampowered.com/account/registerkey
    """

    def __str__(self):
        return (
            '''
            Generates Steam-like keys with different formats based on the specified generation type.
            
            1. Standard keys: generates a 15-symbol Steam key: CVOLP-EZ67M-FCKQF
            2. Extended keys: generates a 25-symbol Steam key: CVOLP-EZ67M-FCKQF-UNYMG-K4KJN
            3. Special keys: generates a 15-symbol special Steam key: 237ABCDGHJLPRST 23
            
            For more information about Steam key types, visit: https: // store.steampowered.com/account/registerkey
            '''
        )

    def main(self, generation_type: str):

        if generation_type == 'Standard':
            return self.generate_standard_key()
        elif generation_type == 'Extended':
            return self.generate_extended_key()
        elif generation_type == 'Special':
            return self.generate_special_key()
        else:
            raise ValueError("Invalid generation_type. Please use 'Standard', 'Extended', or 'Special'.")

    def generate_standard_key(self) -> str:
        """
        Standard-key
        :return: generates a 15-symbol Steam key: CVOLP-EZ67M-FCKQF
        """
        raw = self._chars_generator(length_of_chars=15)
        result = self._add_separator(raw)
        return result

    def generate_extended_key(self) -> str:
        """
        Extended-key
        :return: Generates a 25-symbol Steam key: CVOLP-EZ67M-FCKQF-UNYMG-K4KJN

        """
        raw = self._chars_generator(length_of_chars=25)

        result = self._add_separator(raw)
        return result

    def generate_special_key(self) -> str:
        """
        Special-key
        :return: generates a 15-symbol special Steam key: 237ABCDGHJLPRST 23

        *IMPORTANT*: This type of keys is only announced by Steam, but there's not much information about them on the
        internet.
        """
        raw = self._chars_generator(length_of_chars=17)
        part1 = raw[:-2]
        part2 = raw[-2:]
        result = part1 + ' ' + part2
        return result


if __name__ == '__main__':
    steam_key = KeyGenerator()
    print(steam_key)
    print(steam_key.main(generation_type='Special'))
    print(steam_key.main(generation_type='Extended'))
    print(steam_key.main(generation_type='Standard'))
