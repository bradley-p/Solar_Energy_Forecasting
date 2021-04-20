# Error Metrics 
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import median_absolute_error
# from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import explained_variance_score

"""
truth: actual values
pred: predicted values
Uses sklearn metrics to score several regression metrics
returns a dictionary of error metrics: keys =  [r2, MAE, MAPE, MSE, MedianAE, ExpVar]
"MAPE": mean_absolute_percentage_error(truth, pred),
"""
def compute_scores(truth, pred):
    truth = truth.reshape(-1,)
    pred = pred.reshape(-1,)
    error_return = {
        "r2": r2_score(truth, pred),
        "MAE": mean_absolute_error(truth, pred),
        "MSE": mean_squared_error(truth, pred),
        "MedianAE": median_absolute_error(truth, pred),
        "ExpVar": explained_variance_score(truth, pred),
    }

    return error_return
