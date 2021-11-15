import unittest
import register


class TestRegister(unittest.TestCase):

    # Test email validation
    def test_validate_email(self):
        self.assertEqual(register.validate_email(
            'deshpandeav19.comp@coep.ac.in'), True)
        self.assertEqual(register.validate_email(
            'joshiav19.comp@coep.ac.in'), True)
        self.assertEqual(register.validate_email(
            'deshpandeav19.compcoep.ac.in'), False)
        self.assertEqual(register.validate_email(
            'deshpandeav19.comp@coep'), False)

    # Test mobile number validation
    def test_validate_mobileno(self):
        self.assertEqual(register.validate_mobileno('9404089167'), True)
        self.assertEqual(register.validate_mobileno('940408916'), False)
        self.assertEqual(register.validate_mobileno('94040891656'), False)
        self.assertEqual(register.validate_mobileno('8967945672'), True)

    #Test Aadhar Card Validation
    def test_validate_aadhar(self):
        self.assertEqual(register.validate_aadhar('1234'), False)
        self.assertEqual(register.validate_aadhar('12558745'), False)
        self.assertEqual(register.validate_aadhar('1254789644'), False)
        self.assertEqual(register.validate_aadhar('123456789111'), True)
        self.assertEqual(register.validate_aadhar('123456789000'), True)

    #Test MIS Validation
    def test_validate_misno(self):
        self.assertEqual(register.validate_misno('111903020'), True)
        self.assertEqual(register.validate_misno('111903022'), True)
        self.assertEqual(register.validate_misno('12547896449'), False)
        self.assertEqual(register.validate_misno('12345678911100'), False)
        self.assertEqual(register.validate_misno('1234'), False)

    #Test extension Validation - test if file uploaded is pdf or not
    def test_validate_extension(self):
        self.assertEqual(register.validate_extension('abc.pdf'), True)
        self.assertEqual(register.validate_extension('pqr.pdf'), True)
        self.assertEqual(register.validate_extension('abc.txt'), False)
        self.assertEqual(register.validate_extension('pqr.txt'), False)
        self.assertEqual(register.validate_extension('pqr.png'), False)
    
    #Test Date of Birth Validation
    def test_validate_dob(self):
        self.assertEqual(register.validate_dob('12-01-2001'), True)
        self.assertEqual(register.validate_dob('12-31-2001'), False)
        self.assertEqual(register.validate_dob('14-07-2005'), False)
        self.assertEqual(register.validate_dob('30-03-2000'), True)
        self.assertEqual(register.validate_dob('12-01-2010'), False)


if __name__ == '__main__':
    unittest.main()
