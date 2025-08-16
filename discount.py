def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    A discount is applied only if the discount_percent is 20% or higher.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The percentage of discount to apply.
    
    Returns:
    flot: The original price after applying discount if >= 20%, otherwise returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
    # --- Using the function ---
    price = 4000 # Example price
    discount_percent = 25 # Example discount percent

    final_price = calculate_discount(price, discount_percent)
    if discount_percent >= 20:
        print(f"The final price after a {discount_percent}% discount is: {final_price}")
    else:
        print(f"No discount applied. The price remains: {final_price}") 