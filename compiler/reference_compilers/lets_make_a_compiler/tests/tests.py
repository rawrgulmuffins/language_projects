"""

NOTE: for now this is just intended to be run as python -m tests from the
compiler directory (parent directory of this file).
"""
import logging
import os
import select
import subprocess
import unittest


class CompilerTestBase(unittest.TestCase):
    """Contains the code that actually runs tests and reports their results.
    """

    # TODO: make this a command line argument
    maxDiff = None

    @classmethod
    def setUpClass(cls):

        # Static Configuration
        # TODO: Move static configuration to a config file.
        cls.verbose = False
        cls.compiler_name = "cradle"
        cls.paths_to_test = ["./", "../"]
        # End static configuration

        cls.compiler_path = cls.get_compiler_path(cls.compiler_name)

        # Command that is used to run the compiler.
        cls.run_compiler_string = "{}".format(cls.compiler_path)

        # This is the command and arguments that will build the compiler
        cls.file_extension = "pas"
        build_compiler_commands = ["fpc", "{}.{}".format(
            cls.compiler_path,
            cls.file_extension)]

        if cls is CompilerTestBase:
            cls._build_compiler()

    def potential_paths(cls, potential_paths):
        for path in potential_paths:
            yield "{}{}".format(path, cls.compiler_name)

    @classmethod
    def get_compiler_path(cls, compiler_name):
        """

        # TODO: change into a class attribute function.
        """
        # Currently only supporting calling from test directory and project
        # directory.
        for compiler_path in cls.potential_paths(cls, cls.paths_to_test):
            if os.path.isfile(compiler_path):
                return compiler_path

        raise RuntimeError("No compiler could be found to test. Either the"
            "compiler paths are incorrectly configured or the compiler name"
            "is incorrectly configured.")

    @classmethod
    def _build_compiler(cls):
        """Runs the compliation step before running any tests. If this fails,
        abort the tests.

        Subprocess handling code from
        https://stackoverflow.com/questions/18273962/python-subprocess-call-hangs

        # TODO: COMPILE USING THE PROJECT MAKEFILE!!!
        # No, really, that needs to be the next workflow improvement.
        """
        logger = logging.getLogger(__name__)
        is_running = lambda: compile_process.poll() is None

        compile_process = subprocess.Popen(
            cls.build_compiler_commands,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,)

        # Grab all the output from stdout and stderr and log it
        while is_running():
            rlist, wlist, xlist = select.select(
                [compile_process.stdout, compile_process.stderr], [], [], 1)

        # Log stdout, but don't spam the log
        if compile_process.stdout in rlist and cls.verbose:
            # Adjust the number of bytes read however you like, 1024 seems to work 
            # pretty well for me. 
            logger.debug(compile_process.stdout.read(1024))

        # Log stderr, always
        if compile_process.stderr in rlist:
            # Same as with stdout, adjust the bytes read as needed.
            logger.error(compile_process.stderr.read(1024))

    def clean_formatting(self, raw_text):
        """Simple string cleaner that ignores all prior whitespace and left
        hand side whitespace.
        """
        raw_text = raw_text.decode("utf-8")
        # Remove all whitespace leading up to actual text.
        raw_text = raw_text.strip()
        split_text = raw_text.split("\n")
        cleaned_text = [line.lstrip() for line in split_text]
        return "\n".join(cleaned_text)

    def run_test(self, test_program, expected_assembly):
        sub_process = subprocess.Popen(
            [self.run_compiler_string],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT)
        try:
            test_program = bytes(test_program, "utf-8")
        except AttributeError:
            # Already a string, do nothing.
            pass
        actual_assembly = sub_process.communicate(test_program)
        actual_assembly = self.clean_formatting(actual_assembly[0])
        expected_assembly = self.clean_formatting(expected_assembly)
        if self.verbose:
            # TODO: switch to logging statements.
            print("------- actual assembly ----------")
            print(actual_assembly)
            print("------- expected assembly ----------")
            print(expected_assembly)
            print("------- end ----------")
        self.assertEqual(actual_assembly, expected_assembly)

class TestInitialization(CompilerTestBase):

    def test_single_literal(self):
        test_program = "1"
        expected_assembly = b"""
        .text
        .globl _main
            _main:
            subq $8, %rsp
            movq $1, %rax
            movq $0, %rdi
            call _exit
        """
        self.run_test(test_program, expected_assembly)

    def test_blank_program(self):
        test_program = ""
        expected_assembly = b"""
        .text
        .globl _main
        _main:
            subq $8, %rsp
            movq $0, %rdi
            call _exit
        """
        self.run_test(test_program, expected_assembly)

