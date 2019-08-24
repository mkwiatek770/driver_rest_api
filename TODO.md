1. Create appropriate apps
2. Set up PostgreSQL app
3. Create models
Advice
AdviceQuestion
AdviceQuestionAnswer
AdviceTraining
AdviceTrainingUser
TrainingTask
User

Extend user model by adding points
AdviceTraining has field tasks which is M2M field of TrainingTask
AdviceQuestion is question for advice, AdviceQuestionAnswer is an answer for specific question

4. Create serializers
5. Create viewsets
6. Write unit tests
7. Wrap project into docker container 
