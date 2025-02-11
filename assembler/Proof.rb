require_relative 'Header'

module Proof
  attr_accessor :theorem

  def self.init(theorem)
    @theorem = theorem
    @variables = {}
    @statements = []

    loadVariables
    loadStatements
  end

  def self.theorem
    @theorem
  end

  def self.loadVariables
    return unless @theorem.hypothesis.include? 'args'

    puts "theorem's arguments: " if DEBUG_MODE
    @theorem.hypothesis['args'].each do |k, v|
      puts "#{k}: #{v}" if DEBUG_MODE
      @variables[k] = Variable.new(k, v)
    end
  end

  def self.buildStatementArgs(args)
    res = {}
    args.each do |n, v|
      raise "Variable #{v} does not exist" if @variables[v].nil?

      res[n] = @variables[v]
    end
    res
  end

  def self.loadStatements
    return unless @theorem.hypothesis.include? 'requires'

    puts "theorem's statement requirements: " if DEBUG_MODE
    @theorem.hypothesis['requires'].each do |k|
      @statements << Theodem.statements[k['statement']].getInstance(buildStatementArgs(k['args']))
    end
  end

  # coincides with the field "procedure". At the end of the procedure the proof is called and completed
  # Each procedure field dested in a procedure field is a new context with different variables ("use" field carries variables, statements... to the underlying procedure)
  class Procedure
  end
end
