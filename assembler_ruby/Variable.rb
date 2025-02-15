require_relative 'Header'

class Variable
  def initialize(name, content)
    puts "New variable: #{name}" if DEBUG_MODE
    @name = name
    @content = content
    @properties = []
    @type = ['Set']
    loadProperites
  end

  # loads variable properties inside @properties vector
  def loadProperites
    @content.each do |k|
      if k.keys[0] == 'type'
        @type << Theodem.types[k.values[0]].getInstance
      else
        @properties << Theodem.properties[k.values[0]].getInstance(p)
      end
    end
  end

  def addProperty(*props)
    props.each do |p|
      raise TypeError if p.instanceof(Property)

      @content << p
    end
  end

  def expandProperties
    @properties.each do |p|
    end
  end
end
