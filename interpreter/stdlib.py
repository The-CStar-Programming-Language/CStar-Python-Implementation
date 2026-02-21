import os
import tokenize
import io
import platform
import sys
import math

def list_to_dict(lst):
  return dict(zip(lst[0], lst[1]))
def run_shell(command):
  comm = os.system(command)
  results = {
    "exit code": comm,
    "error": False
  }
  if results.get("exit code") != 0:
    results = {
      "exit code": comm,
      "error": True
    }
  return results
def py_to_token(code):
  rc = io.StringIO(code).readline
  tok = tokenize
 return list(tokenize.generate_tokens(io.StringIO(code).readline))
def dict_to_list(dictionary):
  return [list(dictionary.keys()), list(dictionary.values())]
def total_sum_of_lists(*lists):
	x = []
	return sum(x.append(sum(lst) for lst in lists))
def write_to_file(file, text):
	with open(file, 'w') as file:
		file.write(text)
def sys_info():
	return {
	"machine": platform.machine(),
	"release": platform.release(),
	"argv0": sys.argv[0],
	"system": platform.system(),
	"node": platform.node(),
	"processor": platform.processor(),
	"version": platform.version(),
	"name_of_os": os.name
	}
def round_function(function, decpoint):
	return round(eval(function), decpoint
def tangent(num):
	print(math.tan(num))
def acosine(num):
	print(math.acos(num))
def cosine(num):
	print(math.cos(num))