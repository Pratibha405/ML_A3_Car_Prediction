import numpy as np
from testing import get_X, get_y, calculate_selling_price

feature_vals = [2014.00 , 21.14 , 103.52]
labels = ['cheap', 'average', 'expensive', 'very expensive']
possible_outputs = [f"Selling price is: {label}" for label in labels]

def test_get_Xy():
    # Ensure get_X is properly unpacking feature_vals into separate arguments
    X, features = get_X(*feature_vals)
    print(f"X: {X}, features: {features}")
    assert X.shape == (1, 3)
    #assert X.dtype == np.float64

    y = get_y(X)
    print(f"y: {y}")
    assert y.shape == (1,)

def test_calculate_selling_price_callback():
    output = calculate_selling_price(*feature_vals, 1)
    print(f"Output: {output}")
    
    # Check if the first element matches any of the possible labels
    assert output[0] in possible_outputs
    assert output[1:] == feature_vals