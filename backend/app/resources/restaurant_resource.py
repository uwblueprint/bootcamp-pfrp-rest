class RestaurantResource(object):
    def __init__(self, name, address=None, type=None, budget=None, description=None, rating=None):
        # apply some validations
        if budget is not None:
            budget_values = {'LOW', 'MEDIUM', 'HIGH'}
            if budget.upper() not in budget_values:
                raise ValueError('Invalid budget value, it must be LOW, MEDIUM, or HIGH')
        
        if rating is not None:
            if int(rating) < 1 or int(rating) > 5:
                raise ValueError('Invalid rating value, it must be an integer between 1 and 5 inclusive')

        self.name = name
        self.address = address
        self.type = type
        self.budget = budget.upper() if budget is not None else budget
        self.description = description
        self. rating = int(rating) if rating is not None else rating
    