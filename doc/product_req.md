# Product Requirements

## Background 
- customer: realtors, home buyers and sellers
- goal: discover the ideal price for a house with certain characteristics according to the real estate market and compare with other real estate
- pains: there are many market variables to be evaluated in the process of pricing a property and can be very time-consuming the search for real estate with competitive prices
- gains: calculating a price the price of a property quickly, objectively and fairly and automatically finding real estate with the same competitive price

## Value Proposition

- product: a service that takes into account all the intrinsic characteristics of a property (size, location, number of rooms, etc.) and of the real estate market for automatic pricing and comparing with existing real estate with competitive prices
- alleviates: speeds up the real estate pricing process, eliminating human errors and biases automatically
- advantages: customers only have to visit our product to price different types os real estate.

## Objectives

- Allow the customers to add and categorize their own real estate
- Discover real estate ads from trusted sources to bring into our platform
- Price incoming real estate (with high precision) for our customers to easily discover **[OUR FOCUS]**
- Display categorized real estate on our platform (recent, popular, recommended, etc.)

## Solutions

Develop a model that can classify and price the incoming real estate so that it can be organized by category on our platform.

### Core Features

 - ML service that will predict the correct price and category for incoming real estate. [OUR FOCUS]
 - User feedback process for incorrectly priced and classified content. 
 - Workflows to categorize and price content that the service was incorrect about or not as confident in. 
 - Duplicate screening for content that already exists on the platform.

### Integrations

- Categorized and priced content will be sent to the UI service to be displayed.
- Classification feedback from users will be sent to labeling workflows.

### Alternatives

- Allow users to add real estates manually (bottleneck).

### Constraints

- Maintain low latency (>100ms) when classifying incoming content. [Latency]
- Only recommend real estate from our list of approved real estates. [Security]
- Avoid duplicate content from being added to the platform. [UI/UX]

### Out-of-scope

- Identify relevant real estates beyond our approved list of real estates.
- Using full-text HTML from real estates links to aid in classification.
- Interpretability for why we recommend certain real estates.

## Feasibility

We have a dataset of labeled real estate from various trusted sources. We'll need to assess if it has the necessary categories to meet our objectives.