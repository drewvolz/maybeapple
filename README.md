# maybeapple

This project aims to evaluate if a framework requesting permissions is created by Apple.

It relies on you copy/pasting the message of a service requesting your password from a dialogue box. 

Please check for yourself in all cases. This should never be used in production and exists only for toy purposes.

## Hacking

```sh
$ python3 -m venv ./venv
$ source ./venv/bin/activate # or activate.csh or activate.fish
$ pip install -r requirements.txt
$ python -m maybeapple
```

## Example

```sh
python -m maybeapple -a 'DeviceManagement wants to use your confidential information stored in "iOS Backup" in your keychain.'
Checking frameworks in /System/Library/Frameworks…
Checking frameworks in /System/Library/PrivateFrameworks…
Done.

`DeviceManagement` is possibly a framework created by Apple.
```
