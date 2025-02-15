require_relative 'Header'

# Stuff loading implementation
module Theodem
  # loads statement declaration
  def self.loadStatements
    @content['statement'].each do |n, c|
      puts "Adding new statement: #{n}"
      raise 'Duplicate statement name ' if @statements.include? n

      @statements[n] = DefineStatement.new n, c
    end
  end

  # loads property declaration
  def self.loadProperites
    @content['property'].each do |n, p|
      puts "Adding new property: #{n}"
      raise 'Duplicate property name ' if @properties.include? n

      @properties[n] = DefineProperty.new n, p
    end
  end

  # loads oepration declaration
  def self.loadOperations
    @content['operation'].each do |n, p|
      puts "Adding new operation: #{n}"
      raise 'Duplicate operation name ' if @operations.include? n

      @operations[n] = Operation.new n, p
    end
  end

  # loads types
  def self.loadTypes
    # DEFAULT TYPES SECTION
    @types['Set'] = DefineType.new 'Set', {}
    @types[''] = DefineType.new 'Set', {}
    # END DEFAULT TYPES SECTION
    @content['type'].each do |n, p|
      puts "Adding new type: #{n}"
      raise 'Duplicate type name ' if @types.include? n

      @types[n] = DefineType.new n, p
    end
  end

  # loads theorems declaration
  def self.loadTheorems
    @content['theorem'].each do |n, p|
      puts "Added new theorem: #{n}"
      raise 'Duplicate theorem name ' if @theorems.include? n

      @theorems[n] = Theorem.new n, p
    end
  end
end

# default initializer interface
class ContentLoader
  attr_accessor :name, :args, :equiv, :also, :description, :kind

  def initialize(name, content)
    @name = name
    @content = content
    @equiv = @content['equiv']
    @equiv ||= []
    @also = @content['also']
    @also ||= []
    @args = @content['args']
    @args ||= {}
    @description = @content['description']
    @description ||= ''
    @kind = @content['kind']
    @kind ||= ''
  end
end
