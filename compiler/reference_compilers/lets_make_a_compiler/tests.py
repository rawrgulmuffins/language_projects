import logging
import select
import subprocess
import unittest


class CompilerTestBase(unittest.TestCase):
    """Contains the code that actually runs tests and reports their results.
    """

    compiler_name = "cradle"

    # Command that is used to run the compiler.
    run_compiler_string = "./{}".format(compiler_name)

    # This is the command and arguments that will build the compiler
    build_compiler_commands = ["fpc", "{}.pas".format(compiler_name)]

    @classmethod
    def _build_compiler(cls):
        """Runs the compliation step before running any tests. If this fails,
        abort the tests.

        Subprocess handling code from
        https://stackoverflow.com/questions/18273962/python-subprocess-call-hangs
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
        if compile_process.stdout in rlist and verbose:
            # Adjust the number of bytes read however you like, 1024 seems to work 
            # pretty well for me. 
            logger.debug(compile_process.stdout.read(1024))

        # Log stderr, always
        if compile_process.stderr in rlist:
            # Same as with stdout, adjust the bytes read as needed.
            logger.error(compile_process.stderr.read(1024))

    @classmethod
    def setUpClass(cls):
        if cls is CompilerTestBase:
            cls._build_compiler()

    def _compile_program(self):
        """If the compiler succesfully compiled

        TODO: FINISH ME
        """
        pass

    def run_program(self):
        """Given a successfully compiled compiler and a successfully compiled
        program actually run the program and return the results.

        TODO: FINISH ME
        """
        pass

    def test_if_segfaulted(self):
        """

        TODO: FINISH ME
        """
        pass

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
        test_program = bytes(test_program, "utf-8")
        actual_assembly = sub_process.communicate(test_program)
        actual_assembly = self.clean_formatting(actual_assembly[0])
        expected_assembly = self.clean_formatting(expected_assembly)
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
        mov %eax, 1
        """
        self.run_test(test_program, expected_assembly)

    def test_blank_program(self):
        test_program = ""
        expected_assembly = b""""""
        self.run_test(test_program, expected_assembly)

class TestArithmetic(CompilerTestBase):
    """
    NOTE: turning off for now until we get a basic working program.
    """
    '''
    def test_addition_no_space(self):
        test_program = "1+2"
        # Need to remember that mov is dest, source
        expected_assembly = b"""
        mov %eax, 1
        mov %ebx, %eax
        mov %eax, 2
        add %eax, %ebx"""
        self.run_test(test_program, expected_assembly)

    def test_addition_spaces(self):
        test_program = "1+2"
        # Need to remember that mov is dest, source
        expected_assembly = b"""
        mov %eax, 1
        mov %ebx, %eax
        mov %eax, 2
        add %eax, %ebx"""
        self.run_test(test_program, expected_assembly)

    def test_subtraction_no_space(self):
        test_program = "1+2"
        # Need to remember that mov is dest, source
        expected_assembly = b"""
        mov %eax, 1
        mov %ebx, %eax
        mov %eax, 2
        add %eax, %ebx"""
        self.run_test(test_program, expected_assembly)

    def test_subtraction_spaces(self):
        test_program = "1 - 2"
        # Need to remember that mov is dest, source
        expected_assembly = b"""
        mov %eax, 1
        mov %ebx, %eax
        mov %eax, -2
        sub %eax, %ebx"""
        self.run_test(test_program, expected_assembly)
    '''


if __name__ == "__main__":
    logging.basicConfig()
    unittest.main()
