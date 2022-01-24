def convert(in_seq, out_seq):
	# Make a complimentary rule
	pair = {"A" : "T",
			"T" : "A",
			"C" : "G",
			"G" : "C"}
	# Get the complimentary sequence
	i = 0
	while i < len(in_seq):
		base = in_seq[i].title()
		c_base = pair[base]
		out_seq.append(c_base)
		i += 1

	# Change the orientation of the complimentary senquence
	out_seq.reverse()
	# Output the final result
	print(f"The complimentray sequence for the input is:")
	print("".join(out_seq))

# Users enter a sequence
in_seq = input("Please enter a DNA sequence from 5'->3':")
out_seq = []
convert(in_seq, out_seq)