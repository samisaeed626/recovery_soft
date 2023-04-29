from app.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, Boolean, TIMESTAMP, ForeignKey


class Input(Base):
    """
    The model comprises several fields that store data related to each calculator input.
    Additionally, it includes a title field that allows users to assign a specific title
    to each calculation. For example, if we're calculating different aspects of a property,
    we can use the title field to differentiate between them.
    """
    __tablename__ = "calculator_inputs"

    id = Column(Integer, primary_key=True, index=True)
    # title is to store the title of every calculation for same property
    title = Column(String)
    
    # Add a foreign key column to reference property_detail.id
    property_detail_id = Column(Integer, ForeignKey('property_detail.id'))

    # Purchase
    purchase_price = Column(Float(precision=2))
    is_using_loan = Column(Boolean, default=False)
    closing_cost = Column(Float(precision=2))
    is_need_repairs = Column(Boolean, default=False)
    
    # Recurring Operating Expenses
    hoa_fee = Column(Float(precision=2))
    hoa_fee_annual_increase = Column(Float(precision=2))
    expense_interval = Column(String, choice=["ANNUALLY", "MONTHLY"])
    maintenance = Column(Float(precision=2))
    maintenance_annual_increase = Column(Float(precision=2))
    other_costs = Column(Float(precision=2))
    other_costs_annual_increase = Column(Float(precision=2))
    vacancy_rate = Column(Float(precision=2))
    property_tax = Column(Float(precision=2))
    property_tax_annual_increase = Column(Float(precision=2))
    management_fee = Column(Float(precision=2))
    total_insurance = Column(Float(precision=2))
    total_insurance_annual_increase = Column(Float(precision=2))
    
    # Income
    monthly_rent = Column(Float(precision=2))
    monthly_rent_annual_increase = Column(Float(precision=2))
    other_monthly_income = Column(Float(precision=2))
    other_monthly_income_annual_increase = Column(Float(precision=2))
    income_interval = Column(String, choice=["ANNUALLY", "MONTHLY"])
    
    # Sell
    is_know_sell_price = Column(Boolean, default=False)
    value_appreciation = Column(Float(precision=2))
    holding_length = Column(Float(precision=2))
    cost_to_sell = Column(Float(precision=2))
    
    utilities = Column(Float(precision=2))
    management = Column(Float(precision=2))
    
    created_at = Column(TIMESTAMP(timezone=True), server_default='now()')
