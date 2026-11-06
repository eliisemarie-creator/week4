# TASK
# Create a program that asks the user:"Do you believe in magic? (yes/no)"
# Save the user's answer in a variable.
#
# - if the answer is "yes", display: "You get a magical unicorn!"
# - otherwise, display: "You get a regular horse."

magic = input("Do you believe in magic? (yes/no)").lower()

""" if magic == "yes":
    print("You get a magical unicorn!")
else:
    print("You get a regular horse.") """

#ternary
print("You get a magical unicorn!" if magic == "yes" else "You get a regular horse.")