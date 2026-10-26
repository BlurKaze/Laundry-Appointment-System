import sys, os
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QMainWindow,
                             QGridLayout, QPushButton, QVBoxLayout,
                             QHBoxLayout, QProgressBar, QLineEdit)

from PyQt6.QtGui import QIcon
from pathlib import Path
from Washer_button import CustomerCard


class addAppointment(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Laundry Dashboard System")
        self.setFixedSize(800, 527)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        main_container = QWidget()
        main_container.setLayout(main_layout)

        self.setCentralWidget(main_container)

#======= header ======== start
        header_layout = QHBoxLayout()
        header_container = QWidget()
        header_container.setLayout(header_layout)

        self.back_btn = QPushButton()
        back_btn_icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Btn icons/back_btn.png")
        self.back_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.back_btn.setIcon(QIcon(back_btn_icon_path))
        self.back_btn.setIconSize(QSize(40,40))
        self.back_btn.setFlat(True)
        self.back_btn.setToolTip("Back")

        self.header_text = QLabel("Book Appointment")
        self.confirm_btn = QPushButton("Confirm")
        self.confirm_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.confirm_btn.setFixedSize(200, 40)

        header_layout.addWidget(self.back_btn, stretch=0)
        header_layout.addWidget(self.header_text, stretch=2)
        header_layout.addWidget(self.confirm_btn, stretch=1)

#======= header ======== end
        progress_layout = QHBoxLayout()
        progress_layout.setContentsMargins(0,0,0,0)
        progress_layout.setSpacing(0)

        progress_container = QWidget()
        progress_container.setLayout(progress_layout)

        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        progress_layout.addWidget(self.progress_bar)
 
        inputDetails_layout = QVBoxLayout()
        inputDetails_layout.setContentsMargins(0,5,0,0)
        inputDetails_layout.setSpacing(0)
        
        inputDetails_container = QWidget()
        inputDetails_container.setLayout(inputDetails_layout)

        personalDetails_layout = QGridLayout()
        personalDetails_layout.setContentsMargins(0,0,0,0)
        personalDetails_layout.setHorizontalSpacing(15)
        personalDetails_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        personalDetails_container = QWidget()
        personalDetails_container.setLayout(personalDetails_layout)

        self.personalDetails_label = QLabel("Personal Details")

        self.first_name_label = QLabel("First Name")
        self.first_name_label.setContentsMargins(10,0,0,0)
        self.first_name = QLineEdit()
        self.first_name.setFixedWidth(250)
        self.first_name.setContentsMargins(10,0,0,0)

        self.last_name_label = QLabel("Last Name")
        self.last_name_label.setContentsMargins(10,0,0,0)
        self.last_name = QLineEdit()
        self.last_name.setFixedWidth(250)
        self.last_name.setContentsMargins(10,0,0,0)

        self.phone_no_label = QLabel("Phone No.")
        self.phone_no_label.setContentsMargins(10,0,0,0)
        self.phone_no = QLineEdit()
        self.phone_no.setFixedWidth(250)
        self.phone_no.setContentsMargins(10,0,0,0)

        self.email_address_label = QLabel("Email Address")
        self.email_address_label.setContentsMargins(10,0,0,0)
        self.email_address = QLineEdit()
        self.email_address.setFixedWidth(250)
        self.email_address.setContentsMargins(10,0,0,0)

        self.home_address_label = QLabel("Home Address")
        self.home_address_label.setContentsMargins(10,0,0,0,0)
        self.home_address = QLineEdit()
        self.email_address.setFixedWidth(250)
        self.email_address

        personalDetails_layout.addWidget(self.personalDetails_label, 0, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        personalDetails_layout.addWidget(self.first_name_label, 1, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        personalDetails_layout.addWidget(self.last_name_label, 1, 1, alignment=Qt.AlignmentFlag.AlignLeft)
        personalDetails_layout.addWidget(self.phone_no_label, 1, 2, alignment=Qt.AlignmentFlag.AlignLeft)
        personalDetails_layout.addWidget(self.email_address_label, 3, 0, alignment=Qt.AlignmentFlag.AlignLeft)

        personalDetails_layout.addWidget(self.first_name, 2, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        personalDetails_layout.addWidget(self.last_name, 2, 1, alignment=Qt.AlignmentFlag.AlignLeft)
        personalDetails_layout.addWidget(self.phone_no, 2, 2, alignment=Qt.AlignmentFlag.AlignLeft)
        personalDetails_layout.addWidget(self.email_address, 4, 0, alignment=Qt.AlignmentFlag.AlignLeft)

        services_layout = QGridLayout()
        specification_layout = QGridLayout()
        schedule_layout = QGridLayout()

        main_layout.addWidget(header_container, stretch=0)
        main_layout.addWidget(progress_container, stretch=0)
        main_layout.addWidget(inputDetails_container, stretch=0)

        inputDetails_layout.addWidget(personalDetails_container, stretch=0)
      #  inputDetails_layout.addWidget(services_layout)
      #  inputDetails_layout.addWidget(specification_layout)
      #  inputDetails_layout.addWidget(schedule_layout)

        #object names
        main_container.setObjectName("main_container")

        header_container.setObjectName("header_layout")
        self.back_btn.setObjectName("back_btn")
        self.header_text.setObjectName("header_text")
        self.confirm_btn.setObjectName("confirm_btn")

        progress_container.setObjectName("progress_layout")

        inputDetails_container.setObjectName("inputDetails_layout")
        self.personalDetails_label.setObjectName("personal_details_label")
        self.first_name_label.setObjectName("first_name_label")
        self.last_name_label.setObjectName("last_name_label")
        self.phone_no_label.setObjectName("phone_no_label")
        self.email_address_label.setObjectName("email_address_label")

                                    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    addAppointment_qss = Path(__file__).with_name("addAppointment.qss")
    app.setStyleSheet(addAppointment_qss.read_text())
    window = addAppointment()
    window.show()
    sys.exit(app.exec())
