
import re, sys
def tokenize(line):
	content = re.search(r"\(([^)]+)\)", line)
	if content:
		content = content.group(1).split('|')
		command = content[0]
		command = command.strip()
		if len(content) == 2:
			value = content[1]
			return [command, value]
		elif len(content) == 3:
			var = content[2]
			value = content[1]
			return [command, value, var]
		elif len(command) == 4:
			# assumes command is "init"
			try:
				type = content[1]
				name = content[2]
				value = content[3]
				return [command, type, name, value]
			except:
				pass
	else:
		print("No command or value was found.")