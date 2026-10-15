marks_text = input("Enter marks separated by spaces: ").split()
marks = [float(mark) for mark in marks_text]
pass_fail = ["Pass" if mark >= 40 else "Fail" for mark in marks]
print("Marks:", marks)
print("Pass/fail:", pass_fail)
