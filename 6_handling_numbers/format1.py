import locale as lc
lc.setlocale(lc.LC_ALL, "us")

fp_number = 12345.6789
print("{:.2f}".format(fp_number))          # 12345.68
print("{:.4f}".format(fp_number))          # 12345.6789
print("{:,.2f}".format(fp_number))         # 12,345.68
print("{:15,.2f}".format(fp_number))       #       12,345.68

int_number = 12345
print("{:d}".format(int_number))           # 12345
print("{:,d}".format(int_number))          # 12,345

fp_number = .12345
print("{:.0%}".format(fp_number))          # 12%
print("{:.1%}".format(fp_number))          # 12.3%

print(lc.format("%d", 12345, grouping=True))


