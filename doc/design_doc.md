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

## Modeling

While the specific methodology we employ can differ based on the problem, there are core principles we always want to follow:

 - End-to-end utility: the end result from every iteration should deliver minimum end-to-end utility so that we can benchmark iterations against each other and plug-and-play with the system.
 - Manual before ML: incorporate deterministic components where we define the rules before using probabilistic ones that infer rules from data → baselines.
 - Augment vs. automate: allow the system to supplement the decision making process as opposed to making the final decision.
 - Internal vs. external: not all early releases have to be end-user facing. We can use early versions for internal validation, feedback, data collection, etc.
 - Thorough: every approach needs to be well tested (code, data + models) and evaluated, so we can objectively benchmark different approaches.

#### v1: creating a gold-standard labeled dataset that is representative of the problem space.
#### v2: rule-based text matching approaches to categorize real estate.
#### v3: probabilistically predicting labels from content title and description.

### Feedback 

 - Enforce human-in-loop checks when there is low confidence in classifications.
 - Allow users to report issues related to misclassification.