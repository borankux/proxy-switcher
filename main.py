import re
import sys
import subprocess as sb
import commands



def run(cmd, args = []):
	args.insert(0, cmd)
	return sb.check_output(args).decode('utf-8')


def get_device_list():
	re_list = r"\([0-9]+\) [a-zA-Z \/\-0-9]+"
	result = sb.check_output(['networksetup', '-listnetworkserviceorder']).decode('utf-8')
	device_list  = re.findall(re_list, result)
	devices = []
	for device in device_list:
		devices.append(device.split(')')[1].strip())

	return devices


def open_proxy(device):
	run('networksetup', ['-setwebproxystate', device, 'on'])
	run('networksetup', ['-setsecurewebproxystate', device, 'on'])



def close_proxy(device):
	run('networksetup', ['-setwebproxystate', device, 'off'])
	run('networksetup', ['-setsecurewebproxystate', device, 'off'])


device = get_device_list()[0]

cmd = sys.argv[1]
if cmd == 'on':
	open_proxy(device)
else:
	close_proxy(device)