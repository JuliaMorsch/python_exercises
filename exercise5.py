# Create a new guest list of people didin't RSVP

# guest list
guest_list = ("Alice", "Frank", "Josh", "Peter", "Sam")

# List of confirmated
confirmated = ["Frank", "Sam"]

# New list of people who didn't RSVP
not_rsvp = [guests for guests in guest_list if guests not in confirmated]

# Print the new list
print("Convidados que ainda não confirmaram: ")
for guest in not_rsvp:
    print(guest)
    