from os import path, listdir
from os.path import isdir, join
import argparse

public_framework_path = f'/System/Library/Frameworks'
private_framework_path = f'/System/Library/PrivateFrameworks'


def check_fuzzy(framework_name=''):
	framework_list = listdir(public_framework_path) or listdir(
	    private_framework_path)

	frameworks = [
	    f for f in framework_list if isdir(join(public_framework_path, f))
	    or isdir(join(private_framework_path, f))
	]

	return any(framework_name in sub for sub in frameworks)


def check_verbatim(framework_name=''):
	public_path = f'{public_framework_path}/{framework_name}'
	private_path = f'{private_framework_path}/{framework_name}'

	return path.isdir(public_path) or path.isdir(private_path)


def parse_framework_name(alert=''):
	questionable_framework = alert

	if len(alert) > 1:
		questionable_framework = alert.split()[0]

	return questionable_framework


def show_result(maybe_apple=False, framework_name=''):
	print(f'Done.', end='\n\n')
	confidence_rating = 'possibly' if maybe_apple else 'probably not'
	print(
	    f'`{framework_name}` is {confidence_rating} a framework created by Apple.'
	)


def check(alert=''):
	print(f'Checking frameworks in {public_framework_path}…')
	print(f'Checking frameworks in {private_framework_path}…')

	framework_name = parse_framework_name(alert=alert)

	verbatim_result = check_verbatim(framework_name=framework_name)

	fuzzy_result = check_fuzzy(framework_name=framework_name)

	maybe_apple = verbatim_result or fuzzy_result

	show_result(maybe_apple=maybe_apple, framework_name=framework_name)


def main():
	parser = argparse.ArgumentParser(
	    prog='maybeapple',
	    description=
	    'Haphazardly checks to see if a security alert is about an Apple framework.'
	)

	parser.add_argument('-alert',
	                    '--alert',
	                    required=True,
	                    action='append',
	                    help='the alert message that looks fishy')

	args = parser.parse_args()

	check(alert=args.alert[0])


if __name__ == "__main__":
	main()
