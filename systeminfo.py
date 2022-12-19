import platform
import os
import socket
import psutil

from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

def get_system_info():
    # Get the system name
    system_name = platform.system()

    # Get the hostname
    hostname = socket.gethostname()

    # Get the release version
    release_version = platform.release()

    # Get the long version of the release
    long_version = platform.version()

    # Get the processor information
    processor = platform.processor()

    # Get the current user
    user = os.getlogin()

    # Get the total installed RAM
    total_ram = psutil.virtual_memory().total

    # Get the used RAM
    used_ram = psutil.virtual_memory().used

    return (system_name, hostname, release_version, long_version, processor, user, total_ram, used_ram)

class SystemInfoWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Get the system information
        system_name, hostname, release_version, long_version, processor, user, total_ram, used_ram = get_system_info()

        # Convert the total and used RAM to gigabytes
        total_ram_gb = total_ram / (1024**3)
        used_ram_gb = used_ram / (1024**3)

        # Create a vertical layout to hold the labels
        layout = QVBoxLayout()

        # Create a label for each piece of system information
        system_name_label = QLabel(f"System: {system_name}")
        hostname_label = QLabel(f"Hostname: {hostname}")
        release_version_label = QLabel(f"Release version: {release_version}")
        long_version_label = QLabel(f"Long version: {long_version}")
        processor_label = QLabel(f"Processor: {processor}")
        user_label = QLabel(f"Current user: {user}")
        total_ram_label = QLabel(f"Total RAM: {total_ram} bytes / {total_ram_gb:.2f} GB")
        used_ram_label = QLabel(f"Used RAM: {used_ram} bytes / {used_ram_gb:.2f} GB")

        # Add the labels to the layout
        layout.addWidget(system_name_label)
        layout.addWidget(hostname_label)
        layout.addWidget(release_version_label)
        layout.addWidget(long_version_label)
        layout.addWidget(processor_label)
        layout.addWidget(user_label)
        layout.addWidget(total_ram_label)
        layout.addWidget(used_ram_label)

        # Set the layout for the widget
        self.setLayout(layout)

if __name__ == "__main__":
    # Create a PyQt5 application
    app = QApplication([])

    # Create an instance of the SystemInfoWidget
    widget = SystemInfoWidget()

    # Show the widget
    widget.show()

    # Run the application loop
    app.exec_()