class TestArithmetic(CompilerTestBase):

    division_assembly = b"""
    .text
    .globl _main
    _main:
        subq $8, %rsp
        movq $2, %rax
        push %rax
        movq $2, %rax
        movq %rax, %rbx
        pop %rax
        xor %rdx, %rdx
        div %rbx
        movq $0, %rdi
        call _exit
    """

    multiplication_assembly = b"""
    .text
    .globl _main
    _main:
        subq $8, %rsp
        movq $1, %rax
        push %rax
        movq $2, %rax
        pop %rbx
        mul %rbx
        movq $0, %rdi
        call _exit
    """

    addition_assembly = b"""
    .text
    .globl _main
    _main:
        subq $8, %rsp
        movq $1, %rax
        push %rax
        movq $2, %rax
        pop %rbx
        add %rax, %rbx
        movq $0, %rdi
        call _exit
    """

    subtraction_assembly = b"""
    .text
    .globl _main
    _main:
        subq $8, %rsp
        movq $1, %rax
        push %rax
        movq $2, %rax
        pop %rbx
        sub %rax, %rbx
        movq $0, %rdi
        call _exit
    """
    def test_addition_no_space(self):
        test_program = "1+2"
        self.run_test(
            test_program,
            expected_assembly=self.addition_assembly)

    @unittest.skip("Spaces not included yet.")
    def test_addition_spaces(self):
        test_program = "1 + 2"
        self.run_test(
            test_program,
            expected_assembly=self.addition_assembly)

    @unittest.skip("Errors not included yet.")
    def test_addition_missing_left_literal(self):
        test_program = "+2"
        expected_assembly = b"Error: Addop Expected"
        self.run_test(test_program, expected_assembly)

    @unittest.skip("Errors not included yet.")
    def test_addition_missing_right_literal(self):
        test_program = "1+"
        expected_assembly = b"Error: Addop Expected"
        self.run_test(test_program, expected_assembly)

    def test_subtraction_no_space(self):
        test_program = "1-2"
        self.run_test(
            test_program,
            expected_assembly=self.subtraction_assembly)

    @unittest.skip("Spaces not included yet.")
    def test_subtraction_spaces(self):
        test_program = "1 - 2"
        self.run_test(
            test_program,
            expected_assembly=self.subtraction_assembly)

    @unittest.skip("Errors not included yet.")
    def test_subtraction_missing_right_literal(self):
        test_program = "1-"
        expected_assembly = b"Error: Subop Expected"
        self.run_test(test_program, expected_assembly)

    def test_multiplciation_no_spaces(self):
        test_program = "1*2"
        self.run_test(
            test_program,
            expected_assembly=self.multiplication_assembly)

    @unittest.skip("Spaces not included yet.")
    def test_multiplciation_spaces(self):
        test_program = "1 * 2"
        self.run_test(
            test_program,
            expected_assembly=self.multiplication_assembly)

    @unittest.skip("Errors not included yet.")
    def test_invalid_mul_operation(self):
        test_program = "1*"
        expected_assembly = b"Error: Mulop Expected"
        self.run_test(test_program, expected_assembly)

    @unittest.skip("Spaces not included yet.")
    def test_division_spaces(self):
        test_program = "2 / 2"
        self.run_test(
            test_program,
            expected_assembly=self.division_assembly)

    def test_division_no_spaces(self):
        test_program = "2/2"
        self.run_test(
            test_program,
            expected_assembly=self.division_assembly)

    @unittest.skip("Errors not included yet.")
    def test_invalid_div_operation(self):
        test_program = "1/"
        expected_assembly = b"Error: Divop Expected"
        self.run_test(test_program, expected_assembly)


class TestParenthese(CompilerTestBase):


    pre_boiler_plate = b"""
    .text
    .globl _main
        _main:
        subq $8, %rsp""".lstrip()

    post_boiler_plate = b"""
        movq $0, %rdi
        call _exit""".lstrip()

    def add_boiler_plate(self, assembly):
        boilered_assembly = self.pre_boiler_plate
        boilered_assembly += assembly
        boilered_assembly += self.post_boiler_plate
        return boilered_assembly

    def constant_assembly(self, integer):
        constant_assembly = b"""\n    movq $1, %rax
        """
        constant_assembly = self.add_boiler_plate(constant_assembly)
        return constant_assembly
 
    def addition_assembly(self, left_int, right_int):
        addition_string = """
        movq ${}, %rax
        push %rax
        movq ${}, %rax
        pop %rbx
        add %rax, %rbx
        """.format(left_int, right_int)
        addition_assembly = bytes(addition_string, "utf-8")
        return addition_assembly

    def test_parens_no_expression(self):
        test_program = "()"
        expected_assembly = self.pre_boiler_plate
        expected_assembly += b"\n"
        expected_assembly += self.post_boiler_plate
        self.run_test(test_program, expected_assembly)

    def test_parens_signle_digit(self):
        test_program = "(1)"
        expected_assembly = self.constant_assembly(1)
        self.run_test(test_program, expected_assembly)

    def test_parens_sigle_expression(self):
        test_program = "(1+2)"
        expected_assembly = self.addition_assembly(1, 2)
        expected_assembly = self.add_boiler_plate(expected_assembly)
        self.run_test(test_program, expected_assembly)

    def test_parens_nested_expression(self):
        test_program = "(1(2+(3)))"
        expected_assembly = self.addition_assembly(2, 3)
        expected_assembly += self.addition_assembly(1, 5)

        expected_assembly = self.add_boiler_plate(expected_assembly)
        self.run_test(test_program, expected_assembly)

    def test_parens_broad_expressions(self):
        test_program = "(1+(2+3))+4"
        expected_assembly = self.addition_assembly(2, 3)
        expected_assembly += self.addition_assembly(1, 5)
        expected_assembly += self.addition_assembly(6, 5)

        expected_assembly = self.add_boiler_plate(expected_assembly)
        self.run_test(test_program, expected_assembly)


if __name__ == "__main__":
    logging.basicConfig()
    unittest.main()
