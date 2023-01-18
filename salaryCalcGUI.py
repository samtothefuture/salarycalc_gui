"""
1/12/2023 Program: salaryCalcGUI.py

GUI-based program where the user enters their hourly wage and the number of hours they've worked in order to calculate their salary

NOTE: the file breezypythongui.py must be in the same directory as this file for the app to run correctly!
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# other imports can go here

class SalaryCalcGUI(EasyFrame):

	# definition of the __init__() method which is our class constructor
	def __init__(self):
		# call the EasyFrame constructor method
		EasyFrame.__init__(self, title = "Salary Calculator", background = "honeydew", width = 340, height = 400, resizable = False)
		self.addLabel(text = "Salary Calculator", row = 0, column = 0, columnspan = 2, background = "honeydew", foreground = "darkgreen", font = Font(family = "Arial Black", size = 24), sticky = "NSEW")

		self.addLabel(text = "Enter your information below", row = 1, column = 0, columnspan = 2, background = "honeydew", font = Font(size = 10, slant = "italic", weight = "bold"), sticky = "NSEW")

		# USER INPUT
		self.addLabel(text = "Hourly Wage:", row = 2, column = 0, background = "honeydew", sticky = "NE", font = Font(size = 10))
		self.hourlyWage = self.addFloatField(value = 0.0, row = 2, column = 1, sticky = "NW", width = 10)

		self.addLabel(text = "Number of Hours Worked:", row = 3, column = 0, background = "honeydew", sticky = "NE", font = Font(size = 10))
		self.hoursWorked = self.addIntegerField(value = 0, row =3, column = 1, sticky = "NW", width = 10)

		# BUTTON
		self.button = self.addButton(text = "Calculate Salary", row = 4, column = 0, columnspan = 2, command = self.calculate)
		self.button["background"] = "darkgreen"
		self.button["foreground"] = "white"
		self.button["width"] = 25
		self.button["height"] = 2
		self.button["font"] = Font(size = 12)

		# RESULTS
		self.addLabel(text = "Your salary is: ", row = 5, column = 0, background = "honeydew", foreground = "darkgreen", font = Font(family = "Arial Black", size = 12), columnspan = 2, sticky = "NSEW")
		self.salary = self.addFloatField(value = 0.0, row = 6, column = 0, state = "readonly", sticky = "NE", precision = 2, width = 13)

	# DEFINE calculate() method
	def calculate(self):
		# INPUT from GUI
		wage = self.hourlyWage.getNumber()
		hours = self.hoursWorked.getNumber()

		# PROCESSING
		result = wage * hours

		# OUTPUT
		self.salary.setNumber(result)


# definition of the main() method which will establish class objects
def main():
	# instantiate an object from the class into mainloop()
	SalaryCalcGUI().mainloop()

# global call to the main() method
main()