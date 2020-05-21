high_income=True
#good_credit=True
if high_income or good_credit: #operator checks left to right thus before reaching good_credit the condition is true
    print("Eligible for loan")
else:
    print("not eligible for loan")