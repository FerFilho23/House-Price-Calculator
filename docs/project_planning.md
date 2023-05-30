# Product Management

## Team

### Product:
 - Responsible for outlining the product requirements and approving them may involve product managers, executives, external stakeholders, etc.

### System design:

 - **Data engineering:** responsible for the data dependencies, which include robust workflows to continually deliver the data and ensuring that it’s properly validated and ready for downstream applications.

 - **Machine learning:** develop the probabilistic systems with appropriate evaluation.

 - **DevOps:** deploy the application and help autoscale based on traffic.

 - **UI/UX:** consume the system’s outputs to deliver the new experience to the user.

 - **Accessibility:** help educate the community for the new rollouts and to assist with decisions around sensitive issues.

 - **Site reliability:** maintain the application and to potentially oversee that online evaluation/monitoring workflows are working as they should.


### Project: 
 - Responsible for iterative engagement with the product and engineering teams to ensure that the right product is being built and that it’s being built appropriately may include project managers, engineering managers, etc.

## Deliverables

| Objective                                                                                 | Priority | Release | Status       |
|-------------------------------------------------------------------------------------------|----------|---------|--------------|
| Classify incoming real estate (with high precision) for our customers to easily discover. | High     | v1      | In-progress  |

| Deliverable                       | Contributors                              | Dependencies                                             | Acceptance criteria                                                  | Status      |
|-----------------------------------|-------------------------------------------|----------------------------------------------------------|----------------------------------------------------------------------|-------------|
| Labeled dataset for training      | Project DRI, labeling team, data engineer | Access to location of real estate with relevant metadata | Validation of ground-truth labels                                    | Complete    |
| Trained model with high precision | Data scientist                            | Labeled dataset                                          | Versioned, reproducible, test coverage report and evaluation results | In-progress |
| Scalable service for inference    | ML engineer, DevOps engineer              | Versioned, reproducible, tested and evaluated model      | Stress tests to ensure autoscaling capabilities                      | Pending     |


## Timeline

### v1: classify incoming content (with high precision) for our customers to easily discover.

- Exploration studies conducted by 06/10/2023
- Pushed to dev for A/B testing by 09/01/2023
- Pushed to staging with on-boarding hooks by 09/15/2023
- Pushed to prod by 10/01/2023
