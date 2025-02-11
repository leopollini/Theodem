require_relative 'Header'

# requires: description, type, args
class DefineStatement < ContentLoader
  attr_accessor :name, :args

  def getInstance(args)
    Statement.new @name, @args, args
  end

  # balls.
  class Statement
    def initialize(name, args, vars)
      @name = name
      @args = args
      @argsnames = []
      @args.each_key do |a|
        @argsnames << a
        @args[a] = vars[a]
        puts "assigned #{vars[a]} to #{a}" if DEBUG_MODE
      end
      puts "args names: #{@argsnames}"
    end

    def ==(other)
      @content == other.content
    end
  end
end
