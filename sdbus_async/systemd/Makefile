# Documentation:
# https://python-sdbus.readthedocs.io/en/latest/code_generator.html

# Generate interface class from dbus introspection xml of some systemd binary:
generate_systemd1_interface:
	systemd --bus-introspect /org/freedesktop/systemd1 >org.freedesktop.systemd1.xml

	python -m sdbus gen-from-file  org.freedesktop.systemd1.xml >interfaces.py
	black --skip-string-normalization interfaces.py

# The alternative is to generate the interface code from a running systemd:
# python -m sdbus gen-from-connection org.freedesktop.systemd1 /org/freedesktop/systemd1
