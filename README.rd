Comments instructions:
	require: this object requires whatever comes next to be declared in the json formatted file

Classes:
	- Property: variable property. MUST have description, type and equiv declared
		* field equiv: whenever a variable is called in a "use" field inside a procedure step, all the statement inside equiv will be added to ambient
		* property names beginning with _ and in caps lock are built-ins, eg. _INHERIT
		
	- Statement: this is a formal statement. Deep compares will be used in order to verify theorem hypothesis'

	- Operation: this is a simple operation. Takes some arguments and returns a new variable created from those arguments. 
		* CAN require a proof: in which case an equiv of the property to be appended MUST be present in current environment; defaults to false
		* CAN contain field "inherit_types": if the selected variable is of one of the specified types then the returned variable is set to the same type

	- Variables: since variables are only property-carriers (and not value-carriers), only have type and properies as content.
		* variables are VECTORS of properties (and type)
		* are uniquely identified by their names; will replace placeholders in operations, thorems...

	- Types: object types. Simply a reference to a list of properties (field requires)
		* field inheritable can be set to a list of operation which preserve the type (closed inter closed is closed ...)

General:
	- ALL variables are placeholders
	- variable declared as args are followed by a vector of requirements (empty => no requirements)
	- default type is Set, always refered to implicitly (all variables are also type Set)
	- type field is treated as a property
	- Theorems (field extract) and operations (field returns_list) can return a map of variables, in which is said where to get the variable (_new if the variable is created inside the return field, args if it was one of the arguments...)

Fields Types:
	- "variables": {"var_name":[]}
	- "var_name": [{type}, {property}, {property} ...]
	- "procedure": {"0":{}, ... "proof":{}}
	- "proof": {"theorem":"theo_name", "args":{}}
	- "args" (inside call): {"placeholder":"var_name", "placeholder1":{"operation":"var_creator", "args":{}}} => variables must meet requirements defined in definition
	- "args" (inside definition/hypothesis): {"placeholder":[], ...} => defines arguments requirements.
	- "requirements": [{"statement":"...","args":"{}}] => contain a series of statemens required for the call. "args" and "requirements are merged before checking if call complies
	- "inherit_types":{"var_name":["singleton","_all",...]} => specifies all inheritable types

