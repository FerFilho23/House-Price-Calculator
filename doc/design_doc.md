# Engineering

## Data 

### Training:
- Access to input [data](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data) and labels for training.
- Information on feature origins and schemas.
- Was there sampling of any kind applied to create this dataset?
- Are we introducing any data leaks?

### Production:
- Access to timely batches of new real estate from scattered [sources](https://rapidapi.com/collection/best-real-estate-apis)
- How can we trust that this stream only has data that is consistent with what we have historically seen?

### Labeling

- Labeling: labeled using general zoning classifications of real estate.

- Features: text features (title and description) to provide signal for the classification task.

- Labels: reflect the real estate categories we currently display on our platform:

['Agriculture',
 'Commercial',
 'Floating Village Residential',
  ...
 'other']

## Evaluation

### Metrics

We want to be able to classify incoming data with high precision to display them properly. For the projects that we categorize as 'other', we can recall any misclassified real estate using manual labeling workflows. We may also want to evaluate performance for specific classes or slices of data.

### Offline evaluation

We'll be using the historical dataset for offline evaluation. We'll also be creating slices of data that we want to evaluate in isolation.

### Online evaluation

Online evaluation ensures that our model continues to perform well in production and can be performed using labels or, in the event we don't readily have labels, proxy signals.

 - Manually label a subset of incoming data to evaluate periodically. 
 - Asking the initial set of users viewing a newly categorized content if it's correctly classified. 
 - Allow users to report misclassified content by our model.

It's important that we measure real-time performance before committing to replace our existing version of the system.

 - Internal canary rollout, monitoring for proxy/actual performance, etc. 
 - Rollout to the larger internal team for more feedback. 
 - A/B rollout to a subset of the population to better understand UX, utility, etc.
