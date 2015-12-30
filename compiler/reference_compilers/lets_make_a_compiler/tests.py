import unittest
import subprocess
from pprint import pprint

class TestInitialization(unittest.TestCase):

    def setUp(self):
        self.run_compiler_string = "./cradle"

    def clean_formatting(self, raw_text):
        """Simple string cleaner that ignores all prior whitespace and left
        hand side whitespace.

        TODO: Need to fix output formatting still.
        """
        raw_text = raw_text.decode("utf-8")
        # Remove all whitespace leading up to actual text.
        raw_text = raw_text.strip()
        split_text = raw_text.split("\n")
        cleaned_text = [line.lstrip() for line in split_text]
        return "".join(cleaned_text)

    def run_test(self, test_program, expected_assembly):
        sub_process = subprocess.Popen(
            [self.run_compiler_string],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT)
        test_program = bytes(test_program, "utf-8")
        actual_assembly = sub_process.communicate(test_program)
        actual_assembly = self.clean_formatting(actual_assembly[0])
        expected_assembly = self.clean_formatting(expected_assembly)
        pprint(actual_assembly)
        pprint(expected_assembly)
        self.assertEqual(actual_assembly, expected_assembly)

    def test_single_literal(self):
        test_program = "1"
        expected_assembly = b"""
        mov %eax, $1
        """
        self.run_test(test_program, expected_assembly)

if __name__ == "__main__":
    unittest.main()
