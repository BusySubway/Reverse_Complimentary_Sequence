# Users enter a sequence
in_seq = input("Please enter a DNA sequence form 5'->3':")
#Transform the character string into list
sequence =list(in_seq.upper())
out_seq = []
# Check the validity of the input sequence
for check_base in sequence:
	if check_base not in ["A", "T", "C", "G"]:
		print("Please enter a valid base sequence!")
		quit()
# Make a comlimentary sequnce
for base in sequence:
	if base == "A":
		con_base = "T"
		out_seq.append(con_base)
	elif base == "T":
		con_base = "A"
		out_seq.append(con_base)
	elif base == "C":
		con_base = "G"
		out_seq.append(con_base)
	elif base == "G":
		con_base = "C"
		out_seq.append(con_base)
# Change the orientation of the complimentary senquence
out_seq.reverse()
# Output the final result
print(f"The complimentray sequence for the input is:")
print("".join(out_seq))