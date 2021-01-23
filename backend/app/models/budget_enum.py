from . import db

budget_enum = db.Enum(
    'LOW',
    'MEDIUM',
    'HIGH',
    name='budget'
)
