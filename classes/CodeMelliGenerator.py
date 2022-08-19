import itertools
import time


class CodeMelliGenerator:
    """
    Description: Code Melli Generator is a python class for generating Iranians national code by area code
    Author: Mohammadreza Naderi
    Github: https://github.com/naderidev
    """
    __area_code: str = None
    __codes: list = []
    __print_status_live: bool = False
    all_modes: int = 0
    valid_modes: int = 0

    def __init__(self, area_code: int, print_status_live: bool = False):
        self.__area_code: str = str(area_code)
        self.__print_status_live = print_status_live

    # ATTENTION: printing status in live will decrease speed
    def generate(self):
        self.all_modes = all_modes = 10 ** (10 - len(self.__area_code))
        counter = 0
        valid_modes = 0
        start_time = time.time()
        for number in itertools.product("0123456789", repeat=(10 - len(self.__area_code))):
            number = [*(self.__area_code + ("".join(number)))]
            remainder = self.__remainder(number)
            control_number = int(number[9])
            result = None
            if remainder < 2:
                if remainder == control_number:
                    result = int("".join(number))
            else:
                if control_number == str((11 - remainder)):
                    result = int("".join(number))
            counter += 1
            if result:
                valid_modes += 1
                self.__codes.append(result)
            self.print_status(counter, all_modes, valid_modes, (time.time() - start_time))
        self.valid_modes = valid_modes

    def print_status(self, counter, all_modes, valid_modes, execute_time: float = None):
        if not self.__print_status_live and all_modes != counter:
            return
        text = \
            f'generating... {round((counter / all_modes) * 100)}% ' \
            f'| STATUS:  valid modes: {valid_modes} ' \
            f'# ' \
            f'remaining modes: {(all_modes - counter)} '
        if execute_time and (counter == all_modes):
            text += f'# execute time: {round(execute_time, 1)} seconds ' if execute_time else ''
        print(f"{text}\r", end='')

    # returns the remainder division
    def __remainder(self, num_list: list[int | str]):
        return sum(
            [
                int(num_list[i]) * (10 - i) for i in range(0, 9)
            ]
        ) % 11

    def get_codes(self):
        return self.__codes
