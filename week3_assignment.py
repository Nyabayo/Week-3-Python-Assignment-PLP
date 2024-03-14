def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount, if the discount is 20% or more.
    
    Parameters:
    - price: The original price of the item in Kenyan Shillings.
    - discount_percent: The percentage discount to be applied to the original price.
    
    Returns:
    The final price after applying the discount, or the original price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for the original price and discount percentage.
original_price = float(input("Enter the original price of the item in Kenyan Shillings: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price after applying the discount, if applicable.
final_price = calculate_discount(original_price, discount_percentage)

# Print the final price or the original price if no discount was applied.
if discount_percentage >= 20:
    print(f"The final price after applying the discount is: {final_price} Kenyan Shillings")
else:
    print(f"No discount was applied. The price remains: {original_price} Kenyan Shillings")
