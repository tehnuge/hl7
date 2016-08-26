import re

class GenerateHL7String:
	"""inter_id : int
		name : string
		dob : format is YYYY/MM/DD or YYYYMMDD
		sex : M, F
		address : street_address, city, state zip_code
		patient_class: E, I, O, P, R, B, C, N, U
	"""
	def parse(self, inter_id, name, dob, sex, address, patient_class):
		inter_id = self.process_id(inter_id)
		if inter_id is False:
			print 'invalid Patient ID'
			return -1

		name = self.process_name(name)
		if name is False:
			print 'invalid name'
			return -1

		dob = self.process_dob(dob)
		if dob is False:
			print 'invalid DOB'
			return -1

		sex = self.process_sex(sex)
		if sex is False:
			print 'invalid sex'
			return -1

		address = self.process_address(address)
		if address is False:
			print 'invalid address'
			return -1

		patient_class = self.process_patient_class(patient_class)
		if patient_class is False:
			print 'invalid patient class choice (E, I, O, P, R, B, C, N, U)'
			return -1

		#msh is hardcoded
		msh = 'MSH|^~\&|MegaReg|XYZHospC|SuperOE|XYZImgCtr|20060529090131-0500||ADT^A01^ADT_A01|01052901|P|2.5\n'
		pid = 'PID|||' + inter_id + '||' +  name + '||' + dob + '|' + sex + '|||' + address + '\n'
		pv1 = 'PV1||'+ patient_class
		res = msh + pid + pv1
		return res

	def process_id(self, inter_id):
		if isinstance(inter_id, (int, long)):
			if len(str(inter_id)) > 20:
				return False
			return str(inter_id)
		elif len(inter_id) > 0:
			inter_id = inter_id.split()[0]
			if len(inter_id) > 20:
				return False
			else:
				return inter_id
		return False

	def process_name(self, name):
		if isinstance(name, (int, long)):
			return False
		first_name, mid_name, last_name, suf_name = ['','','','']
		names = name.upper().split()
		if len(names) == 3 or len(names) == 4:
			first_name = names[0]
			mid_name = names[1]
			last_name = names[2]
			if len(names) == 4:
				suf_name = names[3]
		elif len(names) == 2:
			first_name = names[0]
			last_name = names[1]
		elif len(names) == 1:
			last_name = names[0]
		result = last_name + '^' + first_name + '^' + mid_name + '^' + suf_name
		return result.strip('^')

	def process_dob(self, dob):
		if isinstance(dob, (int, long)):
			if len(str(dob)) != 8:
				return False
			else:
				return str(dob)
		else:
			match_obj = re.match(r'\d{4}\/\d{2}\/\d{2}$', dob)
			if match_obj is not None or len(dob) != 8:
				return False
			elif match_obj:
				dob = dob.translate(None, '/')
		return dob

	def process_sex(self, sex):
		if isinstance(sex, (int, long)):
			return False
		sex = sex.upper()
		sex_choices = {'M', 'F'}
		if sex not in sex_choices:
			return False
		return sex

	def process_address(self, address):
		if isinstance(address, (int, long)):
			return False
		res = ''
		address = address.split(',')
		if len(address) != 3:
			return False
		state_zip = address[2].split()
		address.remove(address[2])
		address.extend(state_zip)
		for i, word in enumerate(address):
			address[i] = word.strip()

		res += '^'.join(address)
		return res


	def process_patient_class(self, patient_class):
		patient_class = patient_class.upper()
		patient_class_choices = {'E', 'I', 'O', 'P', 'R', 'B', 'C', 'N', 'U' }
		if patient_class not in patient_class_choices:
			return False
		return patient_class



