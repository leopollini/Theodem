require_relative 'Header'
require_relative 'Property'

# inherits from Propery since it is 90% a propery
# ## WILL BE CONVERTED TO A PROPERTY
class DefineType < DefineProperty
  def getInstance
    Type.new :this, args, @args
  end

  class Type < DefineProperty::Property
  end
end
