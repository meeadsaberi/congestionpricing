# Here we provide the generalized cost functions for nonpricing and pricing liniks in the network considering a particular pricing regime called the joint distance and delay toll.
# Details of this pricing regime can be found in this paper: Gu, Z., Shafiei, S., Liu, Z., Saberi, M., 2018. Optimal distance- and time-dependent area-based pricing with the Network Fundamental Diagram. Transp. Res. Part C 95, 1-28.

# In total there are four generalized cost functions: intial and dynamic cost functions for nonpricing links, and initial and dynamic cost functions for pricing links.
# In AIMSUN, you have to allocate your generalized cost functions to the right groups of links, e.g., the cost functions for pricing links should be allocated to the group of links that forms your pricing zone.

# Initial cost function for nonpricing links
def cost(context, manager, section, turning, travelTime):
	free_flow_travel_time = section.length3D() / section.getSpeed() + turning.length3D() / turning.getSpeed()
	# The free-flow travel time above only considers time, it does no consider the so-called link attractiveness used in AIMSUN.
	# The following adjusted free-flow travel time considers attractiveness. You can set your own attractiveness weight in your experiment. If it is zero, the adjusted free-flow travel time is simply the free-flow travel time.
	# If the attractiveness weight is not zero, you also need to define what attractiveness is. Tipically you can use capacity.
	adjusted_free_flow_travel_time = free_flow_travel_time * (1 + manager.getAttractivenessWeight() * (1 - turning.getAttractiveness() / manager.getMaxTurnAttractiveness()))
	ic = adjusted_free_flow_travel_time
	return ic
	
# Dynamic cost function for nonpricing links
def cost(context, manager, section, turning, travelTime):
	free_flow_travel_time = section.length3D() / section.getSpeed() + turning.length3D() / turning.getSpeed()
	link_travel_time = max(turning.getStaTravelT(manager), free_flow_travel_time)
	dc = link_travel_time * (1 + manager.getAttractivenessWeight() * (1 - turning.getAttractiveness() / manager.getMaxTurnAttractiveness()))
	return dc
	
# Initial cost function for pricing links
def cost(context, manager, section, turning, travelTime):
	free_flow_travel_time = section.length3D() / section.getSpeed() + turning.length3D() / turning.getSpeed()
	adjusted_free_flow_travel_time = free_flow_travel_time * (1 + manager.getAttractivenessWeight() * (1 - turning.getAttractiveness() / manager.getMaxTurnAttractiveness()))
	# If pricing does not start from the beginning of your simulation, the initial cost function for pricing links is exactly the same as that for non-pricing links.
	# If pricing starts from the beginning of your simulation, you need to add the pricing term.
	ic = adjusted_free_flow_travel_time
	return ic
	
# Danamic cost function for pricing links
def cost(context, manager, section, turning, travelTime):
	free_flow_travel_time = section.length3D() / section.getSpeed() + turning.length3D() / turning.getSpeed()
	link_travel_time = max(turning.getStaTravelT(manager), free_flow_travel_time)
	adjusted_link_travel_time = link_travel_time * (1 + manager.getAttractivenessWeight() * (1 - turning.getAttractiveness() / manager.getMaxTurnAttractiveness()))
	# Here is the average value of travel time you use.
	vot = manager.getNetwork().getVehicleById(context.userClass.getVehicle().getId()).getValueOfTimeMean()
	link_travel_time_delay = max(0, turning.getStaTravelT(manager) - free_flow_travel_time)
	link_length = section.length3D() + turning.length3D()
	# Remember to set your own cost weight in your experiment to be nonzero (e.g. one). Otherwise pricing does not work at all.
	dc = adjusted_link_travel_time + manager.getUserDefinedCostWeight() * (section.getUserDefinedCost() * link_length * 3.6 + section.getUserDefinedCost2() * link_travel_time_delay) / vot
	return dc


# The following script allocates the above generalized cost functions to the nonpricing and pricing links, respectively. Remember to first allocate for nonpricing links and then for pricing links.

# Allocate for nonpricing links
turning_type = model.getType('GKTurning')
initial_cost_func = model.getCatalog().find('This is the id of your initial cost function for nonpricing links')
dynamic_cost_func = model.getCatalog().find('This is the id of your dynamic cost function for nonpricing links')
initial_cost_att = model.getColumn('GKTurning::initialFunctionAtt')
dynamic_cost_att = model.getColumn('GKTurning::dynamicFunctionAtt')
for type in model.getCatalog().getUsedSubTypesFromType(turning_type):
    for t in type.itervalues():
        t.setDataValueObject(initial_cost_att, initial_cost_func)
        t.setDataValueObject(dynamic_cost_att, dynamic_cost_func)

# Allocate for nonpricing links
pricing_turning = model.getCatalog().find('This is the id of the group of links that form your pricing zone')
initial_cost_func = model.getCatalog().find('This is the id of your initial cost function for pricing links')
dynamic_cost_func = model.getCatalog().find('This is the id of your dynamic cost function for pricing links')
initial_cost_att = model.getColumn('GKTurning::initialFunctionAtt')
dynamic_cost_att = model.getColumn('GKTurning::dynamicFunctionAtt')
for t in pricing_turning.getObjects():
	t.setDataValueObject(initial_cost_att, initial_cost_func)
	t.setDataValueObject(dynamic_cost_att, dynamic_cost_func)