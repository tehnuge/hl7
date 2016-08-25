import unittest
from generate_hl7_string import GenerateHL7String

class TestMethods(unittest.TestCase):

	def test_general_case(self):
		g = GenerateHL7String()
		self.assertEqual(g.parse(1,'rick johnson',3,'M',5, 'E'), ("MSH|^~\&|MegaReg|XYZHospC|SuperOE|XYZImgCtr|20060529090131-0500||ADT^A01^ADT_A01|01052901|P|2.5\n"
																	"PID|||1|JOHNSON^RICK\n"
																	"PV1||E"))
	def test_invalid_inter_id(self):
		g = GenerateHL7String()
		self.assertEqual(g.parse('', 'rick johnson', '19620110', 'M', '123 foma st, newcastle, ca', 'E'), -1)
    #handle number and string for digit

	def test_invalid_patient_class(self):
		g = GenerateHL7String()
		self.assertEqual(g.parse('567567', 'rick johnson', '19620110', 'M', '123 foma st, newcastle, ca', 'A'), -1)

	def test_invalid_name(self):
		g = GenerateHL7String()
		self.assertEqual(g.parse('567567', 423423, '19620110', 'M', '123 foma st, newcastle, ca', 'A'), -1)

	def test_invalid_patient_class(self):
		g = GenerateHL7String()
		self.assertEqual(g.parse('567567', 'rick johnson', '19620110', 'g', '123 foma st, newcastle, ca', 'E'), -1)

if __name__ == '__main__':
    unittest.main()